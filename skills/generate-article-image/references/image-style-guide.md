# 图像风格规范

`generate-article-image` skill 用这份规范拼接每条 prompt 的 style 后缀。

## 8 项风格指纹

1. **横版 16:9 为默认。** PC / 大屏单图阅读尺寸最舒适。移动端单图阅读才用 9:16 竖版。
2. **等距 / 微缩 3D 视角** 用于场景类图（45° 顶视，diorama 风格）；流程图 / 对比图保持平面视角。
3. **手绘 / 卡通美学。** 明确避免照片级写实（photorealism）。线条柔和，可见笔触。
4. **Anthropic / Claude desktop 暖色调色。** 米白 / 奶油底（cream/beige，#F5F0E8 风格），赭橙色（terracotta / burnt orange，#CC785C 风格）做主强调，深炭黑（rich charcoal，#191919）做文字与主线条。sketchnote 辅色（dusty pink、sage green、soft amber、slate blue）只用于装饰涂鸦元素，**不抢主标题**。避开大红、霓虹色、高饱和数字色、纯黑底。
5. **充足留白。** 关键信息只占画面 50–70%，剩余给空气感。
6. **PBR 材质 + 纸面纹理。** 即使是卡通，材质要做出真实物理感（subtle paper grain、soft fabric、wood）。
7. **强制字体规格：手写感无衬线体（hand-lettered sans-serif）+ sketchnote 涂鸦装饰。**
   - 标题字体：**手写感无衬线体**（hand-lettered sans-serif）——字型清晰、轮廓规整，但笔画**有轻微手作不规则**（slight stroke irregularity），像设计师用粗水笔（chisel-tip marker）手写信息图标题的感觉。**无衬线（no serifs）**，字重在 Bold / Semi-bold 一档（不要 Heavy 那种工业死板感）。
   - 中文呈现：参考"思源黑体 Bold + 手作不规则"的视觉特征——字形端正、笔画粗细基本均匀但末端略有手作起伏；**不要**完全机械的黑体（avoid stiff industrial sans-serif），**不要**毛笔锋、不要楷体、不要行楷、不要书法。
   - 英文呈现：参考 Caveat Brush / Patrick Hand / Architects Daughter 这类 hand-lettered 字体的氛围。
   - 装饰：标题周围可以有 sketchnote 风格的**黑色细笔涂鸦元素**——星星（stars）、箭头（arrows）、螺旋（swirls）、强调圈（emphasis circles）。
   - 配色：标题用赭橙色 + 深炭黑做混排（不是统一颜色）。
8. **信息图导向。** 把文字内容视觉化（卡片化、时间轴化、流程化），不是给文章配情绪图。

## 通用英文 style 后缀（拼到所有 prompt 末尾）

```
Style: hand-drawn sketchnote-style infographic on warm cream/beige paper
texture (#F5F0E8 tone). Title and key labels rendered in HAND-LETTERED
SANS-SERIF typography — clean letterforms with slight stroke irregularity,
like a designer hand-writing infographic titles with a chisel-tip marker.
Bold to semi-bold weight, NOT heavy industrial sans-serif, NOT stiff machine
font. NO SERIFS. For Chinese: structured glyph shapes with subtle hand-drawn
imperfection (think Source Han Sans Bold with hand-painted variation),
ABSOLUTELY NEVER brush calligraphy, NEVER 毛笔字, NEVER 楷体, NEVER 行楷,
NEVER 草书, NEVER 书法, NEVER Chinese ink-brush, NEVER 宋体, NEVER serif
fonts. Primary accent in terracotta burnt orange (#CC785C tone, Anthropic /
Claude desktop palette), primary text and outlines in rich charcoal black
(#191919). Title surrounded by tasteful sketchnote doodle elements (black
thin-line stars, arrows, swirls, emphasis circles). Secondary palette for
decorative doodles: dusty pink, sage green, soft amber, slate blue — muted,
never neon, never pure red. Generous whitespace. Soft pen strokes for
illustration, PBR materials, gentle natural lighting. Avoid photorealism,
avoid harsh shadows.
```

