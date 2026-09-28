# 版式拆分方法论（decomposition-method）

> 模块：P0-b（上）· 执行卡 E3 · 状态：draft（2026-09-28）
> 激活：仅在请求含 `style: ref/layout-decompose` 时加载；无声明时不参与。
> 大纲依据：`v2-计划书.md` §5.2「拆分方法论大纲」9 步，顺序固定，每步有产出。
> 缺口事实：「版式拆解 / 版式拆分 / layout decomposition」全域仅 1 处弱命中（`antigravity…/mobile-design/mobile-design-thinking.md`，讲移动端布局思考，不讲怎么拆别人的版式），见 `差集比对-勘误补遗-20260928.md` §3 第 5 项。
> 配套：标注法与图层色码见 `grid-annotation.md`；SVG 模板见 `templates/annotation-layer.svg`；完整样例见 `example-gutenberg-b42-leaf.md`（独立文件，以便样例更换时不改动方法正文）。
> 落盘时复核项：① huashu `critique-guide.md`「2.5 倍」两处已核实为第 35、114 行（执行 2026-09-28 在 Mac 上核实），报告原写 116；② `muller-brockmann-grid-systems` 的 grid-toggle、scaffold 所在文件名待落盘复核（实体 `/Users/mac/.agents/skills-master/muller-brockmann-grid-systems`，3 个文件，见 `E0-预检.md` §4）；③ 弱命中文件 `antigravity…/mobile-design/mobile-design-thinking.md` 的完整路径待展开。

---

## 0. 适用范围与通用约定

**0.1 这份方法做什么。** 读出**别人已完成的版式**的结构：结构从哪里来、在哪里被打破、打破服务哪条信息。它不生成网格，也不评判好坏；生成和验证自己的网格归 `muller-brockmann-grid-systems`，评审校验（如「标题 ≥ 正文 2.5 倍、3–4 个层级」）归 huashu `critique-guide.md`（第 35、114 行，执行已核实；报告附表原写 116）。

**0.2 拆分对象。** 单页、单幅海报或一个对页。对页须把两页作为一个拆分对象，因为版心、页眉等结构常跨页成对设计。

**0.3 度量约定。**

- 单位：只有图像时一律用图像像素（`px`），并给出比例；已知实物尺寸时再换算为 mm，且写明换算依据。
- 估算标记：凡由图像测得的数值前加 `≈`，并在拆分表表头注明「估算（基于 ×× 图像，像素 / 比例）」。不得把估算写成文献记载的事实。
- 墨迹外沿与名义尺寸：从图像量到的是墨迹外沿（上伸部顶到下伸部底），不是排版时的名义框；两者差异须在表中注明。
- 置信度：每个产出字段附 `confidence: high | mid | low`。`low` 的字段不得进入第 9 步结论句。

**0.4 历史坐标系优先于现代规则。** 被拆对象若来自手工排字、手绘装饰或照排时代，现代的检查规则（例如 2.5 倍字号比）只可作对照，不可作判决。

---

## 1. 外框与版心

- **目的**：确定页面比例、四边白边与版心（type area）的位置，这是其余所有步骤的坐标系。
- **要测什么**：页面宽高（px 或 mm）及比例；版心四边坐标；内白边、上白边、外白边、下白边；版心面积占页面面积的比例；版心比例是否等于页面比例。可与经典页面构成法对照，例如 Van de Graaf 构成法在 2:3 页面上给出内：上：外：下 = 2:3:4:6、版心与页面同比例 [1]。
- **产出字段**：`page_size`、`page_ratio`、`type_area_bbox`、`type_area_ratio`、`margins {inner, top, outer, bottom}`、`margin_ratio`、`type_area_share`、`canon_check`（对照了哪种构成法及偏差）。
- **常见误判**：
  - 把扫描图边界当页面边界。扫描常裁掉纸边，古籍与装订书还可能经过修边，白边会系统性偏小。
  - 用单页判断左右白边：未区分正面（recto）与反面（verso），把内白边与外白边弄反。
  - 量到与某种构成法接近就宣称「采用了该构成法」。构成法本身是后人的历史重构 [1]，吻合只能写「与 ×× 一致 / 不一致」。

## 2. 栏与模块

