# overlay · chinese-typography-system

> atlas 内的引用层，对方文件零改动。本文件须能独立阅读：假设读者所在宿主没有加载该技能。
> 底稿：c61ed7d 版（7 行）。本合并版保留其全部判断，补齐实体路径、链接链、基线、加载状态、读法、边界与来源。
> 落盘时复核项：① `SKILL.md` 的章节标题（报告只写「第 1–51 行」），**待落盘复核**；② c61ed7d 版写的路径 `/Users/mac/.agents/skills-master/chinese-typography-system` 与 `E0-预检.md` §6.2 记录的实体不一致，落盘时用 `ls -la` 与 `realpath` 核一次；③ 邻接技能 `font-pairing-suggester` 的路径，**待落盘复核**。

对方路径：`/Users/mac/.cc-switch/skills/chinese-typography-system`（实体，按 `E0-预检.md` §6.2）
对方管：字体栈、字号、行高、字重、字距、跨平台渲染。不管气质分类。零改对方文件。

## 1. 对方在哪里、是否被加载

| 项 | 值 |
|---|---|
| 实体 | `/Users/mac/.cc-switch/skills/chinese-typography-system`（3 个文件，非 git 仓，HEAD 不适用） |
| 链接链 | `/Users/mac/.agents/skills/chinese-typography-system` →（readlink）`/Users/mac/.hermes/skills/chinese-typography-system` →（realpath）`/Users/mac/.cc-switch/skills/chinese-typography-system` |
| `SKILL.md` sha256 | `489b8684ce2cb0697d998a86b7d5850efa03f2c12313fd0ddb828f72359a0398` |
| tree_sha256 | `223155a9080f31708f6312515fc0339e5b75cb6ff05b08c94ef0ac8d93fb6083` |
| 链接状态 | 正常，链尾落到实体（files=3），不属于 `.agents` ↔ `.hermes` 互指的断链 |
| WorkBuddy 加载状态 | **未加载**（技能列表缓存命中 0 次，无入口） |
| c61ed7d 版写法 | `/Users/mac/.agents/skills-master/chinese-typography-system`：E0 未记录该路径，与上面的实体不一致，待核 |

**读法**：按绝对路径直接打开 `/Users/mac/.cc-switch/skills/chinese-typography-system/SKILL.md`。

## 2. 要读的内容

| 内容 | 位置 | 读它做什么 | 复核状态 |
|---|---|---|---|
| 渲染参数：字体栈、字号、行高、字重、字距 | `SKILL.md` 第 1–51 行（报告实读范围） | 确定中文正文与标题的渲染参数 | 章节标题**待落盘复核**；行号会漂移，只作定位参考 |

## 3. atlas 在其上补什么

`typography/cn-type-classes.md` 的三型 × 场景。渲染稳定性仍听对方；选哪一型听 atlas。系统栈 PingFang / YaHei / Noto Sans CJK 是稳定无衬线，不是三型里的「粗黑气质」自动等价。

补充：
- cn-type-classes 另给代表字体的授权状态，以及「三型各配哪类西文」一层。
- 具体字体配对交给 `font-pairing-suggester`（路径待落盘复核）。

## 4. 何时把读者送过去

- 已选定三型中的某一型，需要落到具体的字体栈、字号、行高、字重、字距时。
- **不送过去**：还在决定「用哪种气质的中文字体」时。这一步读 `typography/cn-type-classes.md`。

## 5. 对方不可读时的最小替代

- 只按 cn-type-classes 的场景矩阵选型。渲染参数标「未定，待 chinese-typography-system 可读后补」，不自行编参数。

## 6. 边界

- 不修改、不复制对方文件。
- E10 复核实体的 `tree_sha256` 未变。

## 来源

本机证据（未访问 Mac，以下均为预检与报告记录）：

1. `/workspace/design-style-v2/E0-预检.md` §3：不在 WorkBuddy 加载面（0 命中、无入口）。
2. `/workspace/design-style-v2/E0-预检.md` §6.2：两跳链接链、实体路径、非 git、3 个文件、`SKILL.md` sha256、tree_sha256。
3. `/workspace/design-style-v2/差集比对-20260928.md` §2 第 8 行：`chinese-typography-system` 管渲染稳定性，不管气质分类。
4. `/workspace/design-style-v2/差集比对-20260928.md` §5.3：链接链 `.agents → .hermes → .cc-switch` 可通（files=3）。
5. `/workspace/design-style-v2/差集比对-20260928.md` 附表：`SKILL.md` 第 1–51 行实读，内容为字体栈、字号、行高、字重、字距，无气质分类。
6. `/workspace/design-style-v2/差集比对-勘误补遗-20260928.md` §1.1（链接 OK、0 断链）与 §3 第 8 项（只管渲染参数，不管气质分类）。
7. `/workspace/design-style-v2/c61ed7d/overlays/chinese-typography-system.md`（提交 c61ed7d）：本文件底稿，含系统栈不等于粗黑气质的判断。
