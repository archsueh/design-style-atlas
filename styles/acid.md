---
id: acid
name_zh: 酸性设计
name_en: Acid Graphics
lineage: "定义松散的当代术语。2019 年设计媒体已将其作为一股潮流报道；视觉上援引 1990 年代 rave 与 techno 传单，以及 1960 年代迷幻美学；常被点名的设计师有 David Rudnick、Jonathan Castro、Anja Kaiser、Studio Cryo（来源见 §7 [1][2]；来源质量说明见 §7）"
status: draft
nearest: [cyber-neon]
overlays: [huashu-design]
exception: true
---

# 酸性设计（acid）

> 真缺条目，也是唯一与本机现有审美纪律正面冲突的风格（计划书 §6、§13 R5）。
> 激活：仅 `style: acid`。
> 例外通道：见文末 §9（schema：仅 `exception: true` 可有 §9）。
> 落盘时复核项：huashu `critique-guide.md` 第 9 条原文（标题 `## 常见设计问题 Top 10` 已核实，第 106 行（执行 2026-09-28 在 Mac 上核实）；见 `overlays/huashu-design.md`）。

## §1 判据

- AC-1 版面中最大的元素是否是一组经过液化、拉伸、镜像或倒置处理的字形，且变形后仍能认出至少一个完整单词？
- AC-2 字形或主图形上是否有铬面或液态金属质感，高光沿曲面连续流动？
- AC-3 高饱和酸性色（如荧光黄绿）是以平涂色块或图案出现，而不是以外发光、光晕、泛光出现？
- AC-4 是否有细线几何结构（同心圆、放射线、变形网格、欧普图案）与字形交叠，并产生视觉振动？
- AC-5 日期、地点、阵容等信息是否以极小字号排成密集文字块，与巨型变形标题形成两极尺度？

（依据：霓虹绿、变形与液态金属字形、欧普图案、科幻未来感见 [1]；液态金属是 acid graphics 的组成部分，并与 Rudnick 的层叠几何和锯齿字形相关，见 [2]。判据句由 atlas 自写，AC-5 为 atlas 观察，暂无外部来源。）

## §2 反模式

- AC-AP-1 **退化为深蓝底加霓虹发光**：深蓝或近黑底上叠发光线条和发光字，落回 huashu 第 9 条描述的赛博霓虹 cliché。此时去掉发光，画面即空，说明酸性的字形变形与铬面并未出现。
- AC-AP-2 只放一个铬金属 3D 字，版面其余部分仍是常规居中排版。酸性被降格为单个特效。
- AC-AP-3 变形施加在所有文字上，连日期、票务、地址等功能信息也被液化，导致这些信息不可读。[1] 中受访设计师批评的「偷懒的极繁」即属此类。
- AC-AP-4 只堆笑脸、迷幻漩涡、扎染等 1960 年代迷幻或 acid house 符号，没有铬面、3D 渲染和字形变形。结果是复古迷幻海报，不是当代 acid graphics（[1] 指出当代风格中虽仍有笑脸，但主体已是新手法）。
- AC-AP-5 荧光色以 RGB 值交付印刷，没有指定荧光专色油墨。印出来只是灰暗的四色近似（见 `color/pantone-print-system.md` §2.2、§2.7 第 6 条）。

## §3 排版机制

**结构从哪来（反网格，但不是无结构）：**
1. **中轴或对称轴**：巨型变形字常沿一条竖向或横向中轴展开。这条轴是全页唯一稳定的参照。该规律为 atlas 观察，未经外部来源证实。
2. **两极尺度**：一个巨型标题，加若干极小的信息块，中间尺度几乎为空。
3. **几何细线骨架**：同心圆、放射线或变形网格，为变形字形提供参照系，是振动感的来源。

**在哪里允许打破：**
- 除功能信息块以外，一切都可以变形、倒置、互相交叠。
- 功能信息块必须水平排列、清晰可读，并共用一条对齐轴。这是本风格唯一不可打破的约束，对应 AC-AP-3。

**与默认纪律的关系**：本机制与 Bauhaus / Swiss 默认路径冲突，只经上文的例外通道生效。

## §4 色彩

- **关系**：以一个高饱和酸性色为主，再从下面两种组合中选一种：
  - 与其互补色（品红、紫）并置，制造振动；
  - 与无彩色（铬银、黑、白）并置。