每个 recipe 在这个后缀基础上加 1–2 行专属修饰。最关键的三条**不要去掉**：
- `HAND-LETTERED SANS-SERIF ... clean letterforms with slight stroke irregularity ... NOT heavy industrial sans-serif ... NO SERIFS`
- 反向围栏：`NEVER brush calligraphy, NEVER 楷体, NEVER 行楷, NEVER 书法, NEVER 宋体, NEVER serif`
- `terracotta burnt orange ... NEVER pure red`

去掉以后模型容易回到默认的毛笔字 / 楷体 / 大红，或者反过来跑到 Heavy 工业感死板。

## 5 个示例 prompt（按图类型，演示描述粒度）

### 示例 1：等距 3D 城市/系统场景

```
Present a clear, 45° top-down view of a horizontal (16:9) isometric miniature 3D cartoon scene,
highlighting iconic landmarks centered in the composition to showcase precise and delicate modeling.
The scene features soft, refined textures with realistic PBR materials and gentle, lifelike
lighting and shadow effects. Title in HAND-LETTERED SANS-SERIF — clean letterforms with slight
hand-drawn irregularity, like marker handwriting, NOT heavy industrial sans-serif, NOT brush
calligraphy. Palette: cream background, terracotta orange accents, rich charcoal black for outlines.
```

### 示例 2：儿童蜡笔风格

```
A vibrant, child-like crayon-style horizontal (16:9) journal illustration for a {topic},
winding route with key items, cute doodles, recognizable landmarks, foods, playful
handwritten notes. Drawn as if by a curious child using colorful crayons, soft warm pale
yellow background, muted earth tones (terracotta, ochre, sage), charcoal black accents.
Headings in hand-lettered sans-serif (NOT serif, NOT brush calligraphy, NOT 宋体). Avoid pure red.
```

### 示例 3：内容转信息图

```
Hand-drawn sketchnote infographic, landscape 16:9, on warm cream paper texture.
Simplify information, emphasize keywords and core concepts, ample whitespace for clarity.
Minimalistic hand-drawn icons (avoid realistic visual elements).
All headlines in HAND-LETTERED SANS-SERIF — clean letterforms with slight irregularity,
marker-handwriting feel, NO serifs, NO brush calligraphy, NO 楷体.
Title surrounded by black thin-line sketchnote doodles (stars, arrows, swirls).
Palette: warm cream background, terracotta orange primary accent, rich charcoal black text,
dusty pink / sage green / soft amber for secondary doodles.
```

### 示例 4：手绘信息卡（最常用）

```
Hand-drawn sketchnote-style infographic card, 16:9 horizontal. Warm cream/beige background
with subtle paper texture. Large HAND-LETTERED SANS-SERIF title (terracotta orange + charcoal
black contrast) — clean letterforms with subtle hand-drawn variation, NOT heavy industrial
sans-serif, NOT stiff machine font, NO SERIFS, NOT brush calligraphy, NOT 楷体. Layout: 2–4
clearly defined sections arranged left-to-right. Title surrounded by black thin-line sketchnote
doodle elements. Avoid pure red, avoid neon colors.
```

### 示例 5：演进时间轴

```
Frameless isometric world telling an entire evolution along a horizontal (16:9) timeline,
humble starting state on the left → futuristic peak on the right. Soft textures, PBR materials,
gentle lighting. Year labels in HAND-LETTERED SANS-SERIF; section titles in same family.
Marker-handwriting feel with slight irregularity, NO serifs, NO 宋体, NO brush calligraphy.
Palette: cream + terracotta orange + rich charcoal black. Sketchnote doodles between nodes.
```

## 反指纹（生成时尽量避开）

- 照片级写实人脸。
- 大红、霓虹、高饱和数字色。
- 满图无留白。
- 平面 vector flat icon 风（违反 #3 手绘感）。
- 黑色背景 / 赛博朋克。
- **毛笔书法字体 / 中文 ink-brush calligraphy / 楷体 / 行楷 / 草书** —— Gemini 在中文上最容易飘的方向。
- **任何衬线体 / 中文宋体 / 仿宋** —— 违反 #7 sans-serif 要求。
- **Heavy / Black weight 的工业感死板黑体** —— 字重太重会失去手作温度，sketchnote 风要的是 Bold/Semi-bold + 手作不规则。
- 多个标题字体混用 —— 一张图里只允许一个标题字体家族。
