# 与 prompt-master 的供料契约（interface）

> 执行卡 E7，依据计划书 §9。
> 分工：atlas 供料，prompt-master 组装。atlas 不输出成品提示词，也不改 prompt-master 的任何文件。
> prompt-master 位置：`/Users/mac/.agents/skills-master/prompt-master`（`E0-预检.md` §6.1 拍板的实体 B）。它不在 WorkBuddy 加载面内，读法见 `overlays/prompt-master.md`。
> 落盘时复核项：
> 1. prompt-master 图像段锚点已核实：`### Tool Routing` 下的加粗条目 `**Image AI — Generation**`（执行 2026-09-28 在 Mac 上核实）；
> 2. 三个风格条目 §6 已改用 `seedream.art_style`（merged 版，2026-09-28）。

---

## 1. 供料格式

每个风格条目的 §6 都必须给出下面的 YAML 块。字段名以计划书 §9 为底，只有两处按 2026-09-28 幕僚长决定修改：`seedream.art_style_first` 改名为 `seedream.art_style`；`dalle3` 增加 `deprecated` 标记。

```yaml
prompt_export:
  positive:            # 按 MJ 顺序给「风格 / 情绪 / 光线 / 构图」四槽；主体由用户请求提供，atlas 不填
    style: []
    mood: []
    light: []
    composition: []
  negative: []         # 该风格特有的反向词，来自条目 §2 反模式
  tools:
    midjourney: { params: "--raw", no: [] }
    stable_diffusion: { weights: [] }
    seedream: { art_style: "" }                       # 位置不在此处给，查 tool-syntax.md §0.1 art_style_position
    dalle3: { prose: "", deprecated: "2026-05-12" }   # 字段保留，已弃用，无替代字段
    flux: { prose: "", negative_as_positive: [] }
```

---

## 2. 字段语义与填写规则

| 字段 | 含义 | 规则 | 来源条款 |
|---|---|---|---|
| `positive.style` | 风格名与核心手法 | 英文短语；至少一项能对应条目 §1 的某条判据 | 计划书 §3 原则 2 |
| `positive.mood` | 情绪 | 只用该风格特有的情绪词，不用 beautiful、stunning 一类通用词 | 计划书 §3 原则 1 |
| `positive.light` | 光线 | 描述光的性质（平光、镜面高光等），不描述器材 | — |
| `positive.composition` | 构图 | 来自条目 §3 的「结构从哪来」 | 计划书 §4 §3 |
| `negative` | 反向词 | 每一项都能追溯到条目 §2 的某条反模式；不放 blurry、low quality 这类通用画质词（那是 prompt-master 的职责） | 计划书 §9 |
| `midjourney.params` | 置尾参数 | 默认 `--raw`，版本参数由 prompt-master 决定 | `tool-syntax.md` §1 |
| `midjourney.no` | `--no` 清单 | 只放单个名词，因为审核系统逐词读取 | `tool-syntax.md` §1 |
| `stable_diffusion.weights` | 加权短语 | `(短语:1.1–1.3)`，只给核心特征 | `tool-syntax.md` §2 |
| `seedream.art_style` | 风格短语 | 中文短语，只给内容不给位置 | `tool-syntax.md` §3 |
| `art_style_position`（不在条目内，在 `tool-syntax.md` §0.1） | 风格短语放句首还是句末 | 组装方按「工具＋版本」查表：SeeDream 4.0 / 4.5 / 5.0 lite 为 `tail`，其他见表；prompt-master 或任何组装方只读此字段，不用自身规则 | `tool-syntax.md` §0.1 |
| `dalle3.prose` | 自然语言描述 | 一到两句英文，已并入正向化的反向约束 | `tool-syntax.md` §4 |
| `dalle3.deprecated` | 弃用日期 | 固定为 `2026-05-12`；组装方须向用户说明模型已从 OpenAI API 下线，不得静默改投其他模型；不设替代字段 | `tool-syntax.md` §4 |
| `flux.prose` | 自然语言描述 | 按「主体 → 动作或状态 → 风格、光线、色彩」组织，已并入 `negative_as_positive` | `tool-syntax.md` §5.3 |
| `flux.negative_as_positive` | 反向转正向约束 | 与 `negative` 一一对应、顺序一致；不含否定词，不复述被排除元素 | `tool-syntax.md` §5.4 |

