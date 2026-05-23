#!/usr/bin/env python3
"""Generate an article illustration via the Gemini image API.

Usage:
    python generate_image.py --prompt "..." --out path/to/fig.png [--model flash|pro] [--aspect 9:16|16:9|1:1]

Env:
    GEMINI_API_KEY (required)  Get one at https://aistudio.google.com/app/apikey

Exit codes:
    0  success
    1  bad arguments / unexpected error
    2  GEMINI_API_KEY missing
    3  safety filter blocked the prompt
    4  SDK not installed and user did not install it
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

MODEL_ALIASES = {
    "flash": "gemini-2.5-flash-image",
    "pro": "gemini-3-pro-image-preview",
}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate an article illustration via Gemini.")
    p.add_argument("--prompt", required=True, help="Full image prompt (Chinese description + English style suffix).")
    p.add_argument("--out", required=True, help="Output PNG path.")
    p.add_argument("--model", default="flash", choices=list(MODEL_ALIASES.keys()),
                   help="flash = gemini-2.5-flash-image (free 50/day), pro = gemini-3-pro-image-preview (paid only).")
    p.add_argument("--aspect", default="9:16", choices=["9:16", "16:9", "1:1"],
                   help="Aspect ratio. Default 9:16 (vertical, mobile-friendly).")
    return p.parse_args()


def check_api_key() -> str:
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        sys.stderr.write(
            "error: GEMINI_API_KEY is not set.\n"
            "  1. Get a key at https://aistudio.google.com/app/apikey\n"
            "  2. export GEMINI_API_KEY=<your-key>\n"
            "  3. Re-run this command.\n"
        )
        sys.exit(2)
    return key


def import_sdk():
    try:
        from google import genai  # noqa: F401
        from google.genai import types  # noqa: F401
        return genai, types
    except ImportError:
        sys.stderr.write(
            "error: google-genai SDK is not importable from this Python.\n"
            "\n"
            "  Recommended (PEP 668 / Homebrew Python safe):\n"
            "    python3 -m venv ~/.venvs/gemini-image\n"
            "    ~/.venvs/gemini-image/bin/pip install google-genai\n"
            "    # then invoke this script via that venv's python:\n"
            "    ~/.venvs/gemini-image/bin/python " + sys.argv[0] + " ...\n"
            "\n"
            "  Plain (if your Python is not externally-managed):\n"
            "    pip install google-genai\n"
            "\n"
            "  Do NOT use --break-system-packages on Homebrew Python.\n"
        )
        sys.exit(4)


def generate(prompt: str, out_path: Path, model_alias: str, aspect: str) -> None:
    genai, types = import_sdk()

    model_id = MODEL_ALIASES[model_alias]
    client = genai.Client()

    try:
        response = client.models.generate_content(
            model=model_id,
            contents=[prompt],
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE"],
                image_config=types.ImageConfig(aspect_ratio=aspect),
            ),
        )
    except Exception as e:
        sys.stderr.write(f"error: Gemini API call failed: {e}\n")
        sys.exit(1)

    block_reason = _extract_block_reason(response)
    if block_reason:
        sys.stderr.write(
            f"error: safety filter blocked the prompt.\n  Reason: {block_reason}\n"
            "  Rewrite the prompt (drop real names, brands, sensitive subjects) and retry.\n"
        )
        sys.exit(3)

    image_bytes = _extract_image_bytes(response)
    if image_bytes is None:
        sys.stderr.write(
            "error: response contained no image.\n"
            f"  Raw response candidates: {getattr(response, 'candidates', None)}\n"
        )
        sys.exit(1)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(image_bytes)
    print(f"Saved: {out_path}")
    print("Note: Gemini images carry an invisible SynthID watermark. This is Google policy and cannot be removed.")


def _extract_block_reason(response) -> str | None:
    pf = getattr(response, "prompt_feedback", None)
    if pf and getattr(pf, "block_reason", None):
        return str(pf.block_reason)
    for cand in getattr(response, "candidates", []) or []:
        fr = getattr(cand, "finish_reason", None)
        if fr and str(fr).upper() in {"SAFETY", "IMAGE_SAFETY", "PROHIBITED_CONTENT"}:
            return str(fr)
    return None


def _extract_image_bytes(response) -> bytes | None:
    for cand in getattr(response, "candidates", []) or []:
        content = getattr(cand, "content", None)
        if not content:
            continue
        for part in getattr(content, "parts", []) or []:
            inline = getattr(part, "inline_data", None)
            if inline and getattr(inline, "data", None):
                return inline.data
    return None


def main() -> None:
    args = parse_args()
    check_api_key()
    generate(args.prompt, Path(args.out).expanduser(), args.model, args.aspect)


if __name__ == "__main__":
    main()
