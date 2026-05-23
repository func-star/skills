# Prompt 模板库

5 个常用 prompt 模板。所有模板末尾都要拼上 `image-style-guide.md` 里的通用 style 后缀。

格式约定：`{占位符}` 是要替换的内容，其余保持。

**默认画幅**：16:9 横版（PC 单图阅读友好）。移动端场景才用 9:16 竖版。

---

## Recipe 1: `infographic-card`（信息图卡片，最通用）

**何时用**：把一段文字内容（定义、对比、清单）视觉化。文章里大多数图位都适合这个。

```
画一张手绘信息卡，16:9 横版。主题是「{主题中文}」。
卡片底色米白带纸面纹理，标题用手写感无衬线体写"{标题}"放在顶部正中，红黑配色。
正文区分成 {N} 个并列卡片（N ∈ 2..4），左右横向排列：
  - {卡片 1 标题}：{一句话说明}
  - {卡片 2 标题}：{一句话说明}
  - ...
每个卡片左上角配一个手绘小图标，图标和卡片内容对应。
所有文字使用手写感无衬线体（hand-lettered sans-serif），不要毛笔字。
整体留白充足，无装饰性元素。

Style: hand-drawn cartoon illustration with soft pen strokes, warm beige/off-white
background with subtle paper grain texture, accent colors in deep red and black,
generous whitespace, PBR materials with soft natural lighting, hand-lettered
sans-serif typography for titles and labels (clean letterforms, slight stroke
irregularity, NO brush calligraphy, NO Chinese ink-brush style). Avoid photorealism,
neon colors, dense small text.
```

**默认模型**：`pro`（文字渲染密集，flash 可能糊）。

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
标签文字使用手写感无衬线体（hand-lettered sans-serif），不要毛笔字。

Style: 3D miniature isometric perspective (45° top-down), diorama style, frameless
floating world, soft refined textures, PBR materials, gentle natural lighting,
warm color palette, generous whitespace, hand-lettered sans-serif for any labels
(NO brush calligraphy). Avoid photorealism.
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
每个节点用一个手绘小场景表现（不是单纯图标），节点之间用蜿蜒线条连起来。
顶部用手写感无衬线体写大标题"{标题}"，不要毛笔字。
米白背景纸面纹理，整体暖色调。

Style: hand-drawn cartoon illustration, 16:9 horizontal timeline, soft pen strokes,
warm beige background with paper grain, isometric mini-scenes at each timeline node,
flowing connecting lines, hand-lettered sans-serif for main title and year labels
(clean letterforms, slight irregularity, NO brush calligraphy), generous whitespace
between nodes. Avoid photorealism.
```

**默认模型**：`pro`（年份/节点文字要清晰）。

---

## Recipe 4: `flow-diagram`（流程图 / 架构图）

**何时用**：展示请求 → 处理 → 响应这类有方向的流程，或多层架构。

```
画一张手绘流程图，16:9 横版，主题「{流程名}」。
流程从左到右分 {N} 步（N ∈ 3..5），每步是一个圆角卡片：
  - 步骤 1：{动作} —— 配小图标
  - 步骤 2：{动作} —— 配小图标
  - ...
步骤之间用粗手绘箭头连接，箭头旁可有 1–3 个字的说明。
顶部用手写感无衬线体写标题，不要毛笔字。米白背景纸面纹理。

Style: hand-drawn cartoon flow diagram, 16:9 horizontal, soft pen strokes,
beige paper texture background, red+black accent for arrows and labels,
rounded card shapes with thin outlines, hand-lettered sans-serif title at top
(clean letterforms, slight irregularity, NO brush calligraphy, NO Chinese
ink-brush style), generous whitespace. Avoid sharp digital geometry.
```

**默认模型**：`pro`。

---

## Recipe 5: `hand-drawn-explainer`（概念解释手绘）

**何时用**：一句话讲清楚一个抽象概念。用拟人化或类比的画面。

```
画一张手绘卡通解释图，16:9 横版。
用一个生动的类比表现「{抽象概念}」：{类比场景描述，1–2 句}。
画面只有一个主角（人物或拟人化对象），居中，周围留白充足。
主角神态生动，姿势能传达概念的核心动作。
右下方留出区域放一句中文 caption："{一句话 caption}"，用手写感无衬线体，不要毛笔字。

Style: hand-drawn cartoon illustration, single centered subject, 16:9 horizontal,
warm beige background with subtle paper texture, soft pen strokes,
expressive character pose, generous whitespace, hand-lettered sans-serif Chinese
caption (clean letterforms, NO brush calligraphy). Avoid photorealism, avoid
complex backgrounds.
```

**默认模型**：`flash`（人物 + 少量文字，flash 够用）。

---

## 怎么用

1. 从图位的 `gen-hint` 看图类型 → 选对应 recipe。
2. 替换占位符 → 生成完整中文描述。
3. 拼上 `image-style-guide.md` 的通用 style 后缀（如果 recipe 自己的 style 段已经覆盖，可省）。
4. 调 `scripts/generate_image.py`。

## 调优技巧

- **文字总是不清晰**：换 `--model pro`。
- **太"AI 味"（光滑塑料感）**：在 prompt 里加 `with visible pen strokes, hand-drawn imperfections, slightly uneven lines`。
- **颜色太亮**：加 `muted earth tones, no saturated colors`。
- **构图太满**：加 `at least 30% empty space, minimalist composition`。
- **模型仍然画出毛笔字**：在 prompt 多个位置（标题描述、style 段、负面提示）都强调 `hand-lettered sans-serif, NOT brush calligraphy`。pro 模型对反向提示更敏感。
- **被安全过滤拦**：去掉真实人名/品牌名/可能敏感的主题词。重试前确认换了表述。
