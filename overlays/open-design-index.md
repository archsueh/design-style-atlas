# overlay · open-design 名称索引

> atlas 内的引用层，对方文件零改动。本文件须能独立阅读：假设读者所在宿主没有加载 open-design（它也没有顶层 `SKILL.md`）。
> 底稿：c61ed7d 版（151 个 `design-systems/` 名字由该版作者在 Mac 上列出）。本合并版保留名单，补齐基线口径、加载状态、反例证据、上游地址、全量名单的生成与复核方法、来源。
> 落盘时复核项：① 用下文「全量名单生成方法」重跑一次，核对 151 与本表一致；② `skills/` 139 个名字与上游地址表待填；③ open-design 自身的上游地址待读取。

对方路径：`/Users/mac/Developer/open-design`
git HEAD：`427e2eaedca5e15b9ed57e3bc1620ab6e1a767d1`
E0：`tree_sha256_12=5d0022fe602c`（hashed 4000 文件封顶）——c61ed7d 版口径
E0（`E0-预检.md` §4 口径，E10 以此为准）：tree_sha256 `1f33b7556566b63dceb3678284b10b85ffd6610029cf1f94087906348f86779c`，5176 个文件，工作区 7 处未提交改动（非本项目造成），无顶层 `SKILL.md`
结构：75 个顶层条目；`skills/` 139 项；`design-systems/` 151 个目录（463 个文件）；`design-templates/` 36 个
WorkBuddy 加载状态：**未加载**（`E0-预检.md` §3，0 命中、无入口）

**只含名字。不含任何 DESIGN.md / tokens.css / 组件 HTML 的复制。** 只取名字作命名参考，不取内容。

## 反例：标签加通用 token 不构成风格

open-design 的 `design-systems/` 看起来像风格库，实际是换名模板。证据（`差集比对-勘误补遗-20260928.md` §2.2）：`brutalism/DESIGN.md` 与 `bento/DESIGN.md` 逐行比对只差 8 处（标题、Category、一句描述、Visual style、Color stance、四个 hex、字体族、字号 Scale 标签），§4 Spacing & Grid 到 §9 Anti-patterns 逐字节相同，粗野主义没有任何特有判据；抽样 12 个风格的 primary 色，8 个同为 Tailwind blue-500 `#3B82F6`；`skills/color-expert/SKILL.md` 全文 1325 B，只有一句简介加一行 `Upstream:` 地址，是上游指针而非技能。因此 atlas 的每条风格必须自带特有的判据、反模式与排版机制，不能以「名字 + 一组 token」充数。

## design-systems/ 名单（c61ed7d 版，全量）
151 个 `design-systems/` 目录名如下，作命名索引。内容是换名模板，见 `principles.md` 第 1 条。

上游总仓（open-design 自身）：**未记录**。报告与 E0 均未给出；c61ed7d 版只写了 `https://github.com/`，不猜 org。落盘时用 `git -C /Users/mac/Developer/open-design remote -v` 或对方 README 读取后填入。

计数：151

