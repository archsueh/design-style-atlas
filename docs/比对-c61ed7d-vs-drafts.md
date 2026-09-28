# 比对：c61ed7d 与 drafts（合并版写入 merged/）

> 生成：2026-09-28 21:05 CST。输入：`c61ed7d/`（提交 c61ed7d4081c，作者 Hsueh，2026-09-28 20:25 +0800，只读拷贝，30 个文件含 `_stat.txt`）；`drafts/`（第 1–3 轮稿，18 个文件）。
> 输出：`merged/`，33 个文件（并集 32 个，另加新增的 `scripts/check_yaml.py`）。c61ed7d/ 未改动；drafts/ 本轮起未再改动。
> 口径：默认「合并」，写明每个文件从哪一版取哪些节；只有一版明显较弱时才整份保留另一版，并写明弱在哪里。

## 0. 证据口径与总计数

计数均由脚本得出（`/workspace/scratch/metrics.py`、`merged/scripts/lint_entries.py`、`merged/scripts/check_yaml.py`）。

| 项 | 取法 | drafts | c61ed7d | merged |
|---|---|---|---|---|
| URL 数（全部 .md/.svg） | 正则 `https?://…` | 88 | 4 | 93 |
| 待核类标记（待核／未核／待落盘复核／待复核） | 计数 | 53 | 11 | 53 |
| 潘通色号（如 `Pantone 186 C`、`PMS 485`） | `(?i)\b(pantone\|pms)\s+\d{2,4}\s?[cu]\b` | 0 | 0 | 0 |
| `#3B82F6` | 字面 | 0 | 1（`principles.md`，作为反例证据） | 3（`principles.md` 1 次、`open-design-index.md` 反例段 2 次，均为证据引用） |
| `--style raw` 作为参数值 | styles §6 与 interface YAML | 0 | 4（3 条目 + interface） | 0 |
| `art_style_first` 作为字段 | 同上 | 3（3 条目，旧字段名） | 4 | 0 |
| `dalle3.deprecated` | 同上 | 1（interface） | 0 | 4（interface + 3 条目） |
| lint（c61ed7d 原脚本） | 在 /tmp 副本上运行 | FAIL：6 项，全为「§1/§2 需 ≥3 条编号句」（drafts 用 `- IT-1` 式 ID 列表） | PASS ready=3 | FAIL：同 drafts 的 6 项 |
| lint（merged 版脚本） | `python3 merged/scripts/lint_entries.py [ROOT]` | — | FAIL：13 项（缺 §9、`--style raw`、`art_style_first`、无 deprecated） | **PASS ready=3 unique_criteria=14 unique_anti=13** |
| YAML（frontmatter + ```yaml 块） | `check_yaml.py`（box 无 PyYAML，用内置严格子集解析） | 14 块，失败 2 | 14 块，失败 1 | **19 块，失败 0** |

已核实的本机锚点（执行 2026-09-28 在 Mac 上核实，用作「锚点是否对得上」的判据）：
- huashu `critique-guide.md` 的标题为 `## 常见设计问题 Top 10`（第 106 行）；「2.5 倍」出现在第 35、114 行。
- huashu 的国际主义变体与 Memphis 是加粗条目，不是标题。
- handraw #225 的锚点为「225 · OscarAI」（第 476 行）。
- HIG `color.md` 有 4 份副本；采用 `~/Developer/skill-libraries/antigravity-awesome-skills/skills/hig-foundations/references/color.md`。
- prompt-master 的锚点为 `### Tool Routing` 下的加粗条目 `**Image AI — Generation**`。
- 实体与基线以 `E0-预检.md` 为准：§4 为 6 仓基线，§6.1 拍板 prompt-master 用 B，§6.2 为 chinese-typography-system 的实体。

## 1. 逐文件

列说明：「来源」写 URL 数与可核性；「锚点」对照上面的核实项与 E0；「schema」只对风格条目；「潘通／#3B82F6」写是否出现；「拍板」对照三处决定：MJ 只用 `--raw`；SeeDream 用 `art_style` 加 `art_style_position`，4.0–5.0 lite 为 tail；`dalle3` 标 `deprecated: 2026-05-12`，无替代字段。

