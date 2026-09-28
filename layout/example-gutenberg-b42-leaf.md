# 样例：Gutenberg 42 行圣经单叶（正面）9 步拆分与标注

> 配套：`decomposition-method.md`（方法）、`grid-annotation.md`（图层与标签）、`example-gutenberg-b42-leaf.annotation.svg`（标注叠层，原图以外部链接引用，不嵌入）。
> 状态：draft（2026-09-28）。
> **测量声明：本文件所有数值均为估算（基于 Wikimedia Commons 文件 831 × 1136 px 图像，像素 / 比例），不是文献记载的尺寸。** 测量方法：灰度阈值与投影（行 / 列墨迹计数）、行心自相关求行距、彩色像素阈值定位红蓝手绘元素；脚本与中间文件在 `/workspace/scratch/`，未进入 atlas。
> 落盘时复核项：① 再次打开 Commons 文件页，确认许可仍为 No known copyright restrictions、外链图片地址仍有效；② 页眉「ASTICUS」是否为跨页拆开的 ECCLESIASTICUS、右缘红线为何物，两项待核；③ 全部数值为估算，不得在落盘时改写为文献数据。

---

## 1. 案例信息

| 项 | 内容 |
| --- | --- |
| 对象 | Gutenberg 圣经（42 行圣经，B42）散叶一张的正面（recto），内容为《便西拉智训》（Sirach / Ecclesiasticus）42:14–43:25 [1] |
| 持有与数字化 | Miami University Libraries – Digital Collections；平板扫描（EXIF 设备 Epson GT-15000）[1] |
| 文件页 | https://commons.wikimedia.org/wiki/File:Gutenberg_Bible_leaf_(recto)_(9068078579).jpg [1] |
| 许可 | Commons 标注为 Flickr The Commons「No known copyright restrictions」（FlickreviewR 2015-03-11 复核）[1]；原作为 1450 年代印刷品 [2] |
| 图像 | 831 × 1136 px（Commons 原始文件分辨率）[1] |
| 选择理由 | 双栏、固定行数、两端对齐，且同时存在「排字层」与「手绘层」，适合演示结构与破格的区分 |

**背景事实（非测量）：** 42 行圣经自第 10 页起每页 42 行，行数增加是通过缩小行距而非扩大版面实现 [2]；Gutenberg 已使用两端对齐 [2]；书名等红字标题最初付印，后改为留空由人工补写，宽阔的白边容纳手工装饰 [2]；印刷用纸为 Royal 规格，15 世纪印刷用纸宽高比多为约 1:1.4，未修边的对开叶约 42 × 30 cm，而牛津 Bodleian 藏本的叶面为 40 × 28.6 cm，说明现存各本经过不同程度的修边 [2]。

---

## 2. 9 步拆分表

表头：估算（基于 Commons 文件 831 × 1136 px 图像，像素 / 比例）。坐标原点为图像左上角。

### 步骤 1 · 外框与版心（confidence: mid）

| 字段 | 值 |
| --- | --- |
| `page_size` | ≈ 809 × 1128 px（纸面亮度阈值得到的边界：x ≈ 9–818，y ≈ 2–1130；上缘可能被扫描裁切） |
| `page_ratio` | ≈ 1:1.39（与文献所述 15 世纪纸张约 1:1.4 的比例相近 [2]） |
| `type_area_bbox` | x ≈ 122–673，y ≈ 108–927（墨迹外沿，非名义框） |
| `type_area_ratio` | ≈ 551 × 819 px，≈ 1:1.49 |
| `margins` | 内 ≈ 113，上 ≈ 106，外 ≈ 145，下 ≈ 203（px；正面叶的内白边在左侧） |
| `margin_ratio` | 内：上：外：下 ≈ 1 : 0.94 : 1.28 : 1.80 |
| `type_area_share` | ≈ 49% |
| `canon_check` | Van de Graaf 构成法在 2:3 页面上给出 2:3:4:6（即 1:1.5:2:3）且版心与页面同比例 [3]。本叶页面 ≈ 1:1.39、版心 ≈ 1:1.49，比例不同；白边比例也不一致。由于叶面经过修边、扫描可能裁边，**本估算既不能证实也不能否定该构成法** |

### 步骤 2 · 栏与模块（confidence: high）

| 字段 | 值 |
| --- | --- |
| `grid_type` | `column`（双栏，无横向模块分割） |
| `columns` | 2 |
| `column_widths` | 左栏 x ≈ 122–368（≈ 246 px）；右栏 x ≈ 426–673（≈ 247 px） |
| `gutter` | ≈ 58 px |
| `module_rows` | 无（`MOD-0 none`） |
| `column_to_leading_ratio` | 栏宽 ≈ 12.6 × 行距；栏距 ≈ 3.0 × 行距 |

