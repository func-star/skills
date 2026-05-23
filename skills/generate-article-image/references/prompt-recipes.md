# Prompt 模板库

5 个常用 prompt 模板。所有模板末尾都拼上 `image-style-guide.md` 里的通用 style 后缀。

格式约定：`{占位符}` 是要替换的内容，其余保持。

**默认画幅**：16:9 横版（PC 单图阅读友好）。
**默认配色**：Anthropic / Claude desktop 调色——米白底 + 赭橙主强调 + 深炭黑文字 + sketchnote 辅色装饰。
**默认字体**：**手写感无衬线体（hand-lettered sans-serif）**——字型清晰、轮廓规整，但笔画有轻微手作不规则，像设计师用粗水笔（chisel-tip marker）手写信息图标题的感觉。字重 Bold / Semi-bold，**不要 Heavy 工业感**。无衬线。

**这是强制规范，两端要守住**：一端别飘到毛笔字 / 楷体 / 书法 / 宋体，另一端别死板成机械工业字。中间的"手写感清晰无衬线"才是目标。

---

## Recipe 1: `infographic-card`（信息图卡片，最通用）

**何时用**：把一段文字内容（定义、对比、清单）视觉化。文章里大多数图位都适合这个。

```
画一张手绘 sketchnote 风信息卡，16:9 横版。主题是「{主题中文}」。
卡片底色米白带纸面纹理，标题"{标题}"放在顶部正中。
**字体强制**：标题用**手写感无衬线体（hand-lettered sans-serif）**——字型清晰、轮廓规整，但笔画有轻微手作不规则，像设计师用粗水笔手写信息图标题。字重 Bold / Semi-bold（**不要 Heavy 那种工业死板感**，也**不要毛笔字、不要楷体、不要行楷、不要宋体衬线**）。
标题周围配 3-5 个黑色细笔 sketchnote 涂鸦元素（星星、箭头、螺旋、强调圈）。
配色：标题用赭橙色（terracotta orange #CC785C）+ 深炭黑（#191919）混排。

正文区分成 {N} 个并列卡片（N ∈ 2..4），左右横向排列：
  - {卡片 1 标题}：{一句话说明}
  - {卡片 2 标题}：{一句话说明}
  - ...
每个卡片左上角配一个手绘小图标。
卡片内文字也用手写感无衬线体，比标题略小。
整体留白充足，无装饰性元素。

Style: hand-drawn sketchnote-style infographic on warm cream/beige paper
(#F5F0E8 tone). Title and labels in HAND-LETTERED SANS-SERIF typography —
clean letterforms with slight stroke irregularity, marker-handwriting feel,
Bold to Semi-bold weight (NOT Heavy industrial sans-serif, NOT stiff machine
font). NO SERIFS. ABSOLUTELY NEVER brush calligraphy, NEVER 毛笔字, NEVER
楷体, NEVER 行楷, NEVER 书法, NEVER 宋体, NEVER serif fonts. Primary accent
in terracotta burnt orange (#CC785C tone), text and outlines in rich charcoal
black (#191919). Title surrounded by black thin-line sketchnote doodles
(stars, arrows, swirls). Secondary doodle palette: dusty pink, sage green,
soft amber. NEVER pure red, NEVER neon. Generous whitespace. Avoid
photorealism, avoid dense small text.
```

**默认模型**：`pro`（文字渲染密集，flash 容易糊）。

---

## Recipe 2: `isometric-scene`（等距 3D 微缩场景）

**何时用**：解释一个系统的整体结构、各组件如何在空间上协作。

