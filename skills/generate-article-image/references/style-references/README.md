# 风格参考样图

这个目录放视觉风格的**参考样图**，给 `generate-article-image` skill 写 prompt 时做锚点。

## 用途

`prompt-recipes.md` 里的风格描述（"hand-lettered sans-serif"、"terracotta orange"）只是文字，模型会按自己的理解发挥。结果之一：中文标题经常飘成毛笔字、楷体、各种书法变体。

样图是给模型（和写 skill 的人）的视觉锚——"看，要这种感觉"。

下次写新 recipe，或现有 recipe 的输出不稳定时，参照这里的样图调整文字描述。

## 来源

这 6 张 `.webp` 来自 [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) 仓库下的 `screenshots/article-illustrator-styles/`，是宝玉（[@dotey](https://x.com/dotey)）的 article illustrator skill 的风格样图。

下载用于本仓库的**参考、学习用途**，不重新分发；如果原仓库版权或许可有变化，相应在此处移除。

## 样图清单

| 文件 | 原风格名 | 字体观察 | 适配场景 |
|---|---|---|---|
| `notion.webp` | notion | 无显式文字，纯线稿图标 | 配合干净文字布局的极简插图 |
| `minimal.webp` | minimal | 几乎无文字 | 留白极致、信息密度低 |
| `warm.webp` | warm | "GROW TOGETHER"——粗体圆角手写（rounded marker handwriting），暖棕色 | 暖色调、有手作温度的解释类插图 |
| `sketch-notes.webp` | sketch-notes | **粗衬线大写（bold serif all-caps）+ 黑色细笔涂鸦元素**（星星 / 箭头 / 螺旋） | **当前强制规范** —— 知识点拆解、信息密度高的场景 |
| `flat-doodle.webp` | flat-doodle | "CREATE!"——黑色 marker 手写，配粉彩涂鸦 | 童趣、活泼、彩色 |
| `elegant.webp` | elegant | "CREATIVE THINKING"——金色细衬线大写（thin elegant serif） | 高端、克制、品质感 |

## 中文字体的强约束

字体规范要在两个极端之间守住中间地带：

- **一端要避免**：飘到毛笔字 / 楷体 / 行楷 / 草书 / 书法 / 中文 ink-brush / 宋体衬线——Gemini 在中文上最容易跑到这些方向
- **另一端要避免**：死板成 Heavy 工业感黑体（思源黑体 Heavy / 苹方 Heavy 那种"广告牌"质感）——失去 sketchnote 的手作温度
- **目标中间地带**：**手写感无衬线体（hand-lettered sans-serif）**——字型清晰、轮廓规整，但笔画有轻微手作不规则，像设计师用粗水笔（chisel-tip marker）手写信息图标题。字重 Bold / Semi-bold

当前强制规范：

- **字形**：手写感无衬线体（hand-lettered sans-serif），无衬线，字型清晰、有手作温度
- **字重**：Bold / Semi-bold（不要 Heavy）
- **中文呈现参考**：思源黑体 Bold + 手作不规则感（视觉描述，非具体字体名）
- **英文呈现参考**：Caveat Brush / Patrick Hand / Architects Daughter 等 hand-lettered 字体的氛围
- **明确避开**：宋体（serif）、仿宋、楷体、行楷、毛笔锋、书法字体、中文 ink-brush、Heavy 工业感死板黑体
- **装饰**：标题周围允许 sketchnote 风的黑色细笔涂鸦元素——星星 / 箭头 / 螺旋 / 强调圈
- **配色**：保留 Anthropic 主调（米白底 + 赭橙强调 + 深炭黑文字），sketchnote 辅色（莫兰迪粉 / 薄荷绿 / 暖琥珀 / 雾蓝灰）只用于次级装饰，不抢主标题

## 怎么挂到 prompt 里

Gemini 3 Pro Image preview 支持参考图作为风格输入。脚本目前还没接这个能力——后续如果想"强制锁定一种字体风格"，扩展 `scripts/generate_image.py` 加 `--reference-image` 参数把这里的样图一并传入是最直接的做法。
