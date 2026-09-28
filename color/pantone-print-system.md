# 潘通印刷色体系（pantone-print-system）

> 模块：P0-c（E4）。写法口径：「现有 2 行」对「需要成体系」，不写成「全空白」。
> 边界：潘通色号与色值属厂商专有资料。本文只写体系与流程，**不收录色号数值表**，也不给任何潘通色的 hex / CMYK / Lab 值。需要举例时一律写成占位形式 `Pantone ### C`。
> 核验日期：2026-09-28。所有外部事实见文末「来源」。
> 落盘时复核项：① 在 Mac 上展开 `claude-skills/marketing-skill/…/brand-identity-and-framework.md` 中的 `…`，用 `grep -n` 核对第 253、255 行原文与行号对应；② 展开 `claude-scholar/…/design-guidelines.md` 的完整路径（HIG `color.md` 路径已定，见 §1 注）；③ 来源 [4][14][15] 为旧版或二手页面，落盘时再查 pantone.com 是否有现行替代页；④ Formula Guide 色数等随版本变化的数字按落盘当日官方页更新。

---

## 1. 现有 2 行

本机全域检索只命中 2 行实质内容（差集比对-勘误补遗-20260928.md 第 116、184 行，记为 [L1]）：

| 出处 | 原文（原样引用） |
|---|---|
| `claude-skills/marketing-skill/…/brand-identity-and-framework.md` 第 253 行 | 「Always use CMYK values for print production (never RGB or hex)」 |
| `claude-skills/marketing-skill/…/brand-identity-and-framework.md` 第 255 行 | 「Proof against Pantone reference before bulk print runs」 |

注：
- 路径中的 `…` 沿用报告原文。本稿无法访问原机，完整路径待落盘时用 `grep -n` 复核。行号与句子的对应关系按报告行文顺序排列，也待复核。
- 另有 `claude-scholar/…/design-guidelines.md` 与 HIG `color.md`，二者只把 CMYK 当色彩模型定义 [L1]。HIG `color.md` 本机有 4 份副本，本稿所指为 `~/Developer/skill-libraries/antigravity-awesome-skills/skills/hig-foundations/references/color.md`（执行 2026-09-28 在 Mac 上核实）。
- 本机缺失的层：专色与四色的取舍、C/U 等后缀、色卡与打样节点、年度色的定位、与风格条目的接口。

对现有 2 行的定位：
- 第 253 行是「印刷不用屏幕值」的正确底线，但它把印刷色一律归为 CMYK，没有覆盖专色。Pantone 官方同样认为，RGB 与 CMYK 数值都不能用来定义一个颜色，它们只是随设备而变的「配方」[1]。因此第 253 行在本模块中只适用于四色印刷分支，见 §2.2。
- 第 255 行对应本模块 §2.4 的「打样—签样」节点。它只说了「要比对」，没有写明比对所用的色卡版本、纸张后缀和光源。

---

## 2. 需要成体系

### 2.1 屏幕色与印刷色

**分工**

| 色彩表示 | 所属 | 用途 | 能否作为印刷依据 |
|---|---|---|---|
| RGB / hex | 屏幕，设备相关 [1] | 界面、屏幕预览、数字交付 | 不能 |
| OKLCH（CSS Color 4 定义的色彩函数 [13]） | 屏幕与 CSS 端 | 界面色阶、明度关系的计算与调校 | 不能 |
| CMYK | 印刷，设备相关：同一组 CMYK 数值在六台印刷机上会印出六种颜色 [1] | 四色印刷的分色配方 | 只能作为特定印刷条件下的配方，不能作为颜色的定义 [1] |
| CIELAB | 设备无关，CIE 推荐的色彩空间 [1] | 测色、比较色差 | 可以作为测量与比对语言，但不能代替实体色卡签样 |
| Pantone 专色编号（带后缀） | 印刷，实体油墨标准 | 专色印刷的指定语言 | 可以，但须配合实体色卡与打样，见 §2.4 |

**规则**
- 屏幕上显示的潘通色只是计算机模拟，可能与潘通颜色标准不符；官方要求用实体出版物目视评估后再使用 [11]。所以任何屏幕近似值，包括 Color Bridge 指南印在色块下方的 sRGB/HTML 数据 [1]，都只能用于预览，不能作为印刷依据。
- 风格条目中的示例 hex 属于屏幕层，必须标注「示例」（计划书 §4 schema 第 125 行，记为 [L2]），不得被下游当作印刷规格。