```
画一个 45° 顶视的等距 3D 微缩卡通场景，16:9 横版。
场景表现「{系统/概念名}」：
  - 前景：{核心组件}
  - 中景：{支撑组件 1}、{支撑组件 2}
  - 背景：{环境元素}
组件之间用细线或路径连接表示数据/请求流向。
diorama 风格，无外框，世界悬浮在米白背景上。
材质柔和，PBR 质感，自然光照。
配色：米白底 + 赭橙（terracotta orange）主强调 + 深炭黑文字。
**所有标签必须是手写感无衬线体（hand-lettered sans-serif）**——清晰但有手作温度，**不要毛笔字、不要楷体、不要宋体、不要 Heavy 工业死板黑体**。

Style: 3D miniature isometric perspective (45° top-down), diorama style, frameless
floating world, soft refined textures, PBR materials, gentle natural lighting,
warm cream background with terracotta orange accents and rich charcoal black
labels. ALL LABELS in HAND-LETTERED SANS-SERIF (marker-handwriting feel, Bold
to Semi-bold weight, NO Heavy industrial sans-serif). NO serifs, NEVER 宋体,
NEVER brush calligraphy, NEVER 楷体. NEVER pure red. Avoid photorealism.
```

**默认模型**：`flash`（场景为主，文字少）。

---

## Recipe 3: `timeline`（时间轴 / 演进图）

**何时用**：展示一个技术/产品/概念在时间上的演变。

```
画一张水平时间轴，16:9 横版。主题「{主题}」。
从左到右依次是 {N} 个时间节点（N ∈ 3..6）：
  - {年份 1}：{事件 1}
  - {年份 2}：{事件 2}
  - ...
每个节点用一个手绘小场景表现，节点之间用蜿蜒线条连起来。
顶部写大标题"{标题}"。
**字体强制**：标题和年份标签一律手写感无衬线体（hand-lettered sans-serif）——字型清晰、有手作温度。**不要毛笔字、不要楷体、不要宋体、不要 Heavy 工业死板**。
标题周围配黑色细笔 sketchnote 涂鸦元素。
米白背景纸面纹理，整体暖色调（米白 + 赭橙 + 深炭黑）。

Style: hand-drawn sketchnote-style infographic, 16:9 horizontal timeline, soft
pen strokes for illustration, warm cream background with paper grain, isometric
mini-scenes at each timeline node, flowing connecting lines in terracotta orange.
Main title and year labels in HAND-LETTERED SANS-SERIF (marker-handwriting feel,
Bold to Semi-bold weight, NO Heavy industrial sans-serif). NO serifs, NEVER 宋体,
NEVER brush calligraphy, NEVER 楷体. Title surrounded by black thin-line
sketchnote doodles. Palette: cream + terracotta orange + rich charcoal black +
muted secondary (dusty pink / sage / amber). NEVER pure red. Generous whitespace.
```

**默认模型**：`pro`（年份/节点文字要清晰）。

---

## Recipe 4: `flow-diagram`（流程图 / 架构图）

**何时用**：展示请求 → 处理 → 响应这类有方向的流程，或多层架构。

```
画一张手绘 sketchnote 风流程图，16:9 横版，主题「{流程名}」。
流程从左到右分 {N} 步（N ∈ 3..5），每步是一个圆角卡片：
  - 步骤 1：{动作} —— 配小图标
  - 步骤 2：{动作} —— 配小图标
  - ...
步骤之间用粗手绘箭头连接（赭橙色），箭头旁可有 1–3 个字的说明。
顶部写大标题。
**字体强制**：标题和卡片内文字一律**手写感无衬线体（hand-lettered sans-serif）**——字型清晰、轮廓规整，但笔画有轻微手作不规则，像设计师用粗水笔手写。字重 Bold / Semi-bold。**不要 Heavy 工业死板黑体、不要毛笔字、不要楷体、不要行楷、不要宋体衬线**。
标题周围配 2-4 个黑色细笔 sketchnote 涂鸦元素（星星 / 箭头 / 螺旋）。
米白背景纸面纹理。配色 Anthropic 风：米白底 + 赭橙强调 + 深炭黑文字。

Style: hand-drawn sketchnote-style flow diagram, 16:9 horizontal, soft pen
strokes for illustration, warm cream paper texture background (#F5F0E8 tone,
Anthropic / Claude desktop palette). Title and labels in HAND-LETTERED
SANS-SERIF typography — clean letterforms with slight stroke irregularity,
marker-handwriting feel, Bold to Semi-bold weight (NOT Heavy industrial
sans-serif, NOT stiff machine font). NO SERIFS. ABSOLUTELY NEVER brush
calligraphy, NEVER 毛笔字, NEVER 楷体, NEVER 行楷, NEVER 草书, NEVER 书法,
NEVER 宋体, NEVER serif. Terracotta burnt orange (#CC785C tone) for arrows
and key labels — NEVER pure red. Rich charcoal black (#191919) for primary
text and outlines. Title surrounded by black thin-line sketchnote doodles
(stars, arrows, swirls). Rounded card shapes with thin outlines. Generous
whitespace. Avoid sharp digital geometry, avoid neon colors, avoid dense
small text.
```

