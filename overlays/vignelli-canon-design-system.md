# overlay · vignelli-canon-design-system

> atlas 内的引用层，对方文件零改动。本文件须能独立阅读：假设读者所在宿主没有加载该技能。
> 落盘时复核项：
> 1. 2 个文件的准确文件名（本轮只确认其中有 `SKILL.md`）；
> 2. `SKILL.md` 分 Intangibles（语义、纪律、得体、永恒）与 Tangibles（网格、六种基本字体、两档字号、白空间、主色作识别）：节名取自 c61ed7d 版 overlay，E0 未独立记录，落盘时 `grep -n "Tangibles"` 复核一次。

## 1. 对方在哪里、是否被加载

| 项 | 值 |
|---|---|
| 实体 | `/Users/mac/.agents/skills-master/vignelli-canon-design-system`（2 个文件，含 `SKILL.md`） |
| 解析路径 | `~/.agents/skills/vignelli-canon-design-system` → `../skills-master/vignelli-canon-design-system`（链接正常） |
| 所在 git 仓 | `/Users/mac/.agents/skills-master`，HEAD `c1d7f2cf…` |
| `SKILL.md` sha256 | `c5246535bccf39baaca74f532f3fc895d878c1eb1b5619cf6eebbbd4d0bdcf52` |
| tree_sha256 | `5a38ac93c80a9dfaacb48f20ec48128754f7a8cf62b292ed1292bf90b8ae241f` |
| WorkBuddy 加载状态 | **未加载**（缓存命中 0 次） |

出处：`E0-预检.md` §3、§4；`差集比对-勘误补遗-20260928.md` §1.1。

**读法**：按绝对路径直接打开 `/Users/mac/.agents/skills-master/vignelli-canon-design-system/SKILL.md`。

## 2. 要读的内容

| 内容 | 位置 | 读它做什么 | 复核状态 |
|---|---|---|---|
| 网格 | `SKILL.md` Tangibles 部分 | `styles/international-typographic.md` §3 的第二个结构来源 | 节名见 c61ed7d 版，复核一次 |
| 六字体限定 | 同上 | `styles/international-typographic.md` §5 选英文字族时的纪律参照 | 节名见 c61ed7d 版，复核一次 |
| 二级字号制（two-size type scale） | 同上 | 与 `layout/decomposition-method.md` 步骤 4「层级」对照；也是 P2 `typography/type-scale-sources.md` 第 6 行的出处 | 节名见 c61ed7d 版，复核一次 |
| 白空间 | 同上 | 与拆分步骤 6「留白」对照 | 节名见 c61ed7d 版，复核一次 |
| Intangibles：语义、纪律、得体、永恒 | `SKILL.md` Intangibles 部分 | `styles/international-typographic.md` §8 区分句的背景 | 取自 c61ed7d 版，复核一次 |

四部分的内容概括来自 `差集比对-20260928.md` §2 第 1、6 行与附表，是报告实读 frontmatter 后的记录；Intangibles / Tangibles 节名合并自 c61ed7d 版 overlay。

## 3. atlas 在其上补什么

- atlas 不重写 Vignelli 体系。国际主义条目只写可测判据（`styles/international-typographic.md` §1），以及与默认 Bauhaus 路径的区分句（§8）。
- atlas 提供读别人作品时的层级计数与倍率记录方法（拆分步骤 4），Vignelli 提供自己作品的字号规定。前者是测量，后者是规范，两者不混用。

## 4. 何时把读者送过去

- 请求 `style: international-typographic`，并需要成套的字体与字号纪律时。
- 汇总字体层级模数（P2，E6）时，把二级字号制列为出处之一。
- **不送过去**：只做拆分或标注时。

## 5. 对方不可读时的最小替代

- 国际主义条目 §5 只保留分类层面的写法（Lineal，Neo-grotesque），不给具体的字体数量与字号规定。
- 在输出中注明「Vignelli 纪律未读取」。

## 6. 边界

- 不修改该技能任何文件。
- E10 复核 `tree_sha256` 未变。

## 来源

本机证据（本轮未访问 Mac，以下均为报告与预检记录）：

1. `/workspace/design-style-v2/E0-预检.md` §3、§4：加载状态、文件数、哈希。
2. `/workspace/design-style-v2/差集比对-20260928.md` §2 第 1、6 行与附表：网格、六字体、二级字号、白空间。
3. `/workspace/design-style-v2/差集比对-勘误补遗-20260928.md` §1.1：`~/.agents/skills` 链接正常。
4. `/workspace/design-style-v2/c61ed7d/overlays/vignelli-canon-design-system.md`（提交 c61ed7d）：Intangibles / Tangibles 节名与要点。