| # | id |
|---|---|
| 1 | `_schema`（疑为模板或 schema 目录，不是设计系统，待核） |
| 2 | `agentic` |
| 3 | `airbnb` |
| 4 | `airtable` |
| 5 | `ant` |
| 6 | `apple` |
| 7 | `application` |
| 8 | `arc` |
| 9 | `artistic` |
| 10 | `atelier-zero` |
| 11 | `bento` |
| 12 | `binance` |
| 13 | `bmw` |
| 14 | `bmw-m` |
| 15 | `bold` |
| 16 | `brutalism` |
| 17 | `bugatti` |
| 18 | `cafe` |
| 19 | `cal` |
| 20 | `canva` |
| 21 | `cisco` |
| 22 | `claude` |
| 23 | `clay` |
| 24 | `claymorphism` |
| 25 | `clean` |
| 26 | `clickhouse` |
| 27 | `cohere` |
| 28 | `coinbase` |
| 29 | `colorful` |
| 30 | `composio` |
| 31 | `contemporary` |
| 32 | `corporate` |
| 33 | `cosmic` |
| 34 | `creative` |
| 35 | `cursor` |
| 36 | `dashboard` |
| 37 | `default` |
| 38 | `discord` |
| 39 | `dithered` |
| 40 | `doodle` |
| 41 | `dramatic` |
| 42 | `duolingo` |
| 43 | `editorial` |
| 44 | `elegant` |
| 45 | `elevenlabs` |
| 46 | `energetic` |
| 47 | `enterprise` |
| 48 | `expo` |
| 49 | `expressive` |
| 50 | `fantasy` |
| 51 | `ferrari` |
| 52 | `figma` |
| 53 | `flat` |
| 54 | `framer` |
| 55 | `friendly` |
| 56 | `futuristic` |
| 57 | `github` |
| 58 | `glassmorphism` |
| 59 | `gradient` |
| 60 | `hashicorp` |
| 61 | `hud` |
| 62 | `huggingface` |
| 63 | `ibm` |
| 64 | `intercom` |
| 65 | `kami` |
| 66 | `kraken` |
| 67 | `lamborghini` |
| 68 | `levels` |
| 69 | `linear-app` |
| 70 | `lingo` |
| 71 | `loom` |
| 72 | `lovable` |
| 73 | `luxury` |
| 74 | `mastercard` |
| 75 | `material` |
| 76 | `meta` |
| 77 | `minimal` |
| 78 | `minimax` |
| 79 | `mintlify` |
| 80 | `miro` |
| 81 | `mission-control` |
| 82 | `mistral-ai` |
| 83 | `modern` |
| 84 | `mongodb` |
| 85 | `mono` |
| 86 | `neobrutalism` |
| 87 | `neon` |
| 88 | `neumorphism` |
| 89 | `nike` |
| 90 | `notion` |
| 91 | `nvidia` |
| 92 | `ollama` |
| 93 | `openai` |
| 94 | `opencode-ai` |
| 95 | `pacman` |
| 96 | `paper` |
| 97 | `perplexity` |
| 98 | `perspective` |
| 99 | `pinterest` |
| 100 | `playstation` |
| 101 | `posthog` |
| 102 | `premium` |
| 103 | `professional` |
| 104 | `publication` |
| 105 | `raycast` |
| 106 | `refined` |
| 107 | `renault` |
| 108 | `replicate` |
| 109 | `resend` |
| 110 | `retro` |
| 111 | `revolut` |
| 112 | `runwayml` |
| 113 | `sanity` |
| 114 | `sentry` |
| 115 | `shadcn` |
| 116 | `shopify` |
| 117 | `simple` |
| 118 | `skeumorphism` |
| 119 | `slack` |
| 120 | `sleek` |
| 121 | `spacex` |
| 122 | `spacious` |
| 123 | `spotify` |
| 124 | `starbucks` |
| 125 | `storytelling` |
| 126 | `stripe` |
| 127 | `supabase` |
| 128 | `superhuman` |
| 129 | `tesla` |
| 130 | `tetris` |
| 131 | `theverge` |
| 132 | `together-ai` |
| 133 | `totality-festival` |
| 134 | `trading-terminal` |
| 135 | `uber` |
| 136 | `urdu` |
| 137 | `vercel` |
| 138 | `vibrant` |
| 139 | `vintage` |
| 140 | `vodafone` |
| 141 | `voltagent` |
| 142 | `warm-editorial` |
| 143 | `warp` |
| 144 | `webex` |
| 145 | `webflow` |
| 146 | `wechat` |
| 147 | `wired` |
| 148 | `wise` |
| 149 | `x-ai` |
| 150 | `xiaohongshu` |
| 151 | `zapier` |

skills/ 目录是广告位式 SKILL.md（平均约 1.3 KB），同样不复制正文。需要上游时读对方 SKILL.md 里的 URL，不在本文件展开。

## skills/ 上游地址

报告中已出现的，非全量：

| skill | 上游地址 | 可达性 |
|---|---|---|
| `color-expert` | https://github.com/meodai/skill.color-expert | HTTP 200（`curl -s -o /dev/null -w '%{http_code}' -L`，2026-09-28 20:54 CST，从 box 发起） |

其余 138 项待执行按下文命令生成后贴入下表：

| skill | 上游地址 |
|---|---|
| | |

## design-templates/ 名字

报告中已出现的，非全量：`critique`、`html-ppt-*` 系列、`finance-report`、`dashboard`（共 36 个，全量待生成）。

| template |
|---|
| |

## 全量名单生成方法（执行在 Mac 只读运行）

以下命令只读，不写对方仓库。输出贴入对应的空表。

```bash
OD=/Users/mac/Developer/open-design
# 1) design-systems 名单：应为 151 行，与上表逐行对照
ls "$OD/design-systems/" | wc -l
ls "$OD/design-systems/"
# 2) skills 名单：应为 139 行
ls "$OD/skills/" | wc -l
ls "$OD/skills/"
# 3) 上游地址：报告引用的原文格式为 `Upstream: https://...`，可能被反引号包裹，故用宽松匹配并带文件名
grep -Ho 'Upstream: https://[^ `)]*' "$OD"/skills/*/SKILL.md
# 4) design-templates 名单：应为 36 行
ls "$OD/design-templates/" | wc -l
ls "$OD/design-templates/"
# 5) open-design 自身的远端地址
git -C "$OD" remote -v
```

## 来源

本机证据（未访问 Mac）：

1. `/workspace/design-style-v2/E0-预检.md` §3、§4：不在 WorkBuddy 加载面；HEAD、未提交改动数、文件数、tree_sha256。
2. `/workspace/design-style-v2/差集比对-勘误补遗-20260928.md` §2.1：75 个顶层条目；`skills/` 139、`design-systems/` 151（463 文件）、`design-templates/` 36；品牌名与风格名示例。
3. `/workspace/design-style-v2/差集比对-勘误补遗-20260928.md` §2.2：brutalism 与 bento 只差 8 处、§4–§9 逐字节相同；12 个抽样中 8 个 primary 为 `#3B82F6`；`color-expert` 是上游指针。
4. `/workspace/design-style-v2/差集比对-勘误补遗-20260928.md` §2.3、§6 Q3：只取命名清单与上游地址，不复用内容。
5. `/workspace/design-style-v2/c61ed7d/overlays/open-design-index.md`（提交 c61ed7d）：151 个 `design-systems/` 名字，以及 c61ed7d 口径的 `tree_sha256_12`。

外部：

6. https://github.com/meodai/skill.color-expert ：box 上 curl 返回 HTTP 200（2026-09-28 20:54 CST）。