| # | 文件 | 结论 | merged 路径 | 取哪节 | 来源 | 锚点 | schema | 潘通／#3B82F6 | 拍板 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `README.md` | 仅 c61ed7d 有，可直接用 | `merged/README.md` | 全文原样 | 0 URL，内部约定 | 扫描面 8 个 skill 根与 E0 §2 一致 | — | 无 | 不涉及 |
| 2 | `SKILL.md` | 仅 c61ed7d 有，需补 2 句 | `merged/SKILL.md` | c61ed7d 全文；补「覆盖范围写在 §9 例外通道」与「风格短语位置查 tool-syntax §0.1 `art_style_position`」 | 0 URL | 路由表 7 项均有对应文件 | — | 无 | 补后不违反 |
| 3 | `principles.md` | 仅 c61ed7d 有，需补 1 处 | `merged/principles.md` | c61ed7d 全文；第 1 条改用勘误 §2.2 的证据：只差 8 处，§4–§9 逐字节相同 | 0 URL；「同为 71 行」报告未记，标待核 | — | — | `#3B82F6` 1 次，作为反例证据，合规 | 不涉及 |
| 4 | `interfaces/imaging-grok.md` | 仅 c61ed7d 有，可直接用 | `merged/interfaces/imaging-grok.md` | 全文原样 | 0 URL | box 路径 `/home/box/agent-data/workflows/{blender-camera,archviz-3d}/` 实测存在；Mac 路径未核 | — | 无 | 不涉及 |
| 5 | `schema/style-entry.md` | 合并 | `merged/schema/style-entry.md` | E1 原文（与 c61ed7d 版逐字节相同，`diff` 为空）；Frontmatter 示例块由 ```yaml 改为 ```markdown；文末加「§9 例外通道（仅限 `exception: true`）」 | 内部规范 | — | 定义 §1–§8 必填，§9 仅限 exception | 无 | 不涉及 |
| 6 | `schema/style-entry.template.md` | 仅 c61ed7d 有，需补 1 处 | `merged/schema/style-entry.template.md` | c61ed7d 全文；文末加注释「仅 exception: true 时加 `## §9 例外通道`」 | — | — | 8 节齐 | 无 | 不涉及 |
| 7 | `scripts/lint_entries.py` | 仅 c61ed7d 有，需补 | `merged/scripts/lint_entries.py` | c61ed7d 全部检查保留；改动见 §2 | — | — | 补后校验 §9 规则 | 补后检查潘通色号 | 补后校验三处拍板 |
| 8 | `styles/_index.md` | 仅 c61ed7d 有，需补 | `merged/styles/_index.md` | c61ed7d 全文；三条 status 由 ready 改为 draft，与条目 frontmatter 一致；补一句 acid §9 | — | — | — | 无 | 不涉及 |
| 9 | `styles/_slot-04.md` | 仅 c61ed7d 有，可直接用 | `merged/styles/_slot-04.md` | 原样 | — | — | placeholder，lint 通过 | 无 | 不涉及 |
| 10 | `styles/_slot-05.md` | 同上 | `merged/styles/_slot-05.md` | 原样 | — | — | 同上 | 无 | 不涉及 |
| 11 | `styles/_slot-06.md` | 同上 | `merged/styles/_slot-06.md` | 原样 | — | — | 同上 | 无 | 不涉及 |
| 12 | `styles/_slot-07.md` | 同上 | `merged/styles/_slot-07.md` | 原样 | — | — | 同上 | 无 | 不涉及 |
| 13 | `styles/acid.md` | 合并（以 drafts 为底） | `merged/styles/acid.md` | drafts：frontmatter 与 §1–§8；原位于 §1 之前的「例外通道」节移到文末，改为 `## §9 例外通道`；§6 按拍板改 | drafts 4 URL，c61ed7d 0 URL，lineage 无出处 | drafts 引 `## 常见设计问题 Top 10`，已核实；c61ed7d 只写「第 9 条」 | drafts 与 c61ed7d 都是 8 节，例外说明都不在 §9；merged 为 §1–§9，exception: true | drafts 示例 hex 4 个，均标「示例」；c61ed7d 反模式里 `#0D1117` 未标示例；无潘通色号 | c61ed7d：`--style raw --v 6`、`art_style_first`、无 deprecated，三处全违反；drafts 违反 2 处；merged 无违反 |
| 14 | `styles/collage.md` | 合并（以 drafts 为底） | `merged/styles/collage.md` | drafts §1–§8；§3 并入 c61ed7d 的「九步拆分第 2 步允许结论为『无栏网格，结构是叠层』」 | drafts 5 URL，c61ed7d 0 URL | 引用 handraw 四条，与核实一致 | 两版 8 节齐；exception: false，无 §9 | drafts 示例 hex 4 个，均标「示例」 | c61ed7d 全违反；merged 无违反 |
| 15 | `styles/international-typographic.md` | 合并（以 drafts 为底） | `merged/styles/international-typographic.md` | drafts §1–§8；§6 按拍板改 | drafts 4 URL（含 Meggs 转引），c61ed7d 0 URL | 两版都引 muller／vignelli overlay | 两版 8 节齐 | drafts 示例 hex 2 个，均标「示例」 | c61ed7d 全违反；merged 无违反 |
| 16 | `prompt-export/tool-syntax.md` | 合并（以 drafts 为底；c61ed7d 无需另取） | `merged/prompt-export/tool-syntax.md` | drafts 全文；c61ed7d 的 Flux `true_cfg_scale` 两路说法 drafts §5.2 已覆盖，且附官方引文 | drafts 24 URL，其中 21 条为官方文档；c61ed7d 2 URL，BFL 页注明「抓取失败」 | 两版都引「Image AI — Generation」；drafts 的 prompt-master 路径为 B | — | 无 | c61ed7d：MJ 例 `--style raw`，SeeDream「先写艺术风格」与 tail 相反，无 deprecated；drafts 与 merged 无违反，另有 `art_style_position` 4 处、deprecated 5 处 |
| 17 | `prompt-export/interface.md` | 合并（以 drafts 为底） | `merged/prompt-export/interface.md` | drafts 全文（第 3 轮已按拍板改）；c61ed7d 的四槽说明与铁律 drafts §2、§3 已含 | 两版 0 URL，均为本机契约 | c61ed7d 用 prompt-master A（`Developer/skill-libraries`，HEAD d15eabbe），与 E0 §6.1 拍板的 B 冲突；drafts 用 B | — | 无 | c61ed7d 违反 3 处；drafts 与 merged 无违反 |
| 18 | `typography/cn-type-classes.md` | 合并（以 drafts 为底） | `merged/typography/cn-type-classes.md` | drafts 全文；§5 末并入 c61ed7d「系统栈不等于粗黑气质」一段 | drafts 18 URL（厂商与许可证页）；c61ed7d 0 URL，判据如「横竖宽差 <30%」无出处 | 两版都引「全域 0 命中」 | — | 无 | 不涉及 |
| 19 | `typography/type-scale-sources.md` | 仅 c61ed7d 有，需补 | `merged/typography/type-scale-sources.md` | c61ed7d 全文；第 7 行 huashu 锚点改为 `## 常见设计问题 Top 10`（第 106 行，「2.5 倍」在第 35、114 行） | 0 URL；7 条本机路径 box 无法核 | 补后与核实一致 | — | 无 | 不涉及 |
| 20 | `layout/decomposition-method.md` | 合并（以 drafts 为底） | `merged/layout/decomposition-method.md` | drafts 全文；第 131 行 `step3_baseline:{` 改为 `step3_baseline: {`；c61ed7d 的九步与 drafts 同构，不另取 | drafts 2 URL；c61ed7d 0 URL | drafts 用核实行号 35、114 | — | 无 | 不涉及 |
| 21 | `layout/grid-annotation.md` | 保留 drafts | `merged/layout/grid-annotation.md` | drafts 全文。c61ed7d 较弱：773 字、无来源；图层 ID（`MB`）与 drafts 模板 SVG 的 `BOX` 不一致，合并会破坏 SVG 对应关系 | drafts 1 URL；c61ed7d 0 | — | — | 无；两版 hex 均为标注层编码色 | 不涉及 |
| 22 | `layout/templates/annotation-layer.svg` | 保留 drafts | `merged/layout/templates/annotation-layer.svg` | drafts 全文。c61ed7d 为 2048 字简模板，ID 与 grid-annotation 表不配套 | — | — | — | 无 | 不涉及 |
| 23 | `layout/example-gutenberg-b42-leaf.md` | 仅 drafts 有 | `merged/layout/example-gutenberg-b42-leaf.md` | drafts 全文；c61ed7d 的样例是不附图的类别描述 | 5 URL | 行号 35、114 已按核实改 | — | 无 | 不涉及 |
| 24 | `layout/example-gutenberg-b42-leaf.annotation.svg` | 仅 drafts 有 | `merged/layout/example-gutenberg-b42-leaf.annotation.svg` | 原样 | 6 URL | — | — | 无 | 不涉及 |
| 25 | `color/pantone-print-system.md` | 合并（以 drafts 为底） | `merged/color/pantone-print-system.md` | drafts 全文；§1 表中两处带 `…` 的路径换成 c61ed7d §0 的完整路径；补激活行 | drafts 16 URL（含 pantone.com，已标出 2 条二手来源）；c61ed7d 0 URL | HIG `color.md` 路径已按核实写明；c61ed7d 未给路径，4 份副本无法区分 | — | 两版都无潘通色号；drafts 用占位 `Pantone ### C` | 不涉及 |
| 26 | `overlays/huashu-design.md` | 合并（以 drafts 为底） | `merged/overlays/huashu-design.md` | drafts 全文（锚点已按核实改）；并入 c61ed7d 的 `SKILL.md` 62359 B；注明 c61ed7d 的 `tree_sha256_12` 与 E0 口径不同 | 0 URL；本机证据 5 条 | drafts 与核实一致；c61ed7d 无锚点 | — | 无 | 不涉及 |
| 27 | `overlays/handraw-style.md` | 合并（以 drafts 为底；c61ed7d 无独有信息） | `merged/overlays/handraw-style.md` | drafts 全文（#225 锚点「225 · OscarAI」第 476 行已核实） | 0 URL；本机证据 2 条 | drafts 与核实一致；c61ed7d 无锚点 | — | 无 | 不涉及 |
| 28 | `overlays/muller-brockmann-grid-systems.md` | 合并 | `merged/overlays/muller-brockmann-grid-systems.md` | drafts 全文；§2 并入 c61ed7d 的 PART 1 纪律／PART 2 工程节名与要点（标「复核一次」） | 0 URL；本机证据 4 条 | `SKILL.md` sha 前缀 `111da5001367` 两版一致；tree 哈希口径不同，以 E0 为准 | — | 无 | 不涉及 |
| 29 | `overlays/vignelli-canon-design-system.md` | 合并 | `merged/overlays/vignelli-canon-design-system.md` | drafts 全文；§2 并入 c61ed7d 的 Intangibles／Tangibles 节名，新增 Intangibles 一行 | 0 URL；本机证据 4 条 | `SKILL.md` sha 前缀 `c5246535bccf` 两版一致 | — | 无 | 不涉及 |
| 30 | `overlays/prompt-master.md` | 合并（以 drafts 为底） | `merged/overlays/prompt-master.md` | drafts 全文（锚点已改为 `### Tool Routing` 下 `**Image AI — Generation**`）；并入 c61ed7d 给出的 A 的 HEAD `d15eabbe…` 作备份信息 | 0 URL；本机证据 4 条 | c61ed7d 把 Image AI — Generation 写成章节标题（实为加粗条目），且以 A 供料，与 E0 §6.1 冲突 | — | 无 | 不涉及 |
| 31 | `overlays/chinese-typography-system.md` | 仅 c61ed7d 有，需补（以 c61ed7d 为底） | `merged/overlays/chinese-typography-system.md` | c61ed7d 两段原文保留；补实体与链接链、基线哈希、加载状态、要读的内容、何时送过去、不可读时的替代、边界、来源 | c61ed7d 0 条；merged 本机证据 7 条 | c61ed7d 的路径 `.agents/skills-master/…` 与 E0 §6.2 的实体 `.cc-switch/…` 不一致，merged 以 E0 为准并标待核 | — | 无 | 不涉及 |
| 32 | `overlays/open-design-index.md` | 仅 c61ed7d 有，需补（以 c61ed7d 为底） | `merged/overlays/open-design-index.md` | c61ed7d 的 151 名单全量保留；补 E0 口径基线、加载状态、反例段、`color-expert` 上游（HTTP 200）、skills 与 templates 待填表、Mac 只读生成命令、来源；删去不完整的 `https://github.com/` | c61ed7d 1 个不完整 URL；merged 5 URL，其中 1 条上游实测可达；本机证据 5 条 | c61ed7d 的 `tree_sha256_12` 为「4000 文件封顶」口径，与 E0 的 `1f33b755…`（5176 文件）不同 | — | `#3B82F6` 仅在反例段作证据 | 不涉及 |
| 33 | `scripts/check_yaml.py` | 仅 merged 有（新增） | `merged/scripts/check_yaml.py` | 新写：有 PyYAML 时用 `yaml.safe_load`，否则用内置严格子集解析 | — | — | — | — | — |

