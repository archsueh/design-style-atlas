# 网格案例标注法（grid-annotation）

> 模块：P0-b（下）· 执行卡 E3 · 状态：draft（2026-09-28）
> 激活：仅在请求含 `style: ref/grid-annotate` 时加载；无声明时不参与。
> 大纲依据：`v2-计划书.md` §5.2「标注法大纲」。
> 缺口事实：「网格标注 / grid annotation / baseline grid overlay」全域 0 命中；`muller-brockmann-grid-systems` 的 grid-toggle 用来显示自己页面的网格，不用于标注别人的案例（`差集比对-勘误补遗-20260928.md` §3 第 7 项）。
> 配套：拆分步骤见 `decomposition-method.md`；模板 `templates/annotation-layer.svg`；样例 `example-gutenberg-b42-leaf.md` 与 `example-gutenberg-b42-leaf.annotation.svg`。
> 落盘时复核项：① `muller-brockmann-grid-systems` 中 grid-toggle 与 Puppeteer 验证所在的文件名与章节标题待落盘复核（实体 `/Users/mac/.agents/skills-master/muller-brockmann-grid-systems`）；② 图层 hex 为 atlas 自定屏幕色，落盘时只需确认与 `templates/annotation-layer.svg` 一致。

---

## 1. 图层约定

六个必需图层对应 §5.2 列出的版心、栏、模块、基线、对齐轴、破格点；另设两个辅助图层：外框（为步骤 1 提供测量基准）与动线（步骤 7，扩展，非 §5.2 必需）。

颜色与线型同时编码：同一图层固定一种颜色**和**一种线型，黑白打印或色觉差异时仍可凭线型区分（冗余编码原则，参见 Okabe & Ito 的色觉无障碍设计建议 [1]）。下表 hex 为 atlas 自定的**屏幕标注色**，只用于叠层，不是任何印刷色规格。

| 图层 | 代码（SVG `<g id>`） | 颜色 hex | 线宽 | 线型（`stroke-dasharray`） | 填充 | 对应拆分步骤 |
| --- | --- | --- | --- | --- | --- | --- |
| 外框（辅助） | `PG` | `#6E6E6E` | 1 | 实线 | 无 | 1 |
| 版心 | `BOX` | `#0072B2` | 2 | 实线 | 无 | 1 |
| 栏 | `COL` | `#56B4E9` | 1.5 | 虚线 `8 4` | 同色，不透明度 0.12 | 2 |
| 模块 | `MOD` | `#009E73` | 1 | 点线 `2 3` | 无 | 2 |
| 基线 | `BL` | `#CC79A7` | 0.75 | 实细线 | 无 | 3 |
| 对齐轴 | `AX` | `#E69F00` | 1.25 | 点划线 `10 3 2 3` | 无 | 5 |
| 破格点 | `BRK` | `#D55E00` | 2 | 实线外框 + 对角叉标记 | 同色，不透明度 0.15 | 8 |
| 动线（扩展） | `EYE` | `#000000` | 1.5 | 长虚线 `12 6` + 箭头 + 序号圈 | 无 | 7 |

**层序（自下而上）：** 原图 → `PG` → `COL` → `MOD` → `BL` → `BOX` → `AX` → `BRK` → `EYE` → 图例。版心线压在栏与基线之上，破格点与动线在最上层，保证它们不被遮挡。

## 2. 标签格式

**2.1 语法**

```
[层]-[序号] 键=值 [键=值 …]
```

- `层`：上表的代码（`PG` `BOX` `COL` `MOD` `BL` `AX` `BRK` `EYE`）。
- `序号`：从 1 起的整数，同一图层内唯一；与拆分表中 `axes`、`breaks` 等条目的 `id` 一一对应。`0` 保留给「本层不存在」，例如 `MOD-0 none`。
- `值`：带单位（`px`、`mm`）或比例（`1:1.39`）；估算值前加 `≈`，不确定的判读后加 `?`。
- 示例（计划书原例）：`COL-3 w=48px gutter=16px`。

**2.2 各层推荐键**