- **目的**：判断版心内部是栏网格、模块网格还是无网格，并给出栏数、栏宽、栏距。
- **要测什么**：栏数；每栏左右边线（取多行行首、行尾的中位数）；栏距；是否存在横向分割（模块行）及模块行高；栏宽与行距的倍数关系。
- **产出字段**：`grid_type: column | modular | manuscript | none`、`columns`、`column_widths`、`gutter`、`module_rows`、`module_height`、`column_to_leading_ratio`。
- **常见误判**：
  - 把两端对齐的文字边缘误读为栏线之外还有「子栏」。先确认行尾参差来自连字符悬挂还是真实分栏。
  - 图片与文字同宽就认定是模块网格。模块网格须同时存在可重复的横向分割。
  - 只量一行。行首缩进、首字下沉、悬挂标点都会让单行测量偏离栏线。

## 3. 基线

- **目的**：确定正文行距，检查标题、图注是否落在同一基线网格上。
- **要测什么**：正文相邻行的基线间距（或行心间距，二者差一个常数）；每栏行数；首行与末行位置；标题、图注、页眉的基线是否为行距的整数倍。
- **产出字段**：`leading`、`lines_per_column`、`first_line_y`、`last_line_y`、`headings_on_baseline: yes | no | partial`、`baseline_offsets`。
- **常见误判**：
  - 用墨迹密度峰值当基线，却不说明它是行心。行心间距可以代替基线间距，但位置不能混用。
  - 只在一栏测。两栏基线错位本身就是一条结构信息（例如对齐或不对齐的双栏）。
  - 标题「看起来对齐」即判为落在基线上。必须计算偏移量是否为行距的整数倍。

## 4. 层级

- **目的**：数出有几个字号层级，记录相邻层级的倍率，并区分「靠字号区分」与「靠颜色、字重、位置区分」的层级。
- **要测什么**：每一类文字元素的高度（统一用大写高、x 高或字身高中的同一种）；以正文为 1 的相对倍率；非字号手段（色彩、字重、缩进、位置）。
- **产出字段**：`levels`（列表：`name`、`size_rel`、`means: size | color | weight | position`）、`level_count`、`adjacent_ratios`。
- **常见误判**：
  - 把颜色不同但字号相同的元素算作独立字号层级。它是层级，但不是字号层级。
  - 混用测量基准：一个元素量大写高、另一个量字身高，倍率失真。
  - 直接套用现代校验阈值给历史版式定罪（见 §0.4）。

## 5. 对齐轴

- **目的**：列出所有主要对齐线，判断哪些被多个元素共用，从而找到版式的「骨架线」。
- **要测什么**：竖向轴（栏左右边、缩进线、图片边）、横向轴（版心顶、底，章节起始行）；每条轴被多少个元素使用；是否存在只被一个元素使用的孤立轴。
- **产出字段**：`axes`（列表：`id`、`orientation: v | h`、`position`、`shared_by`）、`primary_axes`、`orphan_axes`。
- **常见误判**：
  - 把每一条边都记成轴。只有被 ≥ 2 个元素共享或承担结构功能的线才是主轴。
  - 忽略光学对齐：圆形字母、引号、首字母常有意越出轴线，不应记为未对齐。
  - 只看竖轴。横向的版心顶线、章节起始线同样是骨架。

## 6. 留白

- **目的**：确定大留白的位置与占比，判断它由结构产生（白边、栏距、段落缺口）还是被刻意保留（单独空出的区域）。
- **要测什么**：各块留白面积占页面比例；最大留白所在位置；该留白是否可由步骤 1–3 的结构参数推导出来。
- **产出字段**：`whitespace_regions`（列表：`where`、`share`、`origin: structural | reserved`）、`largest_region`。
- **常见误判**：
  - 把所有留白都解释为「设计意图」。能由白边和栏距推导出来的，记为 `structural`。
  - 忽略功能性留白。例如为后续手工装饰或批注预留的空间，是生产流程的产物。
  - 在修边或裁切过的图像上计算占比而不加说明。

## 7. 视觉动线

- **目的**：记录第一眼、第二眼、第三眼的落点及其原因，检验结构层级与观看顺序是否一致。
- **要测什么**：按尺寸、明度对比、色彩饱和度、孤立程度排出前三个落点；每个落点对应哪个层级。
- **产出字段**：`fixations`（有序列表：`order`、`element`、`reason`）、`matches_hierarchy: yes | no`。
- **常见误判**：
  - 把阅读顺序（从左上开始读正文）当作视觉动线。动线指未开始阅读前的注视顺序。
  - 单人判读即当结论。本步属主观判读，须标 `confidence: mid` 以下，除非有多名观察者一致。
  - 只按尺寸排序。高饱和色块、越出版心的元素常比更大的灰色文字块先被看到。

## 8. 破格点