### 步骤 3 · 基线（confidence: high）

| 字段 | 值 |
| --- | --- |
| `leading` | ≈ 19.5 px（行心间距；左栏 41 个行间距跨 800 px，右栏跨 801 px） |
| `lines_per_column` | 42（两栏均检出 42 行，与文献所述 42 行一致 [2]） |
| `first_line_y` / `last_line_y` | 行心 ≈ 121 / ≈ 922（两栏相差 ≤ 2 px，双栏基线对齐） |
| `headings_on_baseline` | `partial`：红色章号 XLIII 占第 28 行行尾，落在行格内；页眉与首字母不在基线网格上 |
| `baseline_offsets` | 首字母顶 ≈ 655（第 29 行上沿附近），底 ≈ 715（伸入第 31 行） |

### 步骤 4 · 层级（confidence: mid）

以正文行距为 1 计相对高度（统一量墨迹外沿高度）。

| 层级 | 元素 | `size_rel` | `means` |
| --- | --- | --- | --- |
| L1 | 章首字母（蓝色，带红色细笔装饰）| ≈ 3.1 | size + color + position |
| L2 | 页眉书名（红蓝交替的手绘大写，可辨读为 ASTICUS）| ≈ 1.6 | size + color + position |
| L3 | 章号 XLIII（红色）| ≈ 0.9 | color |
| L4 | 句首大写上的红色笔触（阈值检出 ≈ 29 处，可能含噪点）| 1.0 | color |
| L5 | 正文（textura 字体 [2]）| 1.0 | — |

- `level_count`：字号层级 3 个（≈ 3.1 / ≈ 1.6 / 1.0），另有 2 个仅靠颜色区分的层级。
- `adjacent_ratios`：≈ 1.9（L1 / L2）、≈ 1.6（L2 / 正文）。
- 注：页眉与正文之比 ≈ 1.6，低于 huashu `critique-guide.md` 的「标题 ≥ 正文 2.5 倍」校验线；按方法 §0.4，这是历史版式，只作对照记录，不作评审结论。
- 页眉读作 ASTICUS，推断为跨对页书写的书名 ECCLESIASTICUS 的后半（**待核**：需对照同一叶的反面或相邻叶）。

### 步骤 5 · 对齐轴（confidence: high）

| `id` | 方向 | 位置 | `shared_by` |
| --- | --- | --- | --- |
| AX-1 | v | x ≈ 122 | 左栏各行行首 |
| AX-2 | v | x ≈ 368 | 左栏各行行尾（两端对齐，行尾波动约 7 px，含第 28 行短行除外） |
| AX-3 | v | x ≈ 426 | 右栏各行行首 |
| AX-4 | v | x ≈ 673 | 右栏各行行尾（波动约 9 px） |
| AX-5 | v | x ≈ 161 | 仅第 29–30 行（为首字母预留的缩进），孤立轴 |
| AX-6 | h | y ≈ 108 | 两栏顶线 |
| AX-7 | h | y ≈ 927 | 两栏底线 |

- `primary_axes`：AX-1 至 AX-4、AX-6、AX-7。
- `orphan_axes`：AX-5；另有页眉中线 x ≈ 377，与版心中线 x ≈ 397.5 不重合，也是孤立轴。
- 行尾波动的来源（连字符悬挂或手工排字误差）未逐行核实。

### 步骤 6 · 留白（confidence: mid）

| `where` | `share` | `origin` |
| --- | --- | --- |
| 下白边 | ≈ 18% 页高 | structural（版心位置决定）|
| 外白边 | ≈ 18% 页宽 | structural |
| 内白边、上白边 | ≈ 14%、≈ 9% | structural；上白边同时承载页眉 |
| 栏距 | ≈ 58 px 通栏 | structural |
| 左栏第 28 行行尾 | ≈ 1 行的约 1/3 | structural（章末短行），被章号 XLIII 填入 |

- `largest_region`：下白边。
- 白边整体约占页面 51%。文献指出宽白边为手工装饰提供了空间 [2]，因此这些留白同时是生产流程上的预留，而非单页的构图选择。

### 步骤 7 · 视觉动线（confidence: low，单人判读）

| `order` | `element` | `reason` |
| --- | --- | --- |
| 1 | 章首字母 | 全页最大、饱和蓝色、越出栏线 |
| 2 | 章号 XLIII | 紧邻首字母上方的红色块 |
| 3 | 页眉书名 | 位于上白边的红蓝字母，孤立于灰色正文之外 |