---

## 3. 与 prompt-master 铁律的对齐

prompt-master 的铁律（据报告转引）：`Always output two separate blocks: Positive Prompt and Negative Prompt. Never merge them.`（`差集比对-20260928.md` §3.1）

atlas 的对应做法：
1. `positive` 与 `negative` 始终是两个独立字段，atlas 从不在一个字段里混写正、反向内容。
2. 对不支持反向参数的工具（Flux、SeeDream、DALL·E 3），atlas 另给正向化结果（`flux.negative_as_positive`），但**不删除** `negative` 字段。prompt-master 因此仍可输出两块，铁律不被破坏。

---

## 4. 组装建议（给 prompt-master 的读者；atlas 不执行）

| 工具 | 正向块 | 反向块 |
|---|---|---|
| Midjourney | 四槽短语用逗号连接，参数置尾：`midjourney.params`、`--no` 加上 `midjourney.no` | 反向块内容与 `--no` 清单一致，作为人工核对用 |
| Stable Diffusion | 四槽短语加 `stable_diffusion.weights` | `negative` 原样送入反向字段 |
| SeeDream | 主体（用户给出）＋行为＋环境，`seedream.art_style` 按 `art_style_position` 放置（4.0 / 4.5 / 5.0 lite 放句末），再并入正向化约束 | 注明「本工具无反向参数；已由 negative_as_positive 并入正向」，并列出原 `negative` 供核对 |
| DALL·E 3（`deprecated: 2026-05-12`） | `dalle3.prose`，并提示用户该模型已下线 | 同 SeeDream |
| Flux | `flux.prose` | 同 SeeDream |

---

## 5. 与计划书 §9 的差异（已于 2026-09-28 由幕僚长定）

1. **Midjourney Raw 写法**：采纳官方现行写法 `--raw`。计划书 §9 的 YAML 行已同步修改（`v2-计划书.md` 文末有修正注记）。另注意：当前默认版本为 V8.2，`::` 多段权重官方只列到 V6.1，见 `tool-syntax.md` §1。
2. **SeeDream**：
   - 字段 `art_style_first` 改名为 `art_style`；
   - 位置规则放在 atlas 内，即 `tool-syntax.md` §0.1 的 `art_style_position`，4.0 / 4.5 / 5.0 lite 为 `tail`；
   - prompt-master 不作修改，组装方读取该字段。
   - 三个风格条目 §6 已在 merged 版改为 `art_style`，值不变。
3. **DALL·E 3**：保留 `dalle3` 字段，标记 `deprecated: 2026-05-12`，不设替代字段，见 `tool-syntax.md` §4。
4. **Flux**：计划书的判断「对反向提示词的原生支持有限」经官方核实成立。BFL 原文为「Most FLUX models do not support negative prompts」，且当前 BFL API 各模型参数中均无 `negative_prompt`，见 `tool-syntax.md` §5。

## 6. 校验（供 E8 `lint_entries.py` 实现）

- 5 个工具字段齐全；`seedream` 用 `art_style` 键，不再接受 `art_style_first`；`dalle3.deprecated` 须为 `2026-05-12`。
- `len(negative) == len(flux.negative_as_positive)`。
- `negative_as_positive` 中不出现 no、not、without、avoid、instead、free of。
- `midjourney.no` 每项为单个词。
- `positive` 四槽都不为空。

## 来源

1. `/workspace/design-style-v2/差集比对-20260928.md` §3.1：prompt-master 图像机制与铁律，转引其 `SKILL.md` 第 263–289 行（行号会漂移，以章节标题为准）。
2. `/workspace/design-style-v2/E0-预检.md` §3、§6.1：加载状态与实体 B 的拍板。
3. `/workspace/design-style-v2/v2-计划书.md` §9：契约原文。
4. 各工具官方文档：见 `tool-syntax.md` 的「来源」一节第 1–16 条（访问日期 2026-09-28），本文件不重复列出。
