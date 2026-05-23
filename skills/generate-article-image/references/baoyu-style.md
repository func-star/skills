# 宝玉风格指纹

`generate-article-image` skill 用这份指纹拼接每条 prompt 的 style 后缀。**所有研究来源都是宝玉本人在 X 上公开过的 prompt**——这不是凭感觉的总结。

## 8 项指纹

1. **竖版 9:16 为默认。** 宝玉绝大多数图都是 X 移动端阅读尺寸。文章封面图才用 16:9。
2. **等距 / 微缩 3D 视角。** 45° 顶视，diorama 风格，无边框小世界。
3. **手绘 / 卡通美学。** 明确避免照片级写实（photorealism）。线条柔和，可见笔触。
4. **暖色有机调色。** 米色 / 米白底，红黑做对比强调色，整体偏温暖、手作感。
5. **充足留白。** 每张图里关键信息只占 50–70% 面积，剩余给空气感。
6. **PBR 材质 + 纸面纹理。** 即使是卡通，材质做出真实物理感（subtle paper grain、soft fabric、wood）。
7. **毛笔 / 手写体大标题。** 标题用 brush-stroke calligraphy 风，做强烈对比突出主题。
8. **信息图传统。** 把文字内容视觉化（卡片化、时间轴化），不是装饰图。

## 通用英文 style 后缀（拼到所有 prompt 末尾）

```
Style: hand-drawn cartoon illustration with soft brush strokes, warm beige/off-white background
with subtle paper grain texture, accent colors in deep red and black, generous whitespace,
3D miniature isometric perspective when applicable (45° top-down view), PBR materials with
soft natural lighting, brush-stroke calligraphy for titles. Avoid photorealism, avoid harsh
shadows, avoid neon or saturated digital colors.
```

每个 recipe 可以在这个后缀基础上加 1–2 行专属修饰，但不要去掉这段基础。

## 5 个宝玉 prompt 实例（带 X 原帖）

读这些理解他的描述粒度——他从不说"做一张好看的图"，永远精确到视角、材质、配色、构图。

### 1. 天气卡片
[x.com/dotey/status/1993729800922341810](https://x.com/dotey/status/1993729800922341810)

> Present a clear, 45° top-down view of a vertical (9:16) isometric miniature 3D cartoon scene,
> highlighting iconic landmarks centered in the composition to showcase precise and delicate modeling.
> The scene features soft, refined textures with realistic PBR materials and gentle, lifelike lighting
> and shadow effects. Weather elements are creatively integrated into the urban architecture,
> establishing a dynamic interaction between the city's landscape and atmospheric conditions.

### 2. 儿童蜡笔旅行手账
[x.com/dotey/status/1994908289813880915](https://x.com/dotey/status/1994908289813880915)

> A vibrant, child-like crayon-style vertical (9:16) travel-journal illustration for a {City} trip,
> winding route with daily attractions, cute doodles, local landmarks, foods, playful handwritten notes.
> Drawn as if by a curious child using colorful crayons, soft warm pale yellow background,
> bright reds, blues, greens.

### 3. 文章转信息图
[x.com/dotey/status/1993567848564686926](https://x.com/dotey/status/1993567848564686926)

> Cartoon-style infographic, hand-drawn illustration style, landscape 16:9.
> Simplify information, emphasize keywords and core concepts, ample whitespace for clarity.
> Minimalistic cartoon characters or icons (avoid realistic visual elements).

### 4. 手绘信息卡（最常用）
[x.com/dotey/status/1996303762428731486](https://x.com/dotey/status/1996303762428731486)

> Hand-drawn style infographic card, 9:16 vertical. Warm, organic look, beige/off-white background
> with subtle paper texture. Large brush-stroke lettering for title (red + black contrast).
> All text in flowing hand-painted script. Layout: 2–4 clearly defined sections.

### 5. 公司演进时间轴
[x.com/dotey/status/1999262265066029156](https://x.com/dotey/status/1999262265066029156)

> Frameless isometric world telling an entire company's evolution in one vertical timeline,
> humble garage → futuristic peak. Soft textures, PBR materials, gentle lighting.

## 反指纹（不要做）

- 照片级写实人脸（容易过滤，且不像宝玉风）。
- 高饱和霓虹色（违反 #4 暖色有机调）。
- 满图无留白（违反 #5）。
- 平面 vector flat icon 风（违反 #3 手绘感和 #6 材质感）。
- 黑色背景 / 赛博朋克（完全跑偏）。