## 2. lint 脚本的改动

原脚本对 acid 的 §9 不会判失败：`main()` 只检查 8 个必需标题是否存在，不检查多余的节。它在 drafts 与 merged 上失败，是因为 `numbered_sentences()` 只认 `1. …` 格式的编号句，drafts 用的是 `- IT-1 …` 式 ID 列表。

merged 版 `merged/scripts/lint_entries.py` 相对 c61ed7d 版的改动：
1. `ROOT`：可用第一个命令行参数指定，默认仍是仓库根。
2. `numbered_sentences()`：新增正则 `ITEM`，同时接受 `1. …` 和 `- XX-n …`／`- XX-AP-n …`。
3. §9 规则写在 `main()` 中：
   - 出现 `## §9` 而 `exception` 不为 true，判失败；
   - `exception: true` 但缺 `## §9 例外通道`，判失败；
   - `section_body()` 的边界表加入 §9，避免 §8 的正文吞入 §9。
4. 三处拍板写在 `main()` 中，只检查 §6：
   - 必须有 5 个工具键；
   - 不得出现 `--style raw`；
   - 不得出现 `art_style_first`，必须是 `seedream: { art_style:`；
   - `dalle3` 必须带 `deprecated: 2026-05-12`。
5. 全文禁止潘通色号：正则 `PANTONE_CHIP`。