- **明度结构**：
  - 铬面高光提供局部最高明度。
  - 酸性色平涂处于中高明度。
  - 底色不限，常为白、浅灰或荧光色本身。与赛博霓虹不同，本风格不依赖暗底来衬托发光。
- **屏幕**：示例主色 `#C6F000`（示例），示例互补色 `#E0118C`（示例）。屏幕 sRGB 呈现不出荧光油墨在印刷品上的效果，只能作预览。
- **印刷时的处理方式**（接口见 `color/pantone-print-system.md` §2.6）：

```yaml
print_handling:
  process: cmyk+spot
  spot_roles: [neon, metallic]    # 荧光色与金属色都须专色油墨
  substrate: either
  suffix_rule: "编号必须带后缀；荧光、金属专色在 C 与 U 上分别打样"
  proof: required
  screen_examples: "#C6F000、#E0118C 为示例，仅作屏幕预览"
  pantone_refs: none
  risks: ["四色无法指定荧光油墨与金属油墨", "铬面效果若只靠四色渐变模拟，印刷后会失去金属反光"]
```

## §5 字体

中文按 `typography/cn-type-classes.md` 三型：

| 型 | 用法 | 理由 | 代表字体与授权（沿用 cn-type-classes §4.2） |
|---|---|---|---|
| 粗黑无衬线 | 适用于变形母体 | 笔画厚，液化和拉伸后仍能辨认 | 思源黑体 Heavy、得意黑、站酷庆科黄油体（均为开源 OFL 1.1） |
| 复古旧字体（美术字支） | 慎用 | 几何构件与液化变形叠加后难以辨认 | — |
| 新中式 | 不用 | 细横画与尖锋会在液化中断裂 | — |

英文：
- 变形母体用 Display，或粗字重 Grotesque。
- 信息块用等宽体或细 Lineal。
- 开源候选：
  - Syne：开源 OFL，Google Fonts 元数据分类 DISPLAY [4]。
  - Unbounded：开源 OFL [4]。
  - IBM Plex Mono：开源 OFL [4]。

## §6 提示词出口

```yaml
prompt_export:
  positive:
    style: ["acid graphics poster", "liquid chrome typography", "warped mirrored lettering", "op-art line patterns"]
    mood: ["abrasive", "artificial", "ironic"]
    light: ["hard specular highlights on chrome"]
    composition: ["one giant distorted headline on a central axis", "tiny dense info blocks", "flat fluorescent color fields"]
  negative: ["dark navy background", "neon glow and bloom", "synthwave sunset grid", "tie-dye and smiley pastiche", "distorted small info text"]
  tools:
    midjourney: { params: "--raw", no: ["glow", "bloom", "synthwave", "tie-dye"] }
    stable_diffusion: { weights: ["(liquid chrome lettering:1.3)", "(flat fluorescent yellow-green:1.2)", "(op-art line pattern:1.1)"] }
    seedream: { art_style: "酸性平面设计风格（acid graphics），液态铬金属字" }
    dalle3: { prose: "An acid graphics poster: one giant warped liquid-chrome headline on a central axis over a flat fluorescent yellow-green field, thin op-art concentric lines behind it, and tiny crisp info text blocks.", deprecated: "2026-05-12" }
    flux: { prose: "Acid graphics poster: a giant warped liquid-chrome headline on a central vertical axis, flat fluorescent yellow-green background, thin concentric op-art lines vibrating behind the letters, tiny crisp monospaced info blocks in the corners.", negative_as_positive: ["off-white or flat fluorescent background", "flat matte fluorescent color fields", "concentric op-art linework", "contemporary 3D chrome rendering", "small info text set straight, level and crisp"] }
```

## §7 来源与既有实现

**来源质量说明**
- 「Acid Graphics」没有公认定义。[1] 中被点名的设计师 Anja Kaiser 表示不熟悉这一术语；另一位受访设计师 Hugo Hoppmann 对标签本身持怀疑态度。
- 本轮未找到博物馆或档案机构给出的定义。
- 可用来源只有设计媒体报道 [1][2]（AIGA Eye on Design，属设计行业媒体）和百科 [3]（弱）。
- 因此 lineage 只写媒体可证的内容，§1 判据标明哪些是 atlas 观察。

