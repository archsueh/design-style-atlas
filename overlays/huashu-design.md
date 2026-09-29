# overlay · huashu-design

> atlas 内的引用层，对方文件零改动。本文件须能独立阅读：假设读者所在宿主没有加载 huashu-design。
> 已核实（执行 2026-09-28 在 Mac 上核实）：`critique-guide.md` 标题为 `## 常见设计问题 Top 10`（第 106 行）；第二处「2.5 倍」在第 114 行（报告原写 116）；5 个国际主义变体与 Memphis Maximalism 是加粗条目，不是标题。
> 落盘时复核项：① 「AI 生图专用风格」节名；② 第 9 条所在行（报告称第 148–151 行）。

## 1. 对方在哪里、是否被加载

| 项 | 值 |
|---|---|
| 实体（最全） | `/Users/mac/.agents/skills-master/huashu-design`（2858 个文件，含 `node_modules`） |
| 所在 git 仓 | `/Users/mac/.agents/skills-master`，HEAD `c1d7f2cf…`；工作区原有 41 处未提交改动，非本项目造成 |
| tree_sha256 | `519e1ffc7e938b2a032040790d0b5628b3213537ab97f9d27ea7537dc900a4e8` |
| `SKILL.md` 大小 | 62359 B（取自 c61ed7d 版 overlay） |
| 其他副本 | `~/.cc-switch/skills/huashu-design`、`~/.grok/skills/huashu-design`（各 90 个文件，不引用） |
| WorkBuddy 加载状态 | **已挂**（2026-09-29）：`~/.workbuddy-ai/skills/huashu-design` → `~/.agents/skills-master/huashu-design`。列表是否出现仍按 R1，不改 WB 配置。`huashu-md-html` 是另一个包 |

以上出自 `E0-预检.md` §3、§4 与 `差集比对-20260928.md` §4.2、§5.2。

**读法**：按绝对路径直接打开下表中的文件。

## 2. 要读的文件与章节

| 文件（绝对路径） | 章节 / 定位锚点 | 读它做什么 | 复核状态 |
|---|---|---|---|
| `/Users/mac/.agents/skills-master/huashu-design/references/critique-guide.md` | `## 常见设计问题 Top 10`（第 106 行）下第 9 条，锚点：搜索「赛博霓虹滥用」 | `styles/acid.md` 例外通道所覆盖的条款原文 | 标题已核实；第 9 条行号报告称第 148–151 行 |
| 同上 | 字号校验：标题 ≥ 正文 2.5 倍、3–4 个层级；锚点：搜索「2.5 倍」 | `layout/decomposition-method.md` 步骤 4 的评审侧对照 | 已核实：第 35 行与第 114 行 |
| `/Users/mac/.agents/skills-master/huashu-design/references/design-styles.md`（370 行） | 5 个国际主义变体（加粗条目，非标题），锚点：搜索加粗文本 **Editorial Brutalism**、**Swiss Monochrome**、**Neo-Swiss Billboard Editorial**、**Institutional Swiss Minimal**、**Functional Brutalism** | `styles/international-typographic.md` 的既有实现入口 | 已核实为加粗条目 |
| 同上 | 加粗条目 **Memphis Maximalism**（孟菲斯复古拼贴最大化，还原度 72%） | `styles/collage.md` §8 的对照对象 | 已核实为加粗条目 |
| 同上 | §「AI 生图专用风格」表，共 9 种被排除项 | 了解 huashu 明确不做纯 HTML 还原的范围 | 节名来自报告原文 |

## 3. 对方已有什么（据报告转述）

- **40 种风格**：约 10 种有设计史血统，约 30 种是当代产品、网页、PPT 风格配方（`差集比对-20260928.md` §1）。
- **禁区第 9 条「赛博霓虹滥用」**：深蓝底加霓虹色发光效果，被列为默认审美禁区，且是最大的 cliché 之一（同上 §1.4）。
- **没有**独立的酸性条目、泛化的拼贴方法、印刷色体系，也没有版式拆分方法（同上 §2）。

## 4. atlas 在其上补什么

| huashu 已有 | atlas 补充 |
|---|---|
| 5 个国际主义变体 | 薄条目 `styles/international-typographic.md`：可测判据，以及与默认 Bauhaus 路径的区分句 |
| Memphis Maximalism | `styles/collage.md`：泛化拼贴方法，并与孟菲斯划界 |
| 禁区第 9 条 | `styles/acid.md`：只在 `style: acid` 下局部覆盖，且保留「深蓝底加发光」为失败判据 |
| 字号校验（评审侧） | `layout/decomposition-method.md`：读别人版式的 9 步拆分 |

## 5. 何时把读者送过去

- 评审一个未声明 `style:` 的设计：用 huashu `critique-guide.md` 的原规则，atlas 不参与。
- 声明了 `style: acid`：先读 `styles/acid.md` 的例外通道，再读 huashu 第 9 条原文，确认覆盖范围。
- 需要当代产品或网页风格配方（Linear 风、Stripe 风等）：直接去 `design-styles.md`，atlas 不收录这类配方（计划书 §13 R9）。

## 6. 对方不可读时的最小替代

- 第 9 条的内容以本文件 §3 的转述为准，并在输出中注明「huashu 原文未读取」。
- 不凭记忆补写 huashu 的其他条款。

## 7. 边界

- 不修改 huashu 任何文件。
- E10 复核 `tree_sha256` 未变。

## 来源

本机证据（本轮未访问 Mac，以下均为报告与预检记录）：

1. `/workspace/design-style-v2/E0-预检.md` §3、§4：加载状态、HEAD、tree_sha256、未提交改动数。
2. `/workspace/design-style-v2/差集比对-20260928.md` §1、§1.4、§2、§4.2、§5.2 与附表：40 种风格的归档；第 9 条原文转述（`critique-guide.md` 第 148–151 行）；字号校验（报告写第 35、116 行，执行核实第二处为第 114 行）；副本拓扑。
3. `/workspace/design-style-v2/差集比对-勘误补遗-20260928.md` §1.1：断链已修复，实体 2858 个文件。
4. 执行 2026-09-28 在 Mac 上的锚点核实：`## 常见设计问题 Top 10` 第 106 行；「2.5 倍」第 35、114 行；国际主义变体与 Memphis 为加粗条目。
5. `/workspace/design-style-v2/c61ed7d/overlays/huashu-design.md`（提交 c61ed7d）：`SKILL.md` 62359 B。该版的目录哈希写作 `tree_sha256_12=e12af6440ebe`，与本文件采用的 E0 值 `519e1ffc…` 不同，原因是两版 E0 的哈希口径不同（c61ed7d 版另一 overlay 注明「hashed 4000 文件封顶」）；E10 以 `E0-预检.md` §4 的口径为准。
