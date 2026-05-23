# 图像风格规范

`generate-article-image` skill 用这份规范拼接每条 prompt 的 style 后缀。

## 8 项风格指纹

1. **横版 16:9 为默认。** PC / 大屏单图阅读尺寸最舒适。移动端单图阅读才用 9:16 竖版。
2. **等距 / 微缩 3D 视角** 用于场景类图（45° 顶视，diorama 风格）；流程图 / 对比图保持平面视角。
3. **手绘 / 卡通美学。** 明确避免照片级写实（photorealism）。线条柔和，可见笔触。
4. **Anthropic / Claude desktop 暖色调色。** 米白 / 奶油底（cream/beige，#F5F0E8 风格），赭橙色（terracotta / burnt orange，#CC785C 风格）做主强调，深炭黑（rich charcoal，#191919）做文字与主线条。sketchnote 辅色（dusty pink、sage green、soft amber、slate blue）只用于装饰涂鸦元素，**不抢主标题**。避开大红、霓虹色、高饱和数字色、纯黑底。
5. **充足留白。** 关键信息只占画面 50–70%，剩余给空气感。
6. **PBR 材质 + 纸面纹理。** 即使是卡通，材质要做出真实物理感（subtle paper grain、soft fabric、wood）。
7. **强制字体规格：粗黑体（heavy sans-serif）+ sketchnote 涂鸦装饰。**
   - 标题字体：**粗黑体**（heavy sans-serif / sans-serif at Heavy or Black weight），笔画粗细**均匀**，**方头方尾**，**没有衬线**（NO serif），结构端正、字怀紧凑。
   - 中文等价为：**思源黑体 Heavy（Source Han Sans Heavy / Noto Sans CJK Black）**、**PingFang SC Heavy / 苹方粗**、**阿里巴巴普惠体 Heavy**、**HarmonyOS Sans Black**。中文笔画粗壮、字形方正。
   - 英文同款字体家族的 Heavy / Black weight（如 Inter Black、Helvetica Black、Source Sans 3 Black）。
   - **明确避开**：宋体（serif）/ 仿宋 / 楷体 / 行楷 / 毛笔锋 / 书法字体 / 中文 ink-brush。这些都不要。
   - 装饰：标题周围可以有 sketchnote 风格的**黑色细笔涂鸦元素**——星星（stars）、箭头（arrows）、螺旋（swirls）、强调圈（emphasis circles）。
   - 参考样图：用户截图的"图增强 RAG 链路"标题样式（赭橙 + 黑色粗黑体混排）；附 [`style-references/sketch-notes.webp`](./style-references/sketch-notes.webp) 仅作 sketchnote 装饰元素的参考，**字体不取它的英文衬线**。
8. **信息图导向。** 把文字内容视觉化（卡片化、时间轴化、流程化），不是给文章配情绪图。

## 通用英文 style 后缀（拼到所有 prompt 末尾）

```
Style: hand-drawn sketchnote-style infographic on warm cream/beige paper
texture (#F5F0E8 tone). Title and key labels rendered in HEAVY SANS-SERIF
typography — uniform stroke weight, squared terminals, NO SERIFS, structured
glyph shapes, compact counters. Chinese equivalent: Source Han Sans Heavy
(思源黑体 Heavy) / PingFang SC Heavy (苹方粗) / Alibaba PuHuiTi Heavy /
HarmonyOS Sans Black. English equivalent: Inter Black / Helvetica Black /
Source Sans 3 Black. ABSOLUTELY NEVER serif fonts, NEVER 宋体, NEVER 仿宋,
NEVER brush calligraphy, NEVER 楷体 / 行楷 / 草书 / 书法 / Chinese ink-brush.
Primary accent in terracotta burnt orange (#CC785C tone, Anthropic / Claude
desktop palette), primary text and outlines in rich charcoal black (#191919).
Title surrounded by tasteful sketchnote doodle elements (black thin-line
stars, arrows, swirls, emphasis circles). Secondary palette for decorative
doodles: dusty pink, sage green, soft amber, slate blue — muted, never neon,
never pure red. Generous whitespace. Soft pen strokes for illustration, PBR
materials, gentle natural lighting. Avoid photorealism, avoid harsh shadows.
```

