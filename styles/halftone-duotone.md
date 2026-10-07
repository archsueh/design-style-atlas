---
id: halftone-duotone
name_zh: 半调双色
name_en: Halftone Duotone
lineage: "AM（幅度调制）加网：用大小变化的规则网点模拟连续调，是印刷业最常用的加网方式，网点分辨率以 lpi 计，网角自 9 点钟方向顺时针量度（来源见 §7 [1]）。本条目描述的是当代数字设计对这一印刷工艺的再采用，不是加网史条目；加网史的年代与专利归属本轮未核实，故不写。"
status: draft
nearest: [collage, riso, color-halftone]   # collage 是本库条目；riso、color-halftone 不是（本库暂无），仅作最近邻参照
overlays: []
exception: false
---

# 半调双色（halftone-duotone）

> 由用户 2026-09-30 提供的样张（1881×836，ObsidianUI 字标）倒推。**本条目全部数值来自对该样张的像素测量**，测量方法与原始读数见 §7 [2]。
> 激活：仅 `style: halftone-duotone`。
> ⚠️ 样张是 JPEG：色相可信，**具体 hex 与网角不可照抄**，见 §4、§3。

## §1 判据

- HD-1 图像是否只由**一个色相**承载？全图色相应集中在 ±5° 以内（样张实测：94.1% 的像素落在 H=240±3°）。
- HD-2 中间调是否**全部由网点尺寸产生**，而不是由渐变、羽化或第二块色版产生？放大到 3 倍以上应能看到孤立的规则圆点。
- HD-3 网点是否为**规则栅格上的圆点**（AM 加网，点的大小随明度变化），而不是随机颗粒（FM／随机加网），也不是叠上去的图案纹理？
- HD-4 主体图像是否为**公有领域的具象古典绘画或雕塑**（文艺复兴、巴洛克、学院派皆可，**不限文艺复兴**），且**加网后轮廓仍可辨认**（不是抽象色块，也不是当代摄影）？
- HD-5 标题是否为**单一现代无衬线字族**、白色、落在画面中心附近，且**直接压在图像上**（不加底板、描边、投影）？

## §2 反模式

- HD-AP-1 给连续调照片叠一层半透明蓝色（multiply 或色相叠加）冒充：放大后看不到网点，中间调是平滑渐变。结果是「一张蓝色照片」，不是半调。
- HD-AP-2 网点尺寸失控：粗到在正常观看距离能数清单点，图像退化成马赛克；或细到在目标输出尺寸下完全看不见，白做了一层加网。
- HD-AP-3 为了让标题可读而给文字加描边、外发光、投影或半透明底板。本风格靠**网点密度**本身提供对比（文字落在网点稀疏处），加任何一层都会掉进通用 UI 卡片的语汇。
- HD-AP-4 引入第二个色相（高光调成暖白，或再加一个强调色）。单色相一破，立刻退化为普通的双色调海报（见 §8）。
- HD-AP-5 把网点当**叠加纹理**盖在无关内容上：网点不随明度变化、也不与被加网图像对齐。正确做法是先加网、再上色，网点是图像本身的一部分。

## §3 排版机制

**结构从哪来：**

1. **加网是唯一的明度机制。** 不是「图像 + 蓝色滤镜」，而是把连续调图像先转成加网位图（网点的大小编码明度），再用单油墨平涂。所有明度信息都在网点里 [1]。
2. **网点频率是唯一需要按输出尺寸调的参数。** 网点周期与观看距离共同决定画面读起来「像照片」还是「像印刷品」。样张在 1881px 宽上网点周期约 2px，**已接近该文件的奈奎斯特极限**——实测三处区域的主频方向为 45°／89°／1°，互不一致，**网角不可靠测量**。因此：**不要照抄频率或网角**，按目标宽度重算，让网点在 100% 缩放下刚好可见。
3. **文字层级靠网点密度而非底板。** 标题落在网点稀疏（亮）的区域，用留白换可读性。这是本风格与「图片 + 卡片 + 文字」的分界，也是 §2 HD-AP-3 的由来。
4. **构图是「图像铺满 + 单一居中文字」。** 没有栏、没有网格、没有第二个信息块。图像占满画幅（样张为 2.25:1 横幅），文字是唯一的结构元素。
5. **题材是变量，不是定义。** 本风格只固定两件事：**加网机制**（AM 圆点）与**色域**（单油墨 + 纸白）。画什么由请求方给——古典绘画、雕塑、浮世绘、科学插图、天文照片都能承载同一机制，只要它是公有领域、具象、且明暗层次足够被网点编码。**不要把题材写进风格名或 id**：一旦写成「半调 + 文艺复兴」，则「半调 + 浮世绘」「半调 + 版画」会各自变成一个条目——同一机制、N 个条目。题材走请求参数（见 §6 `positive.style` 只描述机制、主体由用户给）。