### 2.2 四色印刷与专色

**定义**
- 四色（process）：用 CMYK 网点叠印出颜色。也有使用最多七种原色墨的加色域体系 [1]。
- 专色（spot / solid）：不经网点，用专门调配的油墨直接印出颜色。PMS 颜色即属此类 [1]。专色由印厂油墨间或油墨供应商用 18 种基础油墨按 Pantone 调墨配方调制 [1]。生产这 18 种基础油墨的厂商须获得 Pantone 授权 [1]。

**覆盖范围（官方口径）**
- 典型印刷环境下，只用 CMYK 能以「几乎察觉不到的差异」印出约 55% 的 PMS 专色 [1]。
- 加入橙、绿、紫三种基础油墨，组成 CMYKOGV 扩展色域（ECG），可覆盖至约 90% [1]。
- Extended Gamut Guide 用七色印刷模拟 1,729 个 PMS 专色 [1]。

**必须用专色的四种情况**（计划书 §5.3 第 181 行）

| 情形 | 理由 | 依据 |
|---|---|---|
| 品牌主色 | 专色的纯度与一致性适合企业标志与识别系统，这类场合对轻微偏差也很敏感 [1]。四色数值则随印刷机而变 [1] | [1] |
| 金属色 | Metallic 颜色被视为 PMS 的一部分，因为同样不经网点印制 [1]。官方另有金属色指南 [6]。四色数值无法指定金属油墨 | [1][6] |
| 荧光色 | Neon 颜色同属 PMS 专色 [1]，官方另有粉彩与荧光指南 [7]。四色数值无法指定荧光油墨 | [1][7] |
| 大面积平涂 | 四色叠印受纸张吸收、网点扩大、油墨附着等变量影响 [1]，大面积平涂时这些偏差更容易被看出 | 前半句有 [1]；「大面积更易察觉」是 atlas 推论，待印厂实测 |

**不必或不宜用专色的情况**
- 照片、连续渐变、多色插图：走四色。
- 若一件印品中专色需求超过三色：官方指出专色最适合一至三色的印件，且成本可能高于四色印刷 [1]。此时应先用 Extended Gamut Guide 评估七色印刷能否达标 [1]，再决定是保留专色还是改用 ECG。

**决策顺序**
1. 该颜色是否承担品牌识别，或是否为金属色、荧光色？是 → 专色。
2. 否 → 是否大面积平涂且对一致性敏感？是 → 倾向专色，由打样结果裁定。
3. 否 → 四色。上机前用 Color Bridge 查看最接近的 CMYK 模拟与原专色的差距 [1][3]。差距不可接受时回到第 2 步。

### 2.3 后缀含义

同一编号加不同后缀，表示该颜色在不同纸张或不同印法下的呈现。

| 后缀 | 含义 | 所属指南或体系 | 状态 | 依据 |
|---|---|---|---|---|
| C | Coated，涂布纸 | Graphics / PMS | 现行 | [2] |
| U | Uncoated，非涂布纸 | Graphics / PMS | 现行 | [2] |
| CP | Coated 上的四色模拟 | Color Bridge Coated | 现行（旧帮助页口径） | [4] |
| UP | Uncoated 上的四色模拟 | Color Bridge Uncoated | 现行（旧帮助页口径） | [4] |
| XGC | Extended Gamut Coated，涂布纸上的七色（CMYKOGV）印刷模拟编号 | Extended Gamut Coated Guide | 现行性待核：依据为 2015 年 Pantone 新闻稿的行业媒体转载，未在 pantone.com 现行页面读到该后缀的释义 | [15] |
| CV / CVC / CVU | 早期软件中的屏幕模拟标识 | 已废止 | 废止 | [4] |
| PC / EC | 早期四色、欧洲四色模拟标识 | 已废止 | 废止 | [4] |
| M（matte） | 哑光涂布纸 | 随 2010 年 5 月 PANTONE PLUS SERIES 推出而停用 | 废止 | [4] |
| TCX / TPG | 纺织（棉）与纸面样卡 | Fashion, Home + Interiors（FHI）体系，不是印刷 Graphics 体系 | 待核：来源为 shoppantone.com FAQ，域名归属未核 | [14] |

