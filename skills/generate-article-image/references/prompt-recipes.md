# Prompt 模板库

5 个常用 prompt 模板。所有模板末尾都要拼上 `baoyu-style.md` 里的通用 style 后缀。

格式约定：`{占位符}` 是要替换的内容，其余保持。

---

## Recipe 1: `infographic-card`（信息图卡片，最通用）

**何时用**：把一段文字内容（定义、对比、清单）视觉化。文章里大多数图位都适合这个。

```
画一张手绘信息卡，9:16 竖版。主题是「{主题中文}」。
卡片底色米白带纸面纹理，标题用毛笔字写"{标题}"放在顶部，标题字红黑配色。
正文区分成 {N} 个并列卡片（N ∈ 2..4），每个卡片：
  - {卡片 1 标题}：{一句话说明}
  - {卡片 2 标题}：{一句话说明}
  - ...
每个卡片左上角配一个手绘小图标，图标和卡片内容对应。
整体留白充足，无装饰性元素。

Style: hand-drawn cartoon illustration with soft brush strokes, warm beige/off-white
background with subtle paper grain texture, accent colors in deep red and black,
generous whitespace, PBR materials with soft natural lighting, brush-stroke
calligraphy for titles. Avoid photorealism, neon colors, dense small text.
```

**默认模型**：`pro`（文字渲染密集，flash 可能糊）。

---

## Recipe 2: `isometric-scene`（等距 3D 微缩场景）

**何时用**：解释一个系统的整体结构、各组件如何在空间上协作。

```
画一个 45° 顶视的等距 3D 微缩卡通场景，9:16 竖版。
场景表现「{系统/概念名}」：
  - 前景：{核心组件}
  - 中景：{支撑组件 1}、{支撑组件 2}
  - 背景：{环境元素}
组件之间用细线或路径连接表示数据/请求流向。
diorama 风格，无外框，世界悬浮在米白背景上。
材质柔和，PBR 质感，自然光照。

Style: 3D miniature isometric perspective (45° top-down), diorama style, frameless
floating world, soft refined textures, PBR materials, gentle natural lighting,
warm color palette, generous whitespace. Avoid photorealism.
```

**默认模型**：`flash`（场景为主，文字少）。

---

## Recipe 3: `timeline`（时间轴 / 演进图）

**何时用**：展示一个技术/产品/概念在时间上的演变。

```
画一张垂直时间轴，9:16 竖版。主题「{主题}」。
从顶到底依次是 {N} 个时间节点（N ∈ 3..6）：
  - {年份 1}：{事件 1}
  - {年份 2}：{事件 2}
  - ...
每个节点用一个手绘小场景表现（不是单纯图标），节点之间用蜿蜒线条连起来。
顶部用毛笔字写大标题"{标题}"。
米白背景纸面纹理，整体暖色调。

Style: hand-drawn cartoon illustration, 9:16 vertical timeline, soft brush strokes,
warm beige background with paper grain, isometric mini-scenes at each timeline node,
flowing connecting lines, brush-stroke calligraphy for main title, generous
whitespace between nodes. Avoid photorealism.
```

**默认模型**：`pro`（年份/节点文字要清晰）。

---

## Recipe 4: `flow-diagram`（流程图 / 架构图）

**何时用**：展示请求 → 处理 → 响应这类有方向的流程，或多层架构。

```
画一张手绘流程图，9:16 竖版，主题「{流程名}」。
流程从上到下分 {N} 步（N ∈ 3..5），每步是一个圆角卡片：
  - 步骤 1：{动作} —— 配小图标
  - 步骤 2：{动作} —— 配小图标
  - ...
步骤之间用粗手绘箭头连接，箭头旁可有 1–3 个字的说明。
顶部毛笔字标题。米白背景纸面纹理。

Style: hand-drawn cartoon flow diagram, 9:16 vertical, soft brush strokes,
beige paper texture background, red+black accent for arrows and labels,
rounded card shapes with thin outlines, brush-stroke title at top,
generous whitespace. Avoid sharp digital geometry.
```

**默认模型**：`pro`。

---

## Recipe 5: `hand-drawn-explainer`（概念解释手绘）

**何时用**：一句话讲清楚一个抽象概念。用拟人化或类比的画面。

```
画一张手绘卡通解释图，9:16 竖版。
用一个生动的类比表现「{抽象概念}」：{类比场景描述，1–2 句}。
画面只有一个主角（人物或拟人化对象），居中，周围留白充足。
主角神态生动，姿势能传达概念的核心动作。
底部留出 1/4 高度放一句中文 caption："{一句话 caption}"。

Style: hand-drawn cartoon illustration, single centered subject, 9:16 vertical,
warm beige background with subtle paper texture, soft brush strokes,
expressive character pose, generous whitespace, hand-painted Chinese caption
at the bottom. Avoid photorealism, avoid complex backgrounds.
```

**默认模型**：`flash`（人物 + 少量文字，flash 够用）。

---

## 怎么用

1. 从图位的 `gen-hint` 看图类型 → 选对应 recipe。
2. 替换占位符 → 生成完整中文描述。
3. 拼上 `baoyu-style.md` 的通用 style 后缀（如果 recipe 自己的 style 段已经覆盖，可省）。
4. 调 `scripts/generate_image.py`。

## 调优技巧

- **文字总是不清晰**：换 `--model pro`。
- **太"AI 味"（光滑塑料感）**：在 prompt 里加 `with visible brush strokes, hand-drawn imperfections, slightly uneven lines`。
- **颜色太亮**：加 `muted earth tones, no saturated colors`。
- **构图太满**：加 `at least 30% empty space, minimalist composition`。
- **被安全过滤拦**：去掉真实人名/品牌名/可能敏感的主题词。重试前确认换了表述。