**在哪里允许打破：**

- 文字可以压到网点密集区，但必须靠**字重加粗 + 字号放大**补偿，不能靠加底板。
- 图像可以被裁切、可以出血；文字不可以被图像遮挡，也不可以贴边。
- 允许只有图像没有文字（纯图版本）；不允许只有文字而没有加网。

## §4 色彩

- **关系**：不属于互补、邻近、三角等**多色关系**，而是**单色相 + 纸白的两值结构**。所有中间调由网点密度生成，因此不构成色相关系。按印前口径这是**一个油墨**（monotone）；「duotone」是 Photoshop 的通用叫法（duotone 模式包含 monotone 特例），本条目沿用通用叫法，但按前者理解。
- **明度结构**：三段 —— ① 油墨满涂（实底）② 纸白（无墨）③ 中间调（网点部分覆盖）。样张实测：实底 V=0.85 为众数（约占 46%），高光 V≈1.00 为次峰，两者之间是连续分布的中间调。
- **色相**：样张为 H=240°、S=0.87、V=0.85。**色相是全图最稳的量**（94.1% 像素落在 240±3°）；S/V 会被 JPEG 色度二次采样拉偏，**不要把样张的 hex 当作印刷色**。
- ⚠️ **不要把 JPEG 振铃的暗像素当成第二个油墨。** 样张最暗像素 `#000088` 只占 1.47% 且集中在网点边缘，是压缩伪影。判断方法：看 V<0.7 的**像素占比与众数**，不看最小值；众数若只比实底暗一档（样张为 `#100fb2`），即为伪影。
- **屏幕**：示例油墨色 `#1c1cd8`（示例），示例纸色 `#f6f9ff`（示例）。仅作预览，不代表任何品牌或潘通色。
- **印刷时的处理方式**（接口见 `color/pantone-print-system.md` §2.6）：

```yaml
print_handling:
  process: spot                   # 单油墨专色；四色近似会丢掉单色相的纯度
  spot_roles: [flat-large-area]
  substrate: either
  suffix_rule: "编号必须带后缀；C 与 U 分别打样"
  proof: required
  screen_examples: "#1c1cd8、#f6f9ff 为示例，仅作屏幕预览"
  pantone_refs: none
  risks:
    - "单油墨大面积平涂时，网点扩大（dot gain）会把中间调整体压暗，必须打样确认高光未被糊死"
    - "网点频率必须按最终印刷线数重算；照搬屏幕上的像素周期会与印版网屏产生莫尔纹"
```

## §5 字体

中文按 `typography/cn-type-classes.md` 三型：

| 型 | 用法 | 理由 | 代表字体与授权（沿用 cn-type-classes §4.2） |
|---|---|---|---|
| 粗黑无衬线 | 标题的唯一用途 | 只有粗字重能在网点背景上保住笔画 | 思源黑体 Bold / Heavy（开源 OFL 1.1） |
| 复古旧字体 | 不适用 | 细横画在网点背景上会碎 | — |
| 新中式 | 不适用 | 同上，且与西文几何无衬线不同源 | — |

英文：

- 标题用一个 Neo-grotesque（分类词沿用 `cn-type-classes.md` §5 的口径）。样张可见特征：**i / j 的点是正圆**，O 接近正圆，字距偏紧 —— 这是当代几何化 grotesque 的常见特征，不是 1950 年代 Helvetica 系的方点。
- 开源候选：Inter（开源 OFL [3]）、Archivo（开源 OFL [4]）。两者都是当代字体，不是史实字体。
- 商业候选（Helvetica Now / Neue Haas Grotesk / Aeonik 等）：**授权未核**，本条目不推荐。
- 本风格通常没有正文。若必须加，用小字号同族常规字重，且必须落在网点稀疏区。

## §6 提示词出口

```yaml
prompt_export:
  positive:
    style: ["single-ink halftone screen", "round-dot AM halftone on one flat spot colour", "classical painting screened to one ink"]
    mood: ["reverent and graphic", "print-shop direct"]
    light: ["flat shadowless ink laydown", "no modelled lighting beyond the screened tones"]
    composition: ["image filling the entire frame", "one centred white wordmark overlapping the image", "type sitting directly on the screened tones with no plate behind it"]
  negative: ["smooth continuous-tone gradient", "a flat colour layer over an untreated photograph", "oversized countable halftone dots", "a plate, outline or drop shadow behind the type", "a second hue in the highlights", "halftone applied as an overlay texture"]
  tools:
    midjourney: { params: "--raw", no: ["gradient", "outline", "shadow", "texture"] }
    stable_diffusion: { weights: ["(halftone screen:1.3)", "(single ink:1.2)", "(flat white type:1.1)"] }
    seedream: { art_style: "单色半调印刷风格，古典绘画加网为单油墨圆点网点" }
    dalle3: { prose: "A classical painting converted into a fine round-dot halftone and printed in one saturated blue ink on white paper, with a single large white sans-serif wordmark centred over the image and no plate behind it.", deprecated: "2026-05-12" }
    flux: { prose: "A Renaissance painting screened into a fine round-dot halftone and laid down in one saturated blue ink on bare paper, filling the frame edge to edge, with one large white neo-grotesque wordmark centred over the image and sitting directly on the dots.", negative_as_positive: ["every tone carried by dot size on a fixed screen angle", "the image itself screened into halftone, then inked in one colour", "a fine screen that reads as print texture at the output size", "flat white type resting directly on the screened image", "one hue throughout, highlights as bare paper", "the screened subject still reads as a recognisable classical painting"] }
```