**规则**
- 官方说明：同一潘通颜色印在涂布纸与非涂布纸上，外观差别很大，主要原因是油墨与纸张的反应 [2]。所以 C 与 U 不能互换，交付时必须写全后缀。
- CP/UP 是四色模拟，不是专色 [4]。以 CP/UP 下单，印厂印出的是 CMYK，不是专色油墨。
- 「Pantone+ / PANTONE PLUS」是 2010 年起的系列名 [4]。现行官方产品称谓以 Pantone Graphics 下的 Formula Guide、Color Bridge 等为准 [2][3][5]。文件与交付说明中不再以「Pantone+」作为版本依据。
- FHI 编号（如年度色所用的六位编号，见 §2.5）与 Graphics 的 C/U 编号属于不同体系。印刷交付须落到 Graphics 体系的带后缀编号。两套体系之间的对应关系本稿未核，不作推断。

### 2.4 色卡与打样流程

以实体色卡与打样为准。流程节点如下：

| 节点 | 做什么 | 产出 | 依据 |
|---|---|---|---|
| N1 选纸 | 先确定实际承印物是涂布还是非涂布 | 决定后缀 C 或 U | [2] |
| N2 选色 | 在对应后缀的实体 Formula Guide 上选色；屏幕只作预览 | 带后缀的专色编号 | [5][11] |
| N3 定印法 | 按 §2.2 的决策顺序确定专色、四色或 ECG；用 Color Bridge 或 Extended Gamut Guide 评估四色、七色的替代效果 | 印法说明 | [1][3] |
| N4 文件设定 | 专色色板名与交付编号一致并带后缀；不以 hex 或 RGB 交付 | 印刷文件、色彩说明 | [1] |
| N5 随墨附色卡 | 向印厂提供对应的 Pantone 色卡作参照 | 色卡或色片 | [1] |
| N6 打样与签样 | 在标准观察条件下比对样张与实体色卡，签样 | 签样 | [12]；本机第 255 行 [L1] |
| N7 上机核色 | 以签样与色卡为基准，在同一观察条件下核对 | 核色记录 | [12] |
| N8 色卡维护 | 检查色卡版本与使用时长 | 更换记录 | [5][8] |

**节点说明**
- **N2 版本**：Formula Guide 最新版收录 2,614 个专色（涂布与非涂布），其中新增 224 个 PMS 颜色 [5]。客户指定的颜色若是新增色，旧版色卡中查不到，须确认双方色卡版本一致。
- **N6、N7 光源**：印刷品目视比对的标准观察条件由 ISO 3664 规定，以 CIE 标准照明体 D50 为基础。现行 ISO 3664:2025 为第四版，取代 ISO 3664:2009，并新增了排除紫外成分的 D50 观察条件 P3/P4 [12]。办公室照明、手机屏幕都不是签样条件。
- **N6 色差预期**：官方说明，色卡上的油墨配方只是起点，实际印刷存在正常偏差；官方在色卡生产中的目标是小于 2 ΔE2000；部分基础颜料不耐光 [9]。签样应写明可接受色差由印厂与委托方约定，atlas 不预设数值。
- **N8 更换周期**：官方建议每 12–18 个月更换 Graphics 指南，原因是油墨褪色与纸张黄变 [8]。

### 2.5 年度色

- Pantone 色彩研究所（Pantone Color Institute）的趋势预测工作包括发布「年度色」（Color of the Year）[10]。官方发布时以 FHI 体系的六位编号标识 [10]，与 §2.3 的 Graphics C/U 编号不是同一体系。
- 在 atlas 中的定位：**只作趋势索引**。它说明某一年的流行叙事，不构成任何风格的判据，也不作为品牌选色依据。
- atlas 不建立年度色列表，不写任何年度色的名称、编号或色值。
- 风格条目若提到「某年流行色」，只能写在背景或趋势说明里，不得进入 §4 的色彩关系必填项。

### 2.6 与风格条目的接口

每个 `styles/*.md` 的 §4 色彩在「关系描述」之后，追加「印刷时的处理方式」子块（计划书 §5.3 第 185 行、§4 第 125 行 [L2]）。建议字段：

```yaml
print_handling:
  process: cmyk | spot | cmyk+spot | ecg | screen-only   # 该风格典型的印法；screen-only 表示该风格主要存在于屏幕
  spot_roles: []          # 需要专色的色彩角色，取值限于：brand-primary | metallic | neon | flat-large-area
  substrate: coated | uncoated | either | tbd            # 决定后缀 C / U
  suffix_rule: "编号必须带后缀；C 与 U 分别打样"
  proof: required | recommended                          # 有 spot_roles 时必须为 required
  screen_examples: "示例 hex 仅作屏幕预览，须标注「示例」"
  pantone_refs: none      # atlas 不预填色号；项目中由设计师按实体色卡指定
  risks: []               # 该风格特有的印刷风险，写一句具体原因
```