- **目的**：找出偏离步骤 1–5 结构的地方，判断偏离是否有意、服务哪条信息。
- **要测什么**：越出版心、越出栏线、脱离基线、改变对齐轴的元素；偏离量；该元素承担的信息功能。
- **产出字段**：`breaks`（列表：`id`、`element`、`deviation`、`intentional: yes | no | unknown`、`serves`）。
- **常见误判**：
  - 把扫描歪斜、纸张变形当作破格。先用多行测量排除系统误差。
  - 把结构本身规定的越界（如页眉本来就在上白边）记为破格而不说明。须注明「结构内越界」与「结构外越界」。
  - 不追问「服务哪条信息」。说不出服务对象的偏离，记为 `intentional: unknown`，不得写成「有意打破」。

## 9. 结论句

- **目的**：用一句话写出「这个版式的结构从哪来、在哪里被打破」，作为可以被引用、被复核的最终产出。
- **要测什么**：不再测量；只允许引用步骤 1–8 中 `confidence` 为 `high` 或 `mid` 的字段。
- **产出字段**：`conclusion`（一句话，≤ 120 字）、`cited_fields`（结论句引用的字段名列表）。
- **常见误判**：
  - 用形容词代替结构（「简洁有力」「节奏感强」）。结论句必须包含结构来源与打破位置两个成分。
  - 引入 1–8 步没有测过的新信息。
  - 把估算写成确定值。结论句中的数值保留 `≈`。

---

## 10. 产出格式（拆分表）

每次拆分交付一张表，字段名与上文一致，示意如下（值为占位）：

```yaml
decomposition:
  source: { title: "", url: "", license: "", image_px: [0, 0] }
  measurement_note: "估算（基于 ×× 图像，像素 / 比例）"
  step1_frame:   { page_ratio: "", type_area_bbox: [], margins: {}, canon_check: "", confidence: mid }
  step2_grid:    { grid_type: "", columns: 0, column_widths: [], gutter: "", confidence: mid }
  step3_baseline: { leading: "", lines_per_column: 0, headings_on_baseline: "", confidence: mid }
  step4_levels:  { levels: [], adjacent_ratios: [], confidence: mid }
  step5_axes:    { axes: [], primary_axes: [], orphan_axes: [], confidence: mid }
  step6_space:   { whitespace_regions: [], largest_region: "", confidence: mid }
  step7_flow:    { fixations: [], matches_hierarchy: "", confidence: low }
  step8_breaks:  { breaks: [], confidence: mid }
  step9:         { conclusion: "", cited_fields: [] }
```

标注图层与标签格式按 `grid-annotation.md`；每个 `axes`、`breaks` 条目的 `id` 与 SVG 标签序号一一对应。

## 11. 与既有实现的分工

| 实现 | 负责 | atlas 本模块 |
| --- | --- | --- |
| `muller-brockmann-grid-systems`（含 grid-toggle 叠层） | 生成并验证自己的网格 | 读出别人的网格；不调用其脚手架 |
| `vignelli-canon-design-system` | Vignelli 体系下的网格、字号与白空间规范 | 拆分结果可与其规范对照，但不改写 |
| huashu `critique-guide.md` | 评审校验（层级数、字号倍率） | 步骤 4 只记录，不下评审结论 |
| `archviz-layout`（archsueh 仓） | 用户自有版式生成 | 下游：拆分表可作为其输入；本期只在 overlay 写接口，不改该仓 |

---

## 来源

访问日期均为 2026-09-28。

1. Wikipedia, "Canons of page construction" — https://en.wikipedia.org/wiki/Canons_of_page_construction — 支持：页面构成法是基于实物测量的历史重构；Van de Graaf 构成法在 2:3 页面上给出白边 2:3:4:6（内：上：外：下）且版心与页面同比例；由 Tschichold《The Form of the Book》推广。
2. Wikipedia, "Grid (graphic design)" — https://en.wikipedia.org/wiki/Grid_(graphic_design) — 支持：网格的定义；Müller-Brockmann《Grid Systems in Graphic Design》与 Hurlburt《Grid》为网格设计的代表文献；1980 年代以后对网格教条化使用的反思。

本机证据：`差集比对-勘误补遗-20260928.md` §3 第 5、7 项（版式拆分仅 1 处弱命中、网格标注 0 命中）；`差集比对-20260928.md` §2 第 5、7 行（`muller-brockmann` 的 grid-toggle 是可视化自己的网格）与附表（huashu `critique-guide.md` 第 35、116 行；执行核实第二处为第 114 行）；`v2-计划书.md` §5.2（下游 `archviz-layout`）。