**本机证据**
- `easy-vibe/docs/zh-cn/…/llm-skills-beautiful/index.md` 第 512 行有一行关键词先例：「酸性设计 | Acid Graphics | 金属质感、玻璃态、锯齿字体 | …」（`差集比对-勘误补遗-20260928.md` §3 第 3 项）。**仅作命名参照**，不作判据来源。其中「玻璃态」未被本条目采纳：[1][2] 均未提及。
- huashu `critique-guide.md` 第 148–151 行（常见问题第 9 条），见 `overlays/huashu-design.md`。

**来源**（访问日期 2026-09-28）
1. Emily Gosling, "'Acid Graphics' Are the New Psychedelia—With a Heady Dose of Cynicism", AIGA Eye on Design, 2019-09-05, https://eyeondesign.aiga.org/acid-graphics-are-the-new-psychedelia-with-a-heady-dose-of-cynicism/ 。支持：
   - 风格特征：大量霓虹绿；扭曲、倒置、液态金属般的实验字形；欧普图案；科幻未来感。
   - 谱系：援引 1990 年代 rave 与 techno 传单，并与 1960 年代迷幻美学对照。
   - 人物：David Rudnick 被称作被广泛模仿的参照；Jonathan Castro、Anja Kaiser、Studio Cryo 等人被提及。
   - 其他：Instagram 账号 @acidgraphix 于 2018 年开设；受访者对该标签的保留意见。
2. Liz Stinson, "The Futuristic Gleam of 'Liquid Metal' is Everywhere Right Now—Here's Why", AIGA Eye on Design, 2019-09-26, https://eyeondesign.aiga.org/the-futuristic-gleam-of-liquid-metal-is-everywhere-right-now-heres-why/ 。支持：液态金属是 acid graphics 的组成部分；该类型因 David Rudnick 的层叠几何与锯齿字形而流行，特征包括闪亮、难以辨读、明显人工。
3. Wikipedia, "Acid house", https://en.wikipedia.org/wiki/Acid_house 。支持：笑脸符号在 1980–1990 年代被广泛用作该音乐类型的标志。**弱来源（百科）**，只用于 AC-AP-4 的背景说明。
4. Google Fonts 仓库, `ofl/syne`、`ofl/unbounded`、`ofl/ibmplexmono`, https://github.com/google/fonts/tree/main/ofl 。支持：三款字体以 OFL 发布；Syne 的 METADATA.pb 分类含 DISPLAY。

## §8 区分度自检

- **与赛博霓虹（`nearest: cyber-neon`）的差别**：赛博霓虹以深色夜景底上的发光线条和发光字为主角。酸性以变形字形、铬面和欧普细线振动为主角，荧光色以平涂出现，底色不限。
- **一句判定**：去掉所有外发光和光晕之后，画面是否仍然成立？仍成立的是酸性；只剩一片暗底的是赛博霓虹，也就是 AC-AP-1。

## §9 例外通道

范围：在 `style: acid` 下局部覆盖 huashu 禁区第 9 条（schema：仅 `exception: true` 的条目可有本节）。

**被覆盖的对象**
- 文件：`/Users/mac/.agents/skills-master/huashu-design/references/critique-guide.md`。
- 条目：`## 常见设计问题 Top 10` 第 9 条「赛博霓虹滥用」。报告转述原文为：深蓝底加霓虹色发光效果，属于默认审美禁区，且已成为最大的 cliché 之一（`差集比对-20260928.md` §1.4）。

**生效范围**
1. 只在当前请求显式包含 `style: acid` 时生效，请求结束即失效。
2. 未声明 `style:`，或声明了其他风格时，第 9 条照常适用，默认评审纪律不变。

**覆盖什么**
- 在本请求内，高饱和荧光色、强色彩振动、刻意的「难看」，不再因第 9 条被判为问题。

**不覆盖什么**
- 「深蓝或近黑底加霓虹发光」这一组合仍判失败。它在本条目中就是反模式 AC-AP-1。例外通道只放行酸性色，不放行赛博霓虹。
- huashu 其余九条常见问题仍然适用。

**不改文件**
- atlas 不修改 huashu 任何文件。E0 基线：huashu 的 `tree_sha256` 为 `519e1ffc…a4e8`（`E0-预检.md` §4）。E10 复核时，该值应保持不变。

**评审写法**
- 结论中写明：「依 atlas `acid` 例外通道，huashu 第 9 条不用于判定荧光色使用；深蓝底加发光按 AC-AP-1 判定。」