**写法约束**
- `spot_roles` 必须对应风格中真实存在的角色。例如某风格依赖荧光色块，就写 `neon`，并在 `risks` 中写明「四色无法指定荧光油墨」。不写「视情况而定」这类空泛表述。
- `pantone_refs` 恒为 `none`，理由见文首边界。
- 纯屏幕风格写 `process: screen-only`，其余字段可省略，但须写一句「若转印刷，按本模块 §2.2 重新判定」。

### 2.7 反模式

每条都针对印刷色这一环节，不作泛化。

1. **屏幕取色直接下印**：用吸管从截图、网页或 PDF 屏幕显示中取 hex，换算成 CMYK 后交付。屏幕颜色是计算机模拟 [11]，换算结果只是某一设备条件下的配方 [1]。
2. **用 hex 或 RGB 向印厂交付颜色**：色彩说明只写 hex，或在印刷文件中保留 RGB 对象，让 RIP 自行转换。这违反本机第 253 行的底线 [L1]。
3. **C/U 混用**：涂布纸封面与非涂布纸内页共用同一个带 C 后缀的编号，只打一次样。同一颜色在两种纸上外观差别很大 [2]。
4. **把 CP/UP 当专色下单**：CP/UP 是 Color Bridge 的四色模拟标识 [4]，按此下单得到的是 CMYK 叠印。
5. **把第 253 行读成「禁用专色」**：品牌主色、金属色、荧光色因此被强行转成 CMYK。第 253 行只约束四色分支，见 §1 与 §2.2。
6. **用四色数值指定金属色或荧光色**：金属与荧光在潘通体系中是专色油墨 [1][6][7]，无法用 CMYK 数值指定。
7. **旧色卡、错光源签样**：使用超过 12–18 个月、已褪色或黄变的色卡 [8]，或在非 ISO 3664 观察条件下签样 [12]。
8. **用旧版色卡检索新增色号**：新增的 224 个 PMS 颜色不在旧版 Formula Guide 中 [5]。双方版本不一致时，没有共同的比对基准。
9. **以年度色作为品牌主色依据**：年度色是趋势预测产物 [10]，且编号属于 FHI 体系。直接套用既缺乏品牌论证，也缺少 Graphics 体系的印刷编号。
10. **在 atlas 或风格条目中编制色号色值对照表**：违反本模块边界与计划书第 270 行「不收录色号数值表」。

---

## 来源

外部来源（访问日期均为 2026-09-28）：