反向测试（在 /tmp 副本上）：给 collage 加 §9、把 IT 的 `--raw` 改回 `--style raw` 后，脚本分别报出 `§9 present but exception is not true` 和 `uses '--style raw'`。

## 3. 两份新 overlay 相对 c61ed7d 版补了什么

chinese-typography-system：
1. 实体路径改用 E0 §6.2 的 `.cc-switch/…`；c61ed7d 写的 `.agents/skills-master/…` 记为待核。
2. 补两跳链接链、非 git 仓、3 个文件、`SKILL.md` sha256、tree_sha256。
3. 补 WorkBuddy 未加载。
4. 补要读的内容：`SKILL.md` 第 1–51 行，章节标题待落盘复核。
5. 补何时送过去、不可读时的替代、边界。
6. 补 7 条本机证据。
7. 邻接技能 `font-pairing-suggester` 的路径待落盘复核。

open-design-index：
1. 补 E0 口径基线：tree_sha256、5176 个文件、7 处未提交改动、目录结构计数。
2. 补 WorkBuddy 未加载。
3. 补内联反例段：只差 8 处、§4–§9 逐字节相同、8/12 为 `#3B82F6`、color-expert 是上游指针。
4. 补 `color-expert` 上游 https://github.com/meodai/skill.color-expert（HTTP 200，2026-09-28 20:54 CST）。
5. 补 skills 上游表（其余 138 项待填）与 templates 表（36 项待填）。
6. 补 Mac 只读生成命令：`ls`、`grep -Ho 'Upstream: https://[^ `)]*'`、`git remote -v`。
7. 删除不完整的 `https://github.com/`，改为「未记录」。
8. `_schema` 标为疑似 schema 目录。
9. 补来源。