每个 recipe 在这个后缀基础上加 1–2 行专属修饰。最关键的三条**不要去掉**：
- `HEAVY SANS-SERIF typography ... NO SERIFS ... NEVER 宋体 / 毛笔字 / 楷体`
- `terracotta burnt orange ... NEVER pure red`
- 中文字体名锚定：`Source Han Sans Heavy / 思源黑体 Heavy / 苹方粗`

去掉以后模型容易回到默认的宋体衬线、毛笔字或大红。

## 5 个示例 prompt（按图类型，演示描述粒度）

### 示例 1：等距 3D 城市/系统场景

```
Present a clear, 45° top-down view of a horizontal (16:9) isometric miniature 3D cartoon scene,
highlighting iconic landmarks centered in the composition to showcase precise and delicate modeling.
The scene features soft, refined textures with realistic PBR materials and gentle, lifelike
lighting and shadow effects. Title in HEAVY SANS-SERIF (Source Han Sans Heavy / 思源黑体 Heavy
for Chinese, Inter Black for English) — uniform strokes, no serifs. Palette: cream background,
terracotta orange accents, rich charcoal black for outlines.
```

### 示例 2：儿童蜡笔风格

```
A vibrant, child-like crayon-style horizontal (16:9) journal illustration for a {topic},
winding route with key items, cute doodles, recognizable landmarks, foods, playful
handwritten notes. Drawn as if by a curious child using colorful crayons, soft warm pale
yellow background, muted earth tones (terracotta, ochre, sage), charcoal black accents.
Headings in heavy sans-serif (NOT serif, NOT brush calligraphy, NOT 宋体). Avoid pure red.
```

### 示例 3：内容转信息图

```
Hand-drawn sketchnote infographic, landscape 16:9, on warm cream paper texture.
Simplify information, emphasize keywords and core concepts, ample whitespace for clarity.
Minimalistic hand-drawn icons (avoid realistic visual elements).
All headlines in HEAVY SANS-SERIF (Source Han Sans Heavy / 思源黑体 Heavy for Chinese).
NO serifs, NO 宋体, NO brush calligraphy.
Title surrounded by black thin-line sketchnote doodles (stars, arrows, swirls).
Palette: warm cream background, terracotta orange primary accent, rich charcoal black text,
dusty pink / sage green / soft amber for secondary doodles.
```

### 示例 4：手绘信息卡（最常用）

```
Hand-drawn sketchnote-style infographic card, 16:9 horizontal. Warm cream/beige background
with subtle paper texture. Large HEAVY SANS-SERIF title (terracotta orange + charcoal black
contrast) — uniform strokes, squared terminals, no serifs. Chinese rendered as Source Han Sans
Heavy / 思源黑体 Heavy / 苹方粗 (NOT 宋体, NOT 楷体, NOT brush calligraphy). Layout: 2–4
clearly defined sections arranged left-to-right. Title surrounded by black thin-line sketchnote
doodle elements. Avoid pure red, avoid neon colors.
```

### 示例 5：演进时间轴

```
Frameless isometric world telling an entire evolution along a horizontal (16:9) timeline,
humble starting state on the left → futuristic peak on the right. Soft textures, PBR materials,
gentle lighting. Year labels in HEAVY SANS-SERIF (Source Han Sans Heavy for Chinese); section
titles in same family. NO serifs. Palette: cream + terracotta orange + rich charcoal black.
Sketchnote doodles between nodes.
```

## 反指纹（生成时尽量避开）

- 照片级写实人脸。
- 大红、霓虹、高饱和数字色。
- 满图无留白。
- 平面 vector flat icon 风（违反 #3 手绘感）。
- 黑色背景 / 赛博朋克。
- **任何衬线体（serif）/ 中文宋体 / 仿宋** —— 违反 #7 字体强制规格。
- **毛笔书法字体 / 中文 ink-brush calligraphy / 楷体 / 行楷 / 草书** —— Gemini 在中文上最容易飘的方向，需要在 prompt 多处反复约束。
- **细体 / Light / Regular weight** —— sketch-notes 要的是 Heavy / Black 这种最粗的字重。
- 多个标题字体混用 —— 一张图里只允许一个标题字体家族。