1. Pantone, "Understanding Different Color Spaces", https://www.pantone.com/hk/en/articles/color-fundamentals/understanding-different-color-spaces 。支持以下内容：RGB/CMYK 设备相关；同一 CMYK 数值在六台印刷机上得到六种颜色；RGB/CMYK 不能定义颜色，只是配方；CIELAB 设备无关；专色定义（不经网点）及其适合标志与识别系统；专色最适合一至三色印件且成本可能更高；18 种基础油墨及授权油墨商；随墨附 Pantone 色卡；CMYK 约 55%、ECG 约 90%；CMYKOGV；Metallic/Pastel/Neon 属 PMS；Color Bridge 并列 CMYK 模拟并印 sRGB/HTML；Extended Gamut Guide 模拟 1,729 个 PMS 专色；最多七种原色墨的加色域体系。
2. Pantone Support, "What does the terms coated and uncoated mean in the Pantone Graphics System", https://support.pantone.com/en/what-does-the-terms-coated-and-uncoated-mean-in-the-pantone-graphics-system 。支持：C = coated，U = uncoated；同一颜色在两种纸上外观差别大，主要源于油墨与纸张的反应；Graphics System 称谓。
3. Pantone Support, "What is the difference between the Pantone Formula Guides and Pantone Color Bridge Guides", https://support.pantone.com/en/what-is-the-difference-between-the-pantone-formula-guides-and-pantone-color-bridge-guides 。支持：Formula Guide 与 Color Bridge 的区别及用途。
4. Pantone（日本站旧版帮助页）, "PANTONE Color Suffix differences: C, CV, CVC, CVU, CP, UP", https://www.pantone.jp/customer-service/help/?t=PANTONE-Color-Suffix-differences%3A-C%2C-CV%2C-CVC%2C-CVU%2C-CP%2C-UP 。支持：CP/UP 为 Color Bridge 四色模拟；CV/CVC/CVU、PC/EC 已废止；PANTONE PLUS SERIES 于 2010 年 5 月推出，哑光指南停用。注：此为旧版页面，现行性以 [2][3][5] 为准。
5. Pantone, "Formula Guide Coated & Uncoated"（产品页）, https://www.pantone.com/hk/en-hk/products/graphics/formula-guide-coated-uncoated 。支持：最新版收录 2,614 个专色（涂布与非涂布），含新增 224 个 PMS 颜色。
6. Pantone, "Metallics Guide"（产品页）, https://www.pantone.com/products/graphics/metallics-guide 。支持：官方单列金属色指南（页面称 655 个金属色）。
7. Pantone, "Pastels & Neons Guide Coated & Uncoated"（产品页）, https://www.pantone.com/na/en-us/products/graphics/pastels-neons-guide-coated-uncoated 。支持：官方单列粉彩与荧光指南（页面称 154 个粉彩、56 个荧光）。
8. Pantone Support, "How often should I replace my Pantone Guides", https://support.pantone.com/en/how-often-should-i-replace-my-pantone-guides 。支持：建议每 12–18 个月更换；原因是褪色与纸张黄变。
9. Pantone Support, "Normal printing process color variances explained", https://support.pantone.com/en/normal-printing-process-color-variances-explained 。支持：色卡配方只是起点；色卡生产目标小于 2 ΔE2000；部分基础颜料不耐光。
10. Pantone（新闻稿）, Color of the Year 2026 announcement, https://www.pantone.com/articles/press-releases/pantone-announces-color-of-the-year-2026-cloud-dancer 。支持：Pantone Color Institute 的趋势预测包括年度色；以 FHI 体系六位编号标识。本文不引用其名称、编号或色值。
11. Pantone Color Finder（入口页，不指向任何具体色号）, https://www.pantone.com/color-finder 。支持：页面声明「Before using, understand that the colors shown on this site are computer simulations of the PANTONE Colors and may not match PANTONE-identified color standards. Always consult PANTONE Publications to visually evaluate any result before utilization.」。该文本取自页面源码中的 disclaimer 字段（curl 取得），它在渲染页面上的显示位置未核。
12. ISO 3664:2025 *Graphic technology and photography — Viewing conditions*（iTeh 公开样章）, https://cdn.standards.iteh.ai/samples/iso/iso-3664-2025/f1c7b6b93a4a42f79e1d35a04cc9d396/iso-3664-2025.pdf ；旧版 ANSI 预览 https://webstore.ansi.org/preview-pages/ISO/preview_ISO+3664-2009.pdf 。支持：第四版取代 ISO 3664:2009；以 CIE 标准照明体 D50 为基础；新增排除紫外的 P3/P4 条件。注：iso.org 页面访问被拦截，未直接核对。
13. W3C, *CSS Color Module Level 4*, https://www.w3.org/TR/css-color-4/ 。支持：Oklab/OkLCh 及 `oklch()` 属于 CSS Color 4 定义的色彩表示。
14. Shop Pantone FAQ, https://shoppantone.com/pages/faqs 。支持：TCX（棉）/ TPG（纸，取代 TPX）为 FHI 后缀。**待核**：域名归属未经官方确认，按二手来源处理。
15. PIworld（行业媒体）转载 Pantone 2015-09-09 新闻稿 "Pantone's New Extended Gamut Guide Closes Gap Between CMYK, Spot Color", https://www.piworld.com/article/pantones-new-extended-gamut-guide-closes-gap-cmyk-spot-color-printing/ 。支持：Extended Gamut Coated Guide 中的每个颜色以 "Pantone Extended Gamut Coated (XGC) Number" 标识；七色为 CMYK 加 OGV；可覆盖约 90% 的 PMS 专色。注：此为转载的二手来源（文末注 Source: Pantone），原新闻稿在 pantone.com 上的地址未找到。

本机证据：

- [L1] `/workspace/design-style-v2/差集比对-勘误补遗-20260928.md` 第 116 行（潘通 2 行原文与出处）、第 184 行（`grep -n` 核验方式）。原始文件为 `claude-skills/marketing-skill/…/brand-identity-and-framework.md:253,255`。
- [L2] `/workspace/design-style-v2/v2-计划书.md` 第 95 行（关系优先于数值）、第 125 行（§4 色彩 schema）、第 173–188 行（§5.3 大纲与边界）、第 270 行（E4：不收录色号数值表）。