## 4. 仍待核

- c61ed7d 与 drafts 用的是两套 E0 哈希口径：c61ed7d 为 `tree_sha256_12`，并注明「4000 文件封顶」。merged 以 `/workspace/design-style-v2/E0-预检.md` 为准，E10 须用同一口径。
- chinese-typography-system 的实体路径：c61ed7d 与 E0 §6.2 不一致，落盘时用 `realpath` 核一次。
- prompt-master 用 A 还是 B：c61ed7d 用 A，E0 §6.1 拍板为 B。merged 用 B；若用户改变主意，需要同步改 interface、prompt-master overlay 与 SKILL。
- muller 的 PART 1／PART 2 与 vignelli 的 Intangibles／Tangibles 节名来自 c61ed7d 作者，E0 未独立记录，落盘时 `grep` 一次。
- YAML 校验用的是内置严格子集解析，不是 `yaml.safe_load`：box 无 PyYAML，本轮不得安装。该解析在 drafts 与 c61ed7d 上复现了已知的 2 个错误，merged 为 0 失败。有 PyYAML 的机器上运行 `python3 merged/scripts/check_yaml.py merged` 会自动改用 `safe_load`。

**总建议：以 merged/ 为落盘版本——它以 drafts 的有出处正文和已核实锚点为底，并入 c61ed7d 独有的 SKILL/README/principles/lint/槽位/type-scale、151 名单与节名，已满足三处拍板和 §9 规则，lint 与 YAML 均全绿；落盘前只需在 Mac 上复核第 4 节所列的路径与节名。**
