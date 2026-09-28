# 字体层级模数出处汇总

P2：不新写体系。只指向本机已有实现，并给出与海报模数写法 A / A4 / A8 / A24 的**对应关系**（不是等价证明）。

图 2 的 A 体系：大标题 = A，次要 = A/4，内容 = A/8，辅助 = A/24。这是**单一尺寸的比例切分**，和 UI 的模块化 type scale（1.125 / 1.2 / 1.25…）不是同一套数，只作对照。

| # | 路径 | 采用的比例或模数 | 适用场景 | 与 A/A4/A8/A24 |
|---|---|---|---|---|
| 1 | `/Users/mac/Developer/instatic/docs/reference/design-tokens.md`（549 行） | 流体 `--text-3xs`…`--text-7xl`（约 8px→56px） | 管理端 UI | A≈`--text-5xl+`；A/4≈`--text-l`–`--text-xl`；A/8≈`--text-s`；A/24 无对应（小于 `--text-3xs`） |
| 2 | `/Users/mac/Developer/skill-libraries/claude-skills/markdown-html/skills/design-system/references/design_token_canon.md` | 设计 token 正典（字号为 token 而非海报模数） | 文档站 / 设计系统 | 无 A 切分；层级靠 token 名 |
| 3 | `/Users/mac/Developer/skill-libraries/claude-skills/markdown-html/skills/design-system/references/typography_pairing.md` | `typography.scale_ratio` 默认 1.25（大三度）；另列 1.125 / 1.2 / 1.333 / 1.5 | 长文 HTML | 连续等比，不是 A 的 1/4 切分 |
| 4 | `/Users/mac/Developer/skill-libraries/claude-skills/marketing-skill/skills/brand-guidelines/references/brand-identity-and-framework.md` | 品牌应用分层（Web/Email/Social/Print），无数字模数 | 品牌规范 | 无 |
| 5 | `/Users/mac/Developer/skill-libraries/antigravity-awesome-skills/plugins/antigravity-bundle-web-designer/skills/mobile-design/mobile-typography.md` | 移动端字号建议 | 手机 UI | A 过大；正文≈A/8 量级 |
| 6 | `/Users/mac/.agents/skills-master/vignelli-canon-design-system/SKILL.md` | **两档字号**（two-size type scale） | 标识/编辑/导视 | 接近「A vs 正文」，没有 A/4、A/8、A/24 四档 |
| 7 | huashu `critique-guide` / `slide-decks`（章节标题，不写行号） | 校验：标题≥正文 2.5 倍；3–4 层级 | PPT/页 | 2.5× 接近「A 对正文」，不是 4/8/24 |

本机「模数比例制」已存在，缺的是海报那套 A 切分的生成侧。需要 A 切分时：选定 A（主标题字号），再算 A/4、A/8、A/24，并限制总档数 ≤4。不要另造第五套 scale。
