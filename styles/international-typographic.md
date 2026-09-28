---
id: international-typographic
name_zh: 国际主义平面设计（瑞士风格）
name_en: International Typographic Style
lineage: "1950–1960 年代以瑞士为中心成形；期刊 Neue Grafik 于 1958 年在苏黎世创刊，1958–1965 年共出 18 期，创办人为 Josef Müller-Brockmann、Hans Neuburg、Richard Paul Lohse、Carlo Vivarelli（来源见 §7 [1][2]）"
status: draft
nearest: [bauhaus]            # 指用户的默认 Bauhaus / Swiss 路径，不是 atlas 条目
overlays: [muller-brockmann-grid-systems, vignelli-canon-design-system, huashu-design]
exception: false
---

# 国际主义平面设计（international-typographic）

> 薄条目（计划书 §6）。本机已过度覆盖此风格（`差集比对-20260928.md` §2 第 1 行）。本条目只做入口与区分，§3 与 §7 指向既有实现，不重写。
> 激活：仅 `style: international-typographic`。未声明时 atlas 不参与，默认 Bauhaus / Swiss 路径不变。
> 落盘时复核项：三个 overlay 中标注「待落盘复核」的文件名与章节标题。

## §1 判据

- IT-1 能否画出一套贯穿全页的栏或模块网格，且所有文字块的左缘都落在这组栏线上？
- IT-2 标题与正文是否属于同一个无衬线字族，只以字重和字号区分，全页不出现第二个字族？
- IT-3 文字是否左齐右不齐（flush left, ragged right），全页找不到两端对齐造成的字距拉伸？
- IT-4 图像是否为客观摄影或几何抽象，而不是插画、装饰纹样或手绘？

（依据：网格起版、左齐右不齐、无衬线、客观摄影四点见 [1] 所转引的 Meggs 第 356 页；判据句为 atlas 自写。）

## §2 反模式

- IT-AP-1 只借用 Helvetica 与红白黑配色，却没有网格：各文字块的左缘互不对齐，风格退化成「一款字体加一组配色」。
- IT-AP-2 把网格线作为装饰印在成品上。本风格用网格组织内容，并不展示网格本身；网格只应出现在标注图层（`layout/grid-annotation.md`）里。
- IT-AP-3 中文长文照搬西文的左齐右不齐加宽松字距，并使用标题字重。结果是右缘锯齿过深、全文黑度过重，违背「内容优先于修饰」的初衷。

## §3 排版机制

- **结构从哪来**：数学网格先于内容 [1]。生成与验证网格见 overlay `muller-brockmann-grid-systems`；字号层级、字体数量与留白纪律见 overlay `vignelli-canon-design-system`。
- **在哪里允许打破**：atlas 不另立规则，以上两份 overlay 的规定为准。
- **atlas 自己只提供**：读别人的国际主义作品时，用 `layout/decomposition-method.md` 的 9 步拆分和 `layout/grid-annotation.md` 的标注法。

## §4 色彩

- **关系**：无彩色（黑、白、灰）作底，加一个高纯度色作唯一强调。它不属于互补、邻近等多色关系，而是「单一强调色」结构。
- **明度结构**：文字与底之间高明度差；强调色只用于一个信息层级。
- **屏幕**：示例强调色 `#D52B1E`（示例）。只用于预览，不代表任何品牌或潘通色。
- **印刷时的处理方式**（接口见 `color/pantone-print-system.md` §2.6）：

```yaml
print_handling:
  process: cmyk+spot
  spot_roles: [flat-large-area]   # 强调色常以大面积平涂出现
  substrate: either
  suffix_rule: "编号必须带后缀；C 与 U 分别打样"
  proof: required
  screen_examples: "#D52B1E 为示例，仅作屏幕预览"
  pantone_refs: none
  risks: ["强调色大面积平涂时，四色叠印的批次偏差最容易被看出"]
```

## §5 字体

- **中文**：标题用「粗黑无衬线」（`typography/cn-type-classes.md` §1）。正文用同源黑体的常规字重，它不属于三型中的粗黑型，渲染参数交给 `chinese-typography-system`。
  - 代表字体：思源黑体。开源 OFL 1.1，状态沿用 `cn-type-classes.md` §4.2。