各工具字段的语法依据见 `prompt-export/tool-syntax.md`。

## §7 来源与既有实现

**既有实现（overlay）**

- **无。** 本机现有设计 skill（`huashu-design`、`canvas-design`、`impeccable`、`vignelli-canon-design-system`、`muller-brockmann-grid-systems`）都不覆盖半调加网，故 `overlays: []`。§6 的供料契约仍按 `prompt-export/interface.md`。

**来源**（访问日期 2026-09-30）

1. Wikipedia, "Halftone", https://en.wikipedia.org/wiki/Halftone 。支持：半调的定义（以大小或间距变化的网点模拟连续调）；*"The most common method of creating screens, amplitude modulation, produces a regular grid of dots that vary in size."*；频率调制又称 stochastic screening；*"The resolution of a halftone screen is measured in lines per inch (lpi)."*；网角自 9 点钟方向顺时针量度；*"Round dots: most common, suitable for light images, especially for skin tones. They meet at a tonal value of 70%."* 百科类二手来源。**该条目正文未给出 45°／15°／75° 等具体网角数值**，故本条目 §3 不写网角。
2. 用户提供的样张，2026-09-30，1881×836，ObsidianUI 字标。本条目 §1 的阈值、§4 的全部数值、§3 的网点周期均来自对该图的像素测量。测量方法：本机 `screenshot-forensics` skill 的 `scripts/inspect.py`（`crop` / `colors` 子命令）+ 自写的色相直方图与朴素 DFT。原始读数：色相 240° 占 48.3%、240±3° 占 94.1%；明度众数 V=0.85（≈46%）；V<0.70 的像素占 1.468%；网点周期约 2px。
3. Google Fonts 仓库, `ofl/inter/OFL.txt`, https://github.com/google/fonts/tree/main/ofl/inter 。支持：Inter 以 OFL 发布（沿用 `styles/international-typographic.md` §7 [3]）。
4. Google Fonts 仓库, `ofl/archivo/OFL.txt`, https://github.com/google/fonts/tree/main/ofl 。支持：Archivo 以 OFL 发布（沿用 `styles/collage.md` §7 [5]）。

**未核实项（明确标注，不猜）**

- **主体画作的具体身份。** 样张是文艺复兴盛期绘画的局部（两臂相向、云石与烟云背景），**很可能**是米开朗基罗《创造亚当》，但本轮未核实，故本条目**不写画名**。
- **加网史的年代与专利归属**，未核实。
- **样张所用的具体字体**，未核实；§5 只写可见特征与开源候选。

## §8 区分度自检

- **与拼贴（`nearest: collage`）的差别**：拼贴的主体是**异质素材的叠加**，空间由遮挡产生，素材边缘保留剪切或撕裂痕迹；本条目是**单张图像**经过加网，没有叠加、没有剪切边，画面是平的。拼贴 §1 CL-1 要求「至少两种来源不同的素材」，本条目恰好相反：全画面只有一个图像来源。
- **与 Riso（`nearest: riso`，本库暂无条目）的差别**：孔版／丝网印刷的辨识特征是**套色错位与油墨不均**（两块色版偏移、压痕、脏边）；本条目是**单色版**，没有套印、没有错位，纹理全部来自网点。
- **与「彩色半调」（color halftone，四色加网；`nearest: color-halftone`，本库暂无条目）的差别**：这是最容易混的一个，且**本条目恰恰是它的反面**。彩色半调是**分色加网**——C／M／Y／K 四块版各配一个网角（传统 C 15°、M 75°、Y 0°、K 45°）套印，靠错开角度压莫尔纹，所以画面里**必然出现四组方向不同的网点**；本条目是**单块版**，只有一个网角——正因为只有一个通道，才不需要错角。判据：**数色相簇**。样张 94.1% 的像素落在 H=240±3° → 单油墨；若同时出现四个互不重叠的色相簇，那是彩色半调。波普艺术里的 Ben-Day dots 属于后者，**不属于本条目**。
- **一句判定**：画面的灰度是「网点大小」给的（半调），还是「素材叠加 + 统一重新着色」给的（拼贴）？
