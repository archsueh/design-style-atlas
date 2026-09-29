# overlay · prompt-master

> atlas 内的引用层，对方文件零改动（计划书 §2、§9）。本文件须能独立阅读：假设读者所在宿主没有加载 prompt-master。
> 已核实（执行 2026-09-28 在 Mac 上核实）：图像段锚点为 `### Tool Routing` 下的加粗条目 `**Image AI — Generation**`。
> 落盘时复核项：
> 1. 各文件名；
> 2. 实体 B 的 `tree_sha256` 与下表是否一致。

## 1. 对方在哪里、是否被加载

| 项 | 值 |
|---|---|
| 引用的实体（B，已拍板） | `/Users/mac/.agents/skills-master/prompt-master`（5 个文件，含 `SKILL.md`） |
| 所在 git 仓 | `/Users/mac/.agents/skills-master`，HEAD `c1d7f2cfae0c5880c106a1ae5370ef69fa6d7584` |
| B 的 `SKILL.md` sha256 | `39cf239bd730dd9f8c7ee41636f22b78df95afa5bfd6215fd9933e426db0dc2b` |
| B 的 tree_sha256 | `ea665cbc5999e0275707400a24e5525b15bd75da3d3e576a8d1fa8f03b90aeba` |
| 备份 A（不引用） | `/Users/mac/Developer/skill-libraries/prompt-master`，`SKILL.md` sha256 `b85718374d27bbada453791af92b7ae0b3256e5552d2f3f9d940ca4183131e4b`，与 B 内容已分叉。注意：c61ed7d 版 overlay 与 interface 以 A 为供料对象（git HEAD `d15eabbe5d2122eedc060bae8a771381e9873d1b`），与 `E0-预检.md` §6.1 拍板的 B 冲突；本合并版按拍板用 B |
| 备份 cc-switch（不引用） | `/Users/mac/.cc-switch/skills/prompt-master`，与 B 逐字节相同 |
| WorkBuddy 加载状态 | **已挂**（2026-09-29）：`~/.workbuddy-ai/skills/prompt-master` → `~/.agents/skills-master/prompt-master`（与 agents 同实体 B）。列表是否出现仍按 R1，不改 WB 配置。Developer 副本 A 仍不引用 |

以上均出自 `E0-预检.md` §3、§4、§6.1、§6.3。

**读法**：加载位已挂到实体 B。新开 WorkBuddy 会话看列表有没有；没有则停，不改 WB 配置。也可按绝对路径打开 `/Users/mac/.agents/skills-master/prompt-master/SKILL.md`。

## 2. 要读的章节

| 文件 | 章节 | 定位方法 | 读它做什么 | 复核状态 |
|---|---|---|---|---|
| `/Users/mac/.agents/skills-master/prompt-master/SKILL.md` | 图像生成工具写法段（覆盖 Midjourney、DALL-E 3、Stable Diffusion、SeeDream） | 在 `### Tool Routing` 下找加粗条目 `**Image AI — Generation**`；辅助锚点：铁律原句 `Always output two separate blocks` | 取 prompt-master 的组装顺序与铁律 | 锚点已核实。报告称位于第 263–289 行，行号会漂移，不作引用依据 |
| 同上 | 文件第 4 行附近的图像能力声明 | 查看 frontmatter 或开头描述 | 确认其工具清单不含 Flux | 待落盘复核 |

## 3. 对方已有什么（据报告转述，供未加载时参考）

来源：`差集比对-20260928.md` §3.1。

- **Midjourney**：逗号分隔的描述符，不写散文；顺序为主体 → 风格 → 情绪 → 光线 → 构图；参数置尾；反向用 `--no`。
- **Stable Diffusion**：`(word:weight)` 语法；CFG 7–12；反向提示词强制；步数 20–30 或 40–50。
- **SeeDream（即梦）**：先指定艺术风格，再写场景。
- **铁律**：正向、反向永远分两块输出，不合并。
- **工具清单**：MJ / DALL-E 3 / SD / SeeDream，**没有 Flux**。

## 4. atlas 在其上补什么

1. **风格料**：每个 `styles/*.md` 的 §6，按 `prompt-export/interface.md` 的契约提供正向四槽、反向词和分工具字段。
2. **Flux 一节**：`prompt-export/tool-syntax.md` §5，含 BFL 官方原文、分模型核实表和 `negative_as_positive` 规则。
3. **官方文档核实后的三处差异**（不改 prompt-master，只在 atlas 内记录）：
   - Midjourney Raw 的现行写法是 `--raw`；
   - SeeDream 官方指南的顺序是先写主体、行为、环境，再补风格；
   - DALL·E 3 已于 2026-05-12 从 OpenAI API 下线。
   详见 `tool-syntax.md` §1、§3、§4。

## 5. 何时把读者送过去

- **读者要成品提示词时**：先读本风格条目 §6 取料，再打开 prompt-master 的图像段（§2 表）按它的规则组装。atlas 不组装。
- **目标工具是 Flux 时**：prompt-master 没有这一节，改读 `prompt-export/tool-syntax.md` §5，再回到 prompt-master 套用两块输出。
- **不用送过去**：只做风格判断或评审、不产出提示词时。

## 6. 对方不可读时的最小替代

如果路径失效或文件无法打开：
1. 按 `prompt-export/interface.md` §4 的组装建议，直接用条目 §6 的字段拼出两块。
2. 在输出中注明「prompt-master 未读取，按 atlas 契约最小组装」。
3. 不自行补 CFG、步数等 prompt-master 独有的参数。

## 7. 边界

- 不修改、不复制 prompt-master 的文件。
- 引用写章节标题或定位锚点，不写行号。
- E10 复核实体 B 的 `tree_sha256` 未变。

## 来源

本机证据（本轮未访问 Mac，以下均为报告与预检记录）：

1. `/workspace/design-style-v2/E0-预检.md` §3、§4、§6.1、§6.3：WorkBuddy 未加载；实体 B 的拍板；A、B 与 cc-switch 副本的哈希。
2. `/workspace/design-style-v2/差集比对-20260928.md` §3.1：prompt-master 图像机制与铁律（转引其 `SKILL.md` 第 263–289 行），以及工具清单中没有 Flux。
3. `/workspace/design-style-v2/v2-计划书.md` §9：供料契约与引用稳定性要求。
4. `/workspace/design-style-v2/c61ed7d/overlays/prompt-master.md`（提交 c61ed7d）：A 的 git HEAD `d15eabbe…`；该版把 A 作为供料对象，本合并版未采纳（见 §1）。
