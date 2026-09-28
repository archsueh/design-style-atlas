---
id: collage
name_zh: 拼贴
name_en: Collage
lineage: "papier collé 于 1912 年末至 1913 年初由 Braque 与 Picasso 使用；达达派自 1915 年起以照相蒙太奇作抗议手段；Rodchenko 1923 年起实验照相蒙太奇；Schwitters 以 Merz 命名其拼贴与集合作品（来源见 §7 [1][2][3]）"
status: draft
nearest: [memphis]
overlays: [handraw-style, huashu-design]
exception: false
---

# 拼贴（collage）

> 泛化方法论条目（计划书 §6）。花叔库只有 Memphis Maximalism 一个变体（还原度 72%，`差集比对-20260928.md` §1.1 第 3 行），缺通用方法。本条目只补三条机制：
> 1. 叠加建立空间；
> 2. 冲突是被选择的；
> 3. 色彩作统一机制。
>
> 激活：仅 `style: collage`。
> 落盘时复核项：`handraw-style` 四个条目的原文标题格式与编号（见 `overlays/handraw-style.md`）。

## §1 判据

- CL-1 画面里是否至少有两种来源不同的素材（照片、印刷品、纸张、手绘、字样），且素材边缘保留剪切或撕裂痕迹？
- CL-2 素材之间是否有可辨认的前后遮挡，且至少三层，空间深度由遮挡产生，而不是由透视或投影产生？
- CL-3 画面中尺度或语境错位最强的一处，是否正好落在第一视觉落点上？
- CL-4 所有素材是否被同一套限定色（统一去色后重新着色，或统一的双色、三色）覆盖，使不同来源的素材处于同一色域？
- CL-5 文字本身是否也作为被剪下的素材出现（剪报字、不同字族的单字拼成一个词），而不是只以标题层的形式浮在画面顶部？

## §2 反模式

- CL-AP-1 素材全是同一来源的去背景抠图，边缘干净，没有纸张厚度或剪切痕迹。结果是贴纸排列，不是拼贴。
- CL-AP-2 每块素材保留原始色彩，全图没有统一的色处理。异质素材之间的冲突于是变成色彩噪声，第三条机制失效。
- CL-AP-3 冲突平均分布：四角都有同等强度的尺度错位，没有主冲突，视线找不到落点。
- CL-AP-4 滑向孟菲斯：用波浪线、三角、圆点、水磨石纹等几何母题填满空隙，素材叠加被图案铺陈取代（见 §8）。
- CL-AP-5 直接让生图模型输出「collage style」，不检查物理一致性：同一张纸在不同位置前后穿插，各块素材的投影方向互相矛盾。

## §3 排版机制

**结构从哪来：**
1. **承托面**：一张底纸，或一套不可见的栏网格，决定画面边界和文字信息的落位。
2. **遮挡顺序等于信息层级**：越靠前的层承载越重要的信息，所以第一机制「叠加建立空间」同时是层级机制。
3. **主冲突点等于焦点**：第二机制「冲突是被选择的」落实为只设一个主冲突，其余错位降一级。拆分别人的作品时，用 `layout/decomposition-method.md` 的步骤 8「破格点」定位这个主冲突。
4. **色彩统一**：第三机制把异质素材压回同一平面，这是拼贴与杂乱之间的分界。

拆分别人的拼贴成品时，`layout/decomposition-method.md` 步骤 2「栏与模块」允许结论为「无栏网格，结构是叠层」（合并自 c61ed7d 版 §3）。

**在哪里允许打破：**
- 图像素材可以越出承托面，可以旋转，可以被裁切。
- 功能文字（标题、日期、地点）至少要共用一条对齐轴，不参与旋转。如果需要冲突，只由剪报字承担，而且剪报字最多一组。

**史实旁证（不作规则）：** 达达派与 Rodchenko 用照相蒙太奇并置异质图像，服务于政治或社会议题 [3]。这说明拼贴的冲突历来有指向，不是随机叠放。

## §4 色彩

- **关系**：
  - 限定色板：先把原素材统一去饱和，再用两到三色重新着色。
  - 如果需要强冲突，只允许用一对互补色，并且放在主冲突点上。
- **明度结构**：前后层之间保持明显的明度差，用明度而不是投影来分层。纸色作为最亮的中性底。
- **屏幕**：示例主色 `#C8102E`（示例），示例纸色 `#EFE8D8`（示例），仅作预览。
- **印刷时的处理方式**（接口见 `color/pantone-print-system.md` §2.6）：

```yaml
print_handling:
  process: spot                   # 双色调重新着色常以两色专色印刷实现；也可四色，按预算定
  spot_roles: [flat-large-area]
  substrate: uncoated             # 纸张质感是素材的一部分；涂布与否由项目定
  suffix_rule: "编号必须带后缀；非涂布纸用 U 后缀并单独打样"
  proof: required
  screen_examples: "#C8102E、#EFE8D8 为示例，仅作屏幕预览"
  pantone_refs: none
  risks: ["双色叠印区域在非涂布纸上会变暗、扩散，须打样确认层次仍可分辨"]
```

## §5 字体

中文按 `typography/cn-type-classes.md` 三型：

