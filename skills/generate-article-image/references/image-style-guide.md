# 图像风格规范

`generate-article-image` skill 用这份规范拼接每条 prompt 的 style 后缀。

## 8 项风格指纹

1. **竖版 9:16 为默认。** 移动端单图阅读尺寸最舒适。文章封面图才用 16:9 横版。
2. **等距 / 微缩 3D 视角。** 45° 顶视，diorama 风格，无边框的小世界悬浮在背景上。
3. **手绘 / 卡通美学。** 明确避免照片级写实（photorealism）。线条柔和，可见笔触。
4. **暖色有机调色。** 米色 / 米白底，红黑做对比强调色。整体温暖、手作感。**禁止**霓虹色、高饱和数字色、纯黑底。
5. **充足留白。** 关键信息只占画面 50–70%，剩余给空气感。
6. **PBR 材质 + 纸面纹理。** 即使是卡通，材质要做出真实物理感（subtle paper grain、soft fabric、wood）。
7. **毛笔 / 手写体大标题。** 标题用 brush-stroke calligraphy 风，红黑对比强突出主题。
8. **信息图导向。** 把文字内容视觉化（卡片化、时间轴化、流程化），不是给文章配情绪图。

## 通用英文 style 后缀（拼到所有 prompt 末尾）

```
Style: hand-drawn cartoon illustration with soft brush strokes, warm beige/off-white background
with subtle paper grain texture, accent colors in deep red and black, generous whitespace,
3D miniature isometric perspective when applicable (45° top-down view), PBR materials with
soft natural lighting, brush-stroke calligraphy for titles. Avoid photorealism, avoid harsh
shadows, avoid neon or saturated digital colors.
```

每个 recipe 可以在这个后缀基础上加 1–2 行专属修饰，但不要去掉这段基础。

## 5 个示例 prompt（按图类型，演示描述粒度）

这些示例的核心价值是**描述粒度**：永远精确到视角、材质、配色、构图，从不说"做一张好看的图"。

### 示例 1：等距 3D 城市/系统场景

```
Present a clear, 45° top-down view of a vertical (9:16) isometric miniature 3D cartoon scene,
highlighting iconic landmarks centered in the composition to showcase precise and delicate modeling.
The scene features soft, refined textures with realistic PBR materials and gentle, lifelike
lighting and shadow effects. Weather or thematic elements are creatively integrated into the
architecture, establishing a dynamic interaction between landscape and atmosphere.
```

### 示例 2：儿童蜡笔风格

```
A vibrant, child-like crayon-style vertical (9:16) journal illustration for a {topic},
winding route with key items, cute doodles, recognizable landmarks, foods, playful
handwritten notes. Drawn as if by a curious child using colorful crayons, soft warm pale
yellow background, bright reds, blues, greens.
```

### 示例 3：内容转信息图

```
Cartoon-style infographic, hand-drawn illustration style, landscape 16:9.
Simplify information, emphasize keywords and core concepts, ample whitespace for clarity.
Minimalistic cartoon characters or icons (avoid realistic visual elements).
```

### 示例 4：手绘信息卡（最常用）

```
Hand-drawn style infographic card, 9:16 vertical. Warm, organic look, beige/off-white
background with subtle paper texture. Large brush-stroke lettering for title (red + black
contrast). All text in flowing hand-painted script. Layout: 2–4 clearly defined sections.
```

### 示例 5：演进时间轴

```
Frameless isometric world telling an entire evolution in one vertical timeline,
humble starting state → futuristic peak. Soft textures, PBR materials, gentle lighting.
```

## 反指纹（不要做）

- 照片级写实人脸（容易过滤，也违反 #3 手绘感）。
- 高饱和霓虹色（违反 #4 暖色有机调）。
- 满图无留白（违反 #5）。
- 平面 vector flat icon 风（违反 #3 手绘感和 #6 材质感）。
- 黑色背景 / 赛博朋克（完全跑偏）。
