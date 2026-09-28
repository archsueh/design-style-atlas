# design-style-atlas

风格与版式知识库。git 根在本目录；WorkBuddy 加载位是 `~/.workbuddy-ai/skills/design-style-atlas` 软链。

**默认路径仍是 Bauhaus / Swiss。** 本库只在请求出现 `style: <id>` 时参与。

不推远端。本地 `git` 即可。

## 扫描面（固化）

查「本机有没有某项」时扫这些位置，缺 skill 根软链 ≠ 本机不存在：

1. `~/Developer`（含 `lab/`）
2. `~/Documents/Code/skill-hub`
3. 八个 skill 根：`.agents/skills`、`.agents/skills-master`、`.hermes/skills`、`.workbuddy-ai/skills`、`.claude/skills`、`.codex/skills`、`.cc-switch/skills`、`.grok/skills`

反面样本：`~/Developer/open-design` 的 151 个 `design-systems/` 是换名模板，只取其名字作索引（见 `overlays/open-design-index.md`），不复用内容。

## 更新纪律

- 新风格复制 `schema/style-entry.template.md`，八节写满后再改 `status: ready`。
- 图 1 未知的 4 个风格只占位（`styles/_slot-0N.md`），不猜名字。
- 第三方 skill 只在 `overlays/` 写引用，不改对方文件。
- 改完跑 `python3 scripts/lint_entries.py`。
- 潘通文件不收录色号数值表。
