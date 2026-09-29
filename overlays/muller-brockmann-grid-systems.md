# overlay · muller-brockmann-grid-systems

> atlas 内的引用层，对方文件零改动。本文件须能独立阅读：假设读者所在宿主没有加载该技能。
> 落盘时复核项：
> 1. 3 个文件的准确文件名（本轮只确认其中有 `SKILL.md`）；
> 2. 网格生成器、Puppeteer 验证、grid-toggle 各在哪个文件。**待落盘复核**。
> 3. `SKILL.md` 分 PART 1（纪律）与 PART 2（工程）两部分：节名取自 c61ed7d 版 overlay（作者在 Mac 上写成），E0 未独立记录，落盘时 `grep -n "PART"` 复核一次。

## 1. 对方在哪里、是否被加载

| 项 | 值 |
|---|---|
| 实体 | `/Users/mac/.agents/skills-master/muller-brockmann-grid-systems`（3 个文件，含 `SKILL.md`） |
| 解析路径 | `~/.agents/skills/muller-brockmann-grid-systems` → `../skills-master/muller-brockmann-grid-systems`（链接正常） |
| 所在 git 仓 | `/Users/mac/.agents/skills-master`，HEAD `c1d7f2cf…` |
| `SKILL.md` sha256 | `111da5001367407aed0911643b78310ff941d38b9632a144cbdb364d5eedc4c9` |
| tree_sha256 | `d5dcf796e6ee70a2cbabaa23925d4dc0d635fd246f3316c229c9627fa324824f` |
| WorkBuddy 加载状态 | **已挂**（2026-09-29）：`~/.workbuddy-ai/skills/muller-brockmann-grid-systems` → skills-master 实体。列表是否出现仍按 R1 |

出处：`E0-预检.md` §3、§4；`差集比对-勘误补遗-20260928.md` §1.1。

**读法**：按绝对路径直接打开 `/Users/mac/.agents/skills-master/muller-brockmann-grid-systems/SKILL.md`，再按其中的指引找到另外两个文件。

## 2. 要读的内容

| 内容 | 位置 | 读它做什么 | 复核状态 |
|---|---|---|---|
| 真模块网格的定义与参数 | `SKILL.md` PART 1 纪律（模块网格、基线、齐左、一色强调） | 为 `styles/international-typographic.md` §3 提供网格的「结构从哪来」 | 节名见 c61ed7d 版，复核一次 |
| scaffold 生成器 | 3 个文件之一，文件名待落盘复核 | 生成自己作品的网格骨架 | 待落盘复核 |
| Puppeteer 验证（报告称可验证 0px 贴合） | 同上 | 验证自己的页面是否贴合网格 | 待落盘复核 |
| grid-toggle 叠层 | 同上 | 在开发中显示自己页面的网格 | 待落盘复核 |
| 工程纪律：overlay 必须与内容同盒；字墨对齐不等于字框对齐；scaffold + Puppeteer 0px | `SKILL.md` PART 2 工程 | `styles/international-typographic.md` §2 反模式的出处对照 | 节名与要点取自 c61ed7d 版，复核一次 |

功能清单来自 `差集比对-20260928.md` §2 第 1、7 行，是该报告实读 frontmatter 后的记录。

## 3. atlas 在其上补什么

| muller-brockmann 负责 | atlas 负责 |
|---|---|
| 生成并验证**自己的**网格 | 读出**别人的**网格：`layout/decomposition-method.md` 9 步拆分 |
| grid-toggle：开发时显示网格 | `layout/grid-annotation.md`：把测量结果画成带数值的标注叠层（固定图层色码与标签格式） |
| — | `styles/international-typographic.md`：只写可测判据和与默认路径的区分句，不重写网格理论 |

## 4. 何时把读者送过去

- 读者已经用 atlas 拆出别人的网格，并想用在新作品上：拆分表经人工确认后，交给本技能生成与验证（流程见 `layout/grid-annotation.md` §5）。
- 读者请求 `style: international-typographic`，并需要真正的网格参数与验证手段。
- **不送过去**：只做案例分析或教学标注时，atlas 自足。

## 5. 对方不可读时的最小替代

- 只用 atlas 的拆分表和标注 SVG 交付分析结果，不交付「可用的网格规范」。
- 在输出中注明「网格生成与验证未执行」。

## 6. 边界

- 不修改该技能任何文件，不调用其脚手架。
- E10 复核 `tree_sha256` 未变。

## 来源

本机证据（本轮未访问 Mac，以下均为报告与预检记录）：

1. `/workspace/design-style-v2/E0-预检.md` §3、§4：加载状态、文件数、哈希。
2. `/workspace/design-style-v2/差集比对-20260928.md` §2 第 1、7 行与附表：真模块网格、scaffold 生成器、Puppeteer 验证、grid-toggle。
3. `/workspace/design-style-v2/差集比对-勘误补遗-20260928.md` §1.1：`~/.agents/skills` 链接正常。
4. `/workspace/design-style-v2/c61ed7d/overlays/muller-brockmann-grid-systems.md`（提交 c61ed7d，作者 Hsueh，2026-09-28 20:25）：PART 1 / PART 2 节名与要点。