- **英文**：Lineal，Neo-grotesque 类（描述词沿用 `cn-type-classes.md` §5 的口径）。
  - Helvetica：史上与本风格关联最紧 [1]，属商业字库，本轮未读官方许可页，授权状态**未核**。
  - Univers：同为 1950 年代同期字族 [1]，授权状态**未核**。
  - 开源替代：Inter，开源 OFL [3]。它是当代字体，不是史实字体。

## §6 提示词出口

```yaml
prompt_export:
  positive:
    style: ["International Typographic Style poster", "Swiss modernist layout", "objective black-and-white photography"]
    mood: ["objective", "orderly", "restrained"]
    light: ["even flat lighting"]
    composition: ["strict modular grid", "flush-left ragged-right text blocks", "asymmetric balance", "single sans-serif family"]
  negative: ["decorative illustration", "centered symmetrical layout", "justified text rivers", "multiple typefaces", "visible grid lines as ornament"]
  tools:
    midjourney: { params: "--raw", no: ["illustration", "ornament", "script font"] }
    stable_diffusion: { weights: ["(modular grid:1.2)", "(flush left text:1.1)", "(sans-serif typography:1.2)"] }
    seedream: { art_style_first: "瑞士国际主义平面设计风格" }
    dalle3: { prose: "A poster built on a strict modular grid, with flush-left ragged-right text set in one sans-serif family and an objective black-and-white photograph." }
    flux: { prose: "Swiss International Typographic Style poster: a strict modular grid, flush-left ragged-right text in a single sans-serif family, one objective black-and-white photograph, one red accent.", negative_as_positive: ["photographic or purely geometric imagery", "asymmetric grid-aligned layout", "ragged-right text with even word spacing", "one sans-serif family throughout", "grid implied only by alignment"] }
```

各工具字段的语法依据见 `prompt-export/tool-syntax.md`。

## §7 来源与既有实现

**既有实现（overlay）**
- `overlays/muller-brockmann-grid-systems.md`：网格的生成与验证。
- `overlays/vignelli-canon-design-system.md`：字体与字号纪律。
- `overlays/huashu-design.md`：花叔的 5 个国际主义变体，分别是 Editorial Brutalism、Swiss Monochrome、Neo-Swiss Billboard Editorial、Institutional Swiss Minimal、Functional Brutalism（`差集比对-20260928.md` §1.1、§2 第 1 行）。

**来源**（访问日期 2026-09-28）
1. Wikipedia, "International Typographic Style", https://en.wikipedia.org/wiki/International_Typographic_Style 。支持：网格起版、左齐右不齐、无衬线、客观摄影（条目转引 Meggs' History of Graphic Design 第 356 页）；Univers 与 Helvetica 的年代关联。百科类二手来源。注：该条目正文把 Neue Grafik 的创刊年写作 1959，与 [2] 的 1958 冲突，本文采用 [2]。
2. Wikipedia, "Neue Grafik", https://en.wikipedia.org/wiki/Neue_Grafik 。支持：1958 年 2 月 15 日在苏黎世创刊；1958–1965 年共 18 期；四位创办人；提倡以摄影为核心元素。百科类二手来源，条目转引 Eskilson《Graphic Design: A New History》。
3. Google Fonts 仓库, `ofl/inter/OFL.txt`, https://github.com/google/fonts/tree/main/ofl/inter 。支持：Inter 以 OFL 发布。
4. Wikipedia, "Bauhaus", https://en.wikipedia.org/wiki/Bauhaus 。支持：包豪斯是 1919–1933 年运行的德国艺术学校（用于 §8）。

## §8 区分度自检

- **与默认 Bauhaus 路径（`nearest: bauhaus`）的差别**：默认路径是用户未声明 `style:` 时的审美基线，由既有 skill 负责，atlas 不介入也不改写它。包豪斯作为史实是 1919–1933 年的学校 [4]，早于本风格成形 [1][2]。
- **本条目的门槛**：只在显式 `style: international-typographic` 时加载，要求 §1 的四项可测条件同时成立：贯穿全页的栏网格、单一无衬线字族、左齐右不齐、客观摄影。满足默认路径的几何与原色审美，不等于满足本条目。