| 型 | 用法 | 理由 | 代表字体与授权（沿用 cn-type-classes §4.2） |
|---|---|---|---|
| 复古旧字体 | 适用于剪报字与主冲突文字 | 活字或刻本的印痕本身就是异质素材 | 朱雀仿宋（开源 OFL 1.1）、源样明体（开源 OFL 1.1） |
| 粗黑无衬线 | 适用于功能文字 | 在层层叠加中仍保持可读 | 思源黑体 Bold / Heavy（开源 OFL 1.1） |
| 新中式 | 慎用 | 细横画在剪切边和叠印下容易断裂 | — |

英文：
- 剪报字允许多个分类混用，常见 Grotesque 与 Didone。这是本风格唯一允许多字族并存的地方。
- 功能文字只用一种 Lineal。
- 开源候选：Archivo Black（开源 OFL [5]）、Playfair Display（开源 OFL [5]）。

## §6 提示词出口

```yaml
prompt_export:
  positive:
    style: ["analog paper collage", "cut-and-paste photomontage", "torn paper edges"]
    mood: ["deliberate tension", "tactile"]
    light: ["flat scanner lighting"]
    composition: ["three or more overlapping layers", "one dominant scale clash at the focal point", "duotone recoloring of all elements", "cut-out letters as material"]
  negative: ["clean die-cut stickers", "original unmatched colors", "evenly scattered clutter", "memphis squiggles and terrazzo pattern", "inconsistent drop shadows"]
  tools:
    midjourney: { params: "--raw", no: ["stickers", "memphis pattern", "drop shadow"] }
    stable_diffusion: { weights: ["(torn paper edges:1.3)", "(duotone:1.2)", "(overlapping layers:1.2)"] }
    seedream: { art_style: "模拟纸本拼贴与照相蒙太奇风格" }
    dalle3: { prose: "An analog paper collage: at least three overlapping cut photographs with visible torn edges, all recolored in the same two-color duotone, with one deliberate scale clash at the center.", deprecated: "2026-05-12" }
    flux: { prose: "Analog paper collage with visible torn and scissor-cut edges, three overlapping layers, every element recolored in one red-and-cream duotone, one oversized element clashing in scale at the focal point.", negative_as_positive: ["hand-cut paper edges with visible paper thickness", "all elements recolored in one shared duotone", "a single dominant focal clash with quieter surroundings", "photographic and typographic fragments only", "flat, even scanner lighting"] }
```

## §7 来源与既有实现

**既有实现与参照（overlay）**
- `overlays/handraw-style.md`：`/Users/mac/Developer/handraw-style/styles_200_reorganized.md` 中的四个拼贴条目：#050 Lane Smith、#064 Paul Rand、#225 OscarAI、#256 Morph（`差集比对-勘误补遗-20260928.md` §4）。
  - **这四条是插画风格参照，不是版式方法论。** 它们描述人物或 IP 的手绘画风，只能作为 §6 的风格词来源，不能作为 §3 的结构依据。
- `overlays/huashu-design.md`：Memphis Maximalism 变体，在 §8 中作对照，不作本条目的内容来源。

**来源**（访问日期 2026-09-28）
1. Tate, Art Term "Collage", https://www.tate.org.uk/art/art-terms/c/collage 。支持：collage 同时指技法与作品，即把纸、照片、织物等粘贴到承托面上；词源于法语 papiers collés；20 世纪初开始作为艺术家技法。另见同站 "Merz" 词条摘要：Schwitters 用 Merz 命名其拼贴与集合作品。
2. Tate, Art Term "Papier collé", https://www.tate.org.uk/art/art-terms/p/papier-colle 。支持：Braque 首先使用；Braque 与 Picasso 于 1912 年最后三个月至 1913 年初制作了多件 papiers collés。
3. Tate, Art Term "Photomontage", https://www.tate.org.uk/art/art-terms/p/photomontage 。支持：照相蒙太奇是用照片构成的拼贴；达达派自 1915 年起用于反战抗议；超现实主义随后采用；Rodchenko 1923 年起实验；John Heartfield 以其抗议法西斯政权。
4. Design Museum, "Memphis Group: awful or awesome?", https://www.designmuseum.org/discover-design/all-stories/memphis-group-awful-or-awesome 。支持：Sottsass 于 1980 年 12 月召集并创立 Memphis；1981–1987 年设计家具、织物、陶瓷等；以鲜艳色彩、几何形、大胆图案和彩色塑料层压板著称（用于 §8）。
5. Google Fonts 仓库, `ofl/archivoblack/OFL.txt`、`ofl/playfairdisplay/OFL.txt`, https://github.com/google/fonts/tree/main/ofl 。支持：两款字体以 OFL 发布。

## §8 区分度自检

- **与孟菲斯（`nearest: memphis`）的差别**：孟菲斯是 Sottsass 于 1980 年末发起、1981–1987 年活跃的设计团体，特征是鲜艳色彩、几何形与图案层压板 [4]。其平面衍生以几何图案铺陈为主体。
- **本条目的主体**：拼贴的主体是异质素材的叠加与剪切边，几何图案即使出现，也只是众多素材中的一种。
- **一句判定**：画面的空间是由素材之间的遮挡产生的（拼贴），还是由平铺的几何图案与色块产生的（孟菲斯）？
