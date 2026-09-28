---
id: international-typographic
name_zh: 国际主义
name_en: International Typographic Style
lineage: "1950s Switzerland; International Typographic Style / Swiss Style. Corpus: Josef Müller-Brockmann, Grid Systems in Graphic Design (1981); Massimo Vignelli, The Vignelli Canon."
status: ready
nearest: [bauhaus-default]
overlays: [muller-brockmann-grid-systems, vignelli-canon-design-system, huashu-design]
exception: false
---

# 国际主义

薄条目。本机已有完整实现，本文件只做总览入口与区分句。排版机制与工程细节全部指向 overlay，不重写。

## §1 判据

1. 版心被分成栏（且通常还有行向模块），图和字占整模块，而不是自由漂浮。
2. 正文齐左、右边不齐（flush-left, ragged-right），不是两端对齐撑满。
3. 全页强调色不超过一种，纸面接近白、字接近黑。
4. 无衬线 Grotesque 承担正文；装饰性脚本或展示花体不出现在正文层。

## §2 反模式

1. 把网格画成半透明底纹贴在已经对不齐的内容上（overlay 与内容不在同一盒子）。
2. 大标题的**字框**贴线但油墨因字怀/边距偏出栏线，还宣称「在网格上」。
3. 用蓝紫渐变或多强调色冒充「现代瑞士」。
4. 两端对齐把词距撑出空洞，却仍叫国际主义。

## §3 排版机制

结构从模块网格来：栏 + 行模块 + 基线。打破只允许发生在「一个信息必须跨栏才能远距可读」时，且破格后仍咬住某一条栏线。

实现不在本文件：

- 生成并验证自己的网格 → `overlays/muller-brockmann-grid-systems.md`
- 两档字号、六种基本字体、白空间伦理 → `overlays/vignelli-canon-design-system.md`

## §4 色彩

关系：近黑与近白的明度对立，外加至多一个高饱和强调（历史上常为红）。不是互补色游戏。

屏幕：白底深字。印刷：黑 + 一专色或四色仿一色；不把屏幕渐变下印。年度色不当主色。

## §5 字体

中文：粗黑无衬线作标题方向，正文用常规黑体而非 ExtraBlack（见 `typography/cn-type-classes.md` 型 A）。不要新中式笔锋，不要复古铅印颗粒。

英文：Grotesque（Akzidenz-Grotesk / Helvetica 传统；网上 Inter、Archivo 作替代）。授权：Inter、Source Han Sans 为 OFL；Helvetica 需购买。

## §6 提示词出口

```yaml
prompt_export:
  positive:
    style: ["international typographic style", "Swiss grid poster", "flush-left grotesque sans"]
    mood: ["objective", "restrained", "no decoration"]
    light: ["even print-like lighting", "no neon"]
    composition: ["modular grid", "asymmetric but column-locked", "generous margin"]
  negative: ["centered justified block", "rainbow accents", "script body text", "gradient mesh", "grid overlay misaligned with content"]
  tools:
    midjourney: { params: "--style raw --v 6", no: ["neon", "script font", "justified text"] }
    stable_diffusion: { weights: ["swiss poster:1.2", "modular grid:1.1"] }
    seedream: { art_style_first: "Swiss international typographic poster" }
    dalle3: { prose: "A Swiss-style poster on a modular grid, flush-left grotesque type, one accent color, white paper." }
    flux:
      prose: "Swiss international typographic poster, modular grid, flush-left grotesque, one red accent, white paper."
      negative_as_positive: ["single accent color", "white uncoated paper", "even lighting"]
```

## §7 来源与既有实现

- Müller-Brockmann, *Grid Systems in Graphic Design*, 1981。
- Vignelli, *The Vignelli Canon*。
- 本机：`overlays/muller-brockmann-grid-systems.md`、`overlays/vignelli-canon-design-system.md`。
- 花叔国际主义变体（Swiss Monochrome / Neo-Swiss Billboard / Institutional Swiss Minimal 等）见 `overlays/huashu-design.md`，只引用不改。

## §8 区分度自检

与默认 Bauhaus/Swiss 路径的差别：Bauhaus 默认在本机是「克制 + 几何 + 少装饰」的**审美取向**；本条要求**可验证的模块网格与齐左正文**，并强制把实现交给已有两个 skill，而不是再画一套几何装饰。
