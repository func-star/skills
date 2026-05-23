# 引用与标注规范

`write-ai-article` skill 的引用格式细则。所有产出文章统一遵守。

## 1. 内联事实引用

任何事实声明（数据、版本、行为、官方说法）都要内联超链接到原始出处：

```markdown
Claude Code 在 [v2.0 的发布说明](https://docs.claude.com/en/release-notes/claude-code) 里引入了 Skills 机制，
默认从 `~/.claude/skills/` 加载。
```

链接文字应该是**信息源的名字**，不是"点这里"或"详见此文"。

## 2. 翻译类文章的原文标注

如果整篇文章是翻译/改写自英文原文，开头第二段就要给出原文出处块：

```markdown
> 原文：[Building effective agents](https://www.anthropic.com/research/building-effective-agents) by Anthropic, 2024-12
> 译者注：本文在原文基础上补充了 2026 年 Claude Code Skills 的实现细节。
```

不要把原文标注藏到文末——读者一开始就该知道这是译稿还是原创。

## 3. 主观 / 客观 callout

正文默认全部按客观陈述读。需要主观判断时用 callout 显式区分：

```markdown
> 原文说：Anthropic 推荐每个 skill 单一职责。
> 我的看法：在大型项目里这条容易破，因为跨技能的状态共享缺手段。
> 分析：从 SKILL.md 的 frontmatter 字段看，目前没有 cross-skill state 的官方机制。
```

三种标签的区分：

| 标签 | 含义 | 例子 |
|---|---|---|
| `原文说：` | 引用原作者的观点或描述（不是字面引用，是观点归属） | "原文说：agent 应该尽量保持工具集小。" |
| `我的看法：` | 作者本人的主观判断、推测、偏好 | "我的看法：5 个工具是经验上限。" |
| `分析：` | 基于事实的推理（不是纯主观，但也不是引用） | "分析：从 SKILL.md 的字段命名看，未来可能加入 dependencies 字段。" |

混着用会让读者分不清哪句是事实哪句是推测。

## 4. 术语首次出现

中文技术文章里术语首次出现，挂英文原文：

```markdown
检索增强生成（Retrieval-Augmented Generation, RAG）的核心思路是……
```

后续可以只用中文（"RAG"），但首次必须给出原文。模型名（GPT-4、Claude Opus 4.7）、API 名（Files API）、协议名（MCP）直接用英文写。

## 5. 版本与日期

涉及版本号、日期、价格、限额时：
- **写绝对值，不写"最新"**："Gemini 2.5 Flash Image 在 2026-01 GA"，不要写"最新版本的 Gemini"。
- **价格附日期**："$0.039/张（2026-01 标价）"。
- **限额引官方文档**：链接到 [Gemini pricing page](https://ai.google.dev/gemini-api/docs/pricing)。

## 6. 截图与示意图归属

- **截图**：截官方界面/文档时不需要署名，但 caption 要写清是从哪个页面截的。
- **示意图**：自己用 `generate-article-image` skill 生成的图，不需要署名。
- **借用别人的图**：原作者署名 + 链接，写在 caption 里：

  ```markdown
  ![Transformer 结构图](assets/fig-2.png)
  > 图源：[The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) by Jay Alammar
  ```

## 7. 代码出处

代码片段来自外部（仓库、论文、文档）：

```markdown
\`\`\`python
# 出处：https://github.com/anthropics/anthropic-sdk-python/blob/main/examples/...
from anthropic import Anthropic
\`\`\`
```

自己写的最小示例不需要标。

## 8. 不要做的事

- **不要伪造 URL**。每个链接都要真存在；不确定就先 WebFetch 验一下。
- **不要把"据说""有人说"当出处**。说不清原作者就不写这句。
- **不要把 LLM 训练数据当事实**。任何 "GPT-4 知道 X" 类的话需要附带原始文档链接。
- **不要在引用 callout 里塞链接**。callout 是用来标观点归属的，链接走正文内联。