| 层 | 推荐键 |
| --- | --- |
| `PG` | `w` `h` `ratio` |
| `BOX` | `x` `y` `w` `h` `ratio` `inner` `top` `outer` `bottom` |
| `COL` | `x` `w` `gutter` |
| `MOD` | `rows` `h` `gutter` |
| `BL` | `pitch` `n` `first` `last` |
| `AX` | `x` 或 `y`，`shared` |
| `BRK` | `bbox` `dev`（偏离量与方向）`serves` |
| `EYE` | `order` `el` `why` |

**2.3 书写规则**

- 标签放在被标注几何体的外侧，用 0.5 px 引线连接，不压在原图文字上（直接标注优于远离图形的图例 [1]）。
- 一个标签只描述一个几何体；同一数值不在两层重复标注。
- 标签字体用系统无衬线体，字号不小于画布短边的 1.2%，保证缩小预览时可读。

## 3. 输出物

每个案例交付三件，缺一不算完成：

1. **原图引用**：来源页 URL、许可、图像像素尺寸。原图不复制进 atlas 仓库；SVG 中以外部链接 `<image href>` 引用，或留空由使用者本地放入。
2. **标注 SVG 叠层**：由 `templates/annotation-layer.svg` 复制而来；`viewBox` 等于原图像素尺寸，保证标签数值与画布坐标一致。
3. **9 步拆分表 + 标注表**：拆分表字段见 `decomposition-method.md` §10；标注表逐行列出 SVG 中每个标签的全文。

## 4. 操作流程

1. 复制模板，把根元素的 `width`、`height`、`viewBox` 改为原图像素尺寸。
2. 在 `#source` 组内填写 `<image href>`（外部链接）与来源元数据（`<title>`、`<desc>`）。
3. 按拆分步骤 1 → 8 依次绘制 `PG`、`BOX`、`COL`、`MOD`、`BL`、`AX`、`BRK`，每画一个几何体即写一个标签。
4. 需要时绘制 `EYE`。
5. 删除模板中的占位几何体（带 `data-placeholder="true"` 的元素）。
6. 校验：SVG 可被 XML 解析器读取；八个图层 `id` 齐全（不存在的层保留空组并写 `-0 none` 标签）；标签序号与拆分表一致。

## 5. 与 `muller-brockmann-grid-systems` 的分工

| 问题 | `muller-brockmann-grid-systems` | atlas 标注法 |
| --- | --- | --- |
| 网格从哪来 | 由它生成（scaffold 生成器） | 从别人的成品中读出 |
| 验证什么 | 自己的页面元素是否贴合自己的网格（Puppeteer 验证，见 `差集比对-20260928.md` §2 第 1 行） | 读出的网格与成品的偏差、偏差是否有意 |
| 叠层用途 | grid-toggle：开发时显示网格 | 教学与分析：把测量结果画在原图上并附数值 |
| 输出 | 可运行的页面 | 原图引用 + SVG 叠层 + 拆分表 |

两者不互相调用。若需要把读出的网格用于新作品，流程是：atlas 拆分表 → 人工确认 → 交给 `muller-brockmann-grid-systems` 或用户自有的 `archviz-layout` 生成（本期只写接口，不改后者，见 `v2-计划书.md` §5.2）。

---

## 来源

访问日期均为 2026-09-28。

1. Masataka Okabe & Kei Ito, "Color Universal Design (CUD) — How to make figures and presentations that are friendly to Colorblind people" — https://jfly.uni-koeln.de/color/ — 支持：不要只用颜色传达信息，应同时用线型、形状区分（redundant coding）；标签直接写在图形上，避免远离图形的图例；细线与小符号应选择更易分辨的颜色。本文件的具体 hex 为 atlas 自定，未声称取自该页调色板。

本机证据：`差集比对-勘误补遗-20260928.md` §3 第 7 项（网格标注 0 命中）；`差集比对-20260928.md` §2 第 1、7 行（`muller-brockmann-grid-systems` 的 scaffold 生成器、Puppeteer 验证与 grid-toggle overlay）；`v2-计划书.md` §5.2（标签格式原例 `COL-3 w=48px gutter=16px`、输出物三件、下游 `archviz-layout`）。
