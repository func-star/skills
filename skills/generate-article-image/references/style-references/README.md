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

宝玉的样图原图都是英文标题，**英文样图用粗衬线**——但**中文场景下我们采用粗黑体而不是粗宋体**。原因：中文宋体衬线在 Gemini 渲染下容易飘成楷体或书法变体；中文黑体的方头方尾在视觉上和英文粗衬线一样"有力量"，且不容易飘。

当前强制规范（中文场景）：

- **字形**：**粗黑体**（heavy sans-serif），笔画粗细均匀、方头方尾、**无衬线**、结构端正、字怀紧凑
- **中文等价字体名**：思源黑体 Heavy（Source Han Sans Heavy）/ Noto Sans CJK Black / PingFang SC Heavy / 苹方粗 / 阿里巴巴普惠体 Heavy / HarmonyOS Sans Black
- **英文等价字体名**：Inter Black / Helvetica Black / Source Sans 3 Black
- **明确避开**：宋体（serif）、仿宋、楷体、行楷、毛笔锋、书法字体、中文 ink-brush
- **装饰**：标题周围允许 sketchnote 风的黑色细笔涂鸦元素——星星 / 箭头 / 螺旋 / 强调圈
- **配色**：保留 Anthropic 主调（米白底 + 赭橙强调 + 深炭黑文字），sketchnote 辅色（莫兰迪粉 / 薄荷绿 / 暖琥珀 / 雾蓝灰）只用于次级装饰，不抢主标题

### 实际样本参考

用户截图的"图增强 RAG 链路"标题（赭橙色"图增强" + 黑色"RAG"+ 赭橙"链路"，字体为粗黑体）是这个 skill 字体规范的视觉锚点。所有 prompt 里的字体描述要朝这种效果走。

## 怎么挂到 prompt 里

Gemini 3 Pro Image preview 支持参考图作为风格输入。脚本目前还没接这个能力——后续如果想"强制锁定一种字体风格"，扩展 `scripts/generate_image.py` 加 `--reference-image` 参数把这里的样图一并传入是最直接的做法。