- `matches_hierarchy`：yes（前三个落点与 L1–L3 一致）。

### 步骤 8 · 破格点（confidence: mid）

| `id` | `element` | `deviation` | `intentional` | `serves` |
| --- | --- | --- | --- | --- |
| BRK-1 | 章首字母 | 排字层预留 2 行缩进（≈ 39 px ≈ 2 行距），手绘字母高 ≈ 3 行，并向左越出栏线 ≈ 22 px 进入内白边（结构外越界） | yes | 标记第 43 章起点（与 XLIII 配合） |
| BRK-2 | 页眉书名 | 位于上白边（结构内越界）；中线较版心中线偏左 ≈ 21 px | 位置 yes；偏移 unknown | 书名定位 |

- 不计为破格：章号 XLIII（在行格内）；叶面右缘断续的红色竖线（位于纸边，性质未判读，待核）。

### 步骤 9 · 结论句

> 结构来自与纸张比例（≈ 1:1.39）相近的双栏版心和每栏 42 行的固定行距（≈ 19.5 px），两栏两端对齐、共用顶线与底线；结构只在手绘层被打破：章首蓝色首字母在排字预留的两行缩进之外再向内白边溢出约 22 px，与红色章号共同标记第 43 章的起点。

- `cited_fields`：`page_ratio`、`columns`、`lines_per_column`、`leading`、`primary_axes`、`breaks[BRK-1]`、`levels[L1, L3]`。

---

## 3. 标注表（与 SVG 标签逐一对应）

| 图层 | 标签全文 |
| --- | --- |
| PG | `PG-1 w≈809px h≈1128px ratio≈1:1.39` |
| BOX | `BOX-1 x≈122 y≈108 w≈551px h≈819px inner≈113 top≈106 outer≈145 bottom≈203` |
| COL | `COL-1 x≈122 w≈246px gutter≈58px` |
| COL | `COL-2 x≈426 w≈247px` |
| MOD | `MOD-0 none` |
| BL | `BL-1 pitch≈19.5px n=42 first≈121 last≈922` |
| AX | `AX-1 x≈122 shared=col1` |
| AX | `AX-2 x≈368 shared=col1` |
| AX | `AX-3 x≈426 shared=col2` |
| AX | `AX-4 x≈673 shared=col2` |
| AX | `AX-5 x≈161 shared=L29-30 orphan` |
| AX | `AX-6 y≈108 shared=col1,col2` |
| AX | `AX-7 y≈927 shared=col1,col2` |
| BRK | `BRK-1 bbox≈100,655,76,60 dev≈-22px(x) serves=ch43` |
| BRK | `BRK-2 bbox≈307,41,139,32 dev≈-21px(center) serves=running-head` |
| EYE | `EYE-1 order=1 el=initial` · `EYE-2 order=2 el=XLIII` · `EYE-3 order=3 el=head` |

---

## 来源

访问日期均为 2026-09-28。

1. Wikimedia Commons, "File:Gutenberg Bible leaf (recto) (9068078579).jpg" — https://commons.wikimedia.org/wiki/File:Gutenberg_Bible_leaf_(recto)_(9068078579).jpg — 支持：图像来源（Miami University Libraries – Digital Collections，Flickr 9068078579）、内容为 Sirach 42:14–43:25、许可标注「No known copyright restrictions」、原始分辨率 831 × 1136 px、扫描设备 EXIF。原图文件地址（仅供外部链接，未复制进 atlas）：https://upload.wikimedia.org/wikipedia/commons/2/2e/Gutenberg_Bible_leaf_%28recto%29_%289068078579%29.jpg
2. Wikipedia, "Gutenberg Bible" — https://en.wikipedia.org/wiki/Gutenberg_Bible — 支持：1450 年代印于美因茨；自第 10 页起每页 42 行，靠缩小行距实现；两端对齐；textura 字体；红字标题改为留空由人工补写；宽白边容纳手工装饰；Royal 纸规格、约 1:1.4 的纸张比例、未修边对开叶约 42 × 30 cm、Bodleian 藏本叶面 40 × 28.6 cm。
3. Wikipedia, "Canons of page construction" — https://en.wikipedia.org/wiki/Canons_of_page_construction — 支持：Van de Graaf 构成法在 2:3 页面上的白边比例 2:3:4:6 与「版心与页面同比例」；构成法属历史重构。

本机证据：huashu `critique-guide.md` 第 35、114 行（标题 ≥ 正文 2.5 倍、3–4 层级）；`差集比对-20260928.md` 附表原写 116，执行 2026-09-28 在 Mac 上核实为 114。