**默认模型**：`pro`。

---

## Recipe 5: `hand-drawn-explainer`（概念解释手绘）

**何时用**：一句话讲清楚一个抽象概念。用拟人化或类比的画面。

```
画一张手绘 sketchnote 风解释图，16:9 横版。
用一个生动的类比表现「{抽象概念}」：{类比场景描述，1–2 句}。
画面只有一个主角（人物或拟人化对象），居中，周围留白充足。
主角神态生动，姿势能传达概念的核心动作。
右下方留出区域放一句中文 caption："{一句话 caption}"。
**字体强制**：caption 用手写感无衬线体（hand-lettered sans-serif），字型清晰但带手作温度，颜色赭橙 + 深炭黑。**不要毛笔字、不要书法、不要宋体、不要 Heavy 工业死板**。
caption 旁边可以配 1-2 个黑色细笔 sketchnote 涂鸦（小箭头或强调圈）。

Style: hand-drawn sketchnote illustration, single centered subject, 16:9
horizontal, warm cream background with subtle paper texture, soft pen strokes,
expressive character pose, generous whitespace. Chinese caption in
HAND-LETTERED SANS-SERIF (marker-handwriting feel, Bold to Semi-bold weight,
NO Heavy industrial sans-serif) in terracotta orange + rich charcoal black.
NO serifs, NEVER 宋体, NEVER brush calligraphy, NEVER 楷体. NEVER pure red.
Avoid photorealism, avoid complex backgrounds.
```

**默认模型**：`flash`（人物 + 少量文字，flash 够用）。

---

## 怎么用

1. 从图位的 `gen-hint` 看图类型 → 选对应 recipe。
2. 替换占位符 → 生成完整中文描述。
3. 拼上 `image-style-guide.md` 的通用 style 后缀。
4. 调 `scripts/generate_image.py`。

## 调优技巧

- **文字总是不清晰**：换 `--model pro`。
- **字体死板成工业黑体**：在 prompt 里强调 `slight stroke irregularity, marker-handwriting feel, hand-drawn imperfection, NOT machine font, NOT industrial sans-serif`，把字重往 Semi-bold 拉。
- **中文飘成毛笔字 / 楷体 / 书法**：在 prompt 多个位置强调 `NEVER brush calligraphy, NEVER 楷体, NEVER 行楷, NEVER 书法`。pro 模型对反向提示更敏感。
- **中文飘成宋体 / 衬线体**：在 prompt 多个位置强调 `NO SERIFS, NEVER 宋体, NEVER 仿宋`。
- **颜色变成大红色**：在 prompt 多个位置强调 `terracotta orange / burnt orange (#CC785C tone), NEVER pure red, NEVER saturated red, NEVER crimson`。
- **构图太满**：加 `at least 30% empty space, minimalist composition`。
- **被安全过滤拦**：去掉真实人名/品牌名/可能敏感的主题词。重试前确认换了表述。
