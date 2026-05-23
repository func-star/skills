---
name: generate-article-image
description: 用 Google Gemini 图像 API ("Nano Banana" 家族) 生成手绘信息图风格的文章配图（默认 16:9 横版、米色纸面、手写感无衬线体标题、等距 3D 微缩场景），保存到文章目录的 assets/ 下。配合 write-ai-article 使用：当 article.md 里有 ![FIG-N](assets/fig-N.png) 占位与 gen-hint 注释时调用。需要 GEMINI_API_KEY 环境变量。
---

## Goal

生成一张符合本仓库图像风格规范的文章配图，保存到 `<article-dir>/assets/fig-N.png`。

## Preconditions

- `GEMINI_API_KEY` 环境变量已设置（从 [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey) 获取）。
- Python 3.10+ 可用，且 `google-genai` SDK 在调用脚本的 Python 环境里可导入。
- 用户已给出图描述（中文），或者 `article.md` 里有 `<!-- gen-hint: ... -->` 注释。
- 目标 `<article-dir>/assets/` 目录存在或可创建。

### Python 环境推荐（解决 PEP 668）

macOS Homebrew Python 默认拒绝 `pip install`（PEP 668 "externally managed"）。规范做法是用专用 venv：

```bash
python3 -m venv ~/.venvs/gemini-image
~/.venvs/gemini-image/bin/pip install google-genai
```

之后调用脚本时显式用 venv 的 python：

```bash
GEMINI_API_KEY="$(cat ~/.gemini-api-key)" \
  ~/.venvs/gemini-image/bin/python ${SKILL_DIR}/scripts/generate_image.py \
  --prompt "..." --out "..."
```

如果系统 Python 不受 PEP 668 限制（Linux 发行版自带、conda、uv 管理的 Python 等），直接 `pip install google-genai` 即可，无需 venv。**永远不要**用 `--break-system-packages` 绕过——会污染 Homebrew 的 Python 环境。

## Steps

### 1. 取图描述

来源有两类：
- **直接用户输入**：用户在对话中描述要生成什么图。
- **从 article.md 抽取**：用户给一个 markdown 文件路径，找到 `<!-- gen-hint: ... -->` 注释，按顺序逐张生成。

### 2. 选模板

读 `${SKILL_DIR}/references/prompt-recipes.md`，按图类型挑模板：

| 图类型 | 模板 |
|---|---|
| 信息图卡片（多块短文字） | `infographic-card` |
| 等距 3D 微缩场景 | `isometric-scene` |
| 时间轴 / 演进图 | `timeline` |
| 流程图 / 架构图 | `flow-diagram` |
| 概念解释手绘 | `hand-drawn-explainer` |

不确定就用 `infographic-card`，最通用。

### 3. 加风格指纹

读 `${SKILL_DIR}/references/image-style-guide.md`，把 8 项风格指纹拼到 prompt 末尾。

最终 prompt 结构：

```
<中文核心描述>

Style: <英文风格后缀，来自 image-style-guide.md>
Aspect ratio: 16:9 (默认) / 9:16 / 1:1
```

中文写"画什么"，英文写"怎么画"——Gemini 对英文 style descriptor 响应更稳。

### 4. 选模型

| 模型 | 用什么场景 | 价格 |
|---|---|---|
| `gemini-2.5-flash-image` (Nano Banana) | 默认；速度快，免费额度 50 张/天 | 付费 $0.039/张 |
| `gemini-3-pro-image-preview` (Nano Banana Pro) | 文字渲染多的信息图；需要锐利字体 | 仅付费 |

用户没指定时用 flash。文章封面或文字密集的信息图用 pro。

### 5. 调脚本

```bash
python ${SKILL_DIR}/scripts/generate_image.py \
  --prompt "<完整 prompt>" \
  --out "<article-dir>/assets/fig-N.png" \
  --model flash \
  --aspect 16:9
```

`--model` 接受 `flash` / `pro`（脚本内部映射到完整模型名）。

### 6. 处理结果

- **成功**：脚本打印 `Saved: <path>` 和一行 SynthID 水印提示。把 caption 建议打印给用户。
- **`GEMINI_API_KEY` 未设置**（退出码 2）：把脚本输出的设置指引转述给用户，停下。
- **安全过滤拦截**（退出码 3）：把脚本输出的 block reason 原样转给用户，建议改 prompt（例如去掉人脸、品牌名），**不要**静默重试。
- **SDK 未安装**：脚本会提示 `pip install google-genai`，按提示装。

### 7. 反馈给文章

如果是从 `article.md` 批量生成的，每张生成完后：
- 验证图存在。
- 打印一行 caption 建议，方便用户回填到 markdown 的 `![FIG-N: <caption>](...)` 里。

## Success criteria

- PNG 文件落到 `<article-dir>/assets/fig-N.png`。
- 用户至少看到一次 SynthID 水印提示（每次会话第一张图后说一次即可，不要每张都打）。
- 如果从 `article.md` 批量生成，所有 `gen-hint` 都对应到了一张图。

## Stop conditions

- **没有 `GEMINI_API_KEY`**：停，把如何获取 key 的指引转给用户，**不要**尝试无认证调用。
- **同一类 prompt 连续被安全过滤拦截**：停，请用户改图思路（去掉真实人名、敏感主题、品牌商标），**不要**循环重试。
- **目标文件已存在**：默认不覆盖。停下问"覆盖 / 改名 / 跳过"。
- **用户要求超过 5 张/次**：停下提示免费额度 50/天，确认要不要继续。

## Notes

- **SynthID 水印**：所有 Gemini 生成的图都带不可见水印，无法去除。这是 Google 的策略，不是 bug，给用户说一次即可。
- **不会画好的东西**：写实人脸（容易拙）、特定品牌 logo（容易侵权且过滤）、密集小字（flash 模型会糊，pro 模型也只是相对好）。这些场景提示用户用其他方式（截图 / 手绘 / 设计师介入）。
- **横版 vs 竖版**：默认 16:9 横版（PC / 大屏单图阅读最舒适，是当前主要查看场景）。移动端单图场景才用 9:16 竖版。脚本 `--aspect` 不传时按 16:9。
- 这个 skill 不负责把图回写到 `article.md`——它只产出图。回写 markdown 的工作交给用户或 `write-ai-article` skill 的下一轮。
