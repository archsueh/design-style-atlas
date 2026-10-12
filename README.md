# design-style-atlas

风格与版式知识库。git 根在本目录；WorkBuddy 加载位是 `~/.workbuddy-ai/skills/design-style-atlas` 软链。

**默认路径仍是 Bauhaus / Swiss。** 本库只在请求出现 `style: <id>` 时参与。

远端：`archsueh/design-style-atlas`（public，建仓 2026-10-07）。推 `main` 与特性分支。

（2026-09-28 原记「不推远端。本地 `git` 即可。」；建远端后该约定作废。）

## 扫描面（固化）

查「本机有没有某项」时扫这些位置，缺 skill 根软链 ≠ 本机不存在：

1. `~/Developer`（含 `lab/`）
2. `~/Documents/Code/skill-hub`
3. 八个 skill 根：`.agents/skills`、`.agents/skills-master`、`.hermes/skills`、`.workbuddy-ai/skills`、`.claude/skills`、`.codex/skills`、`.cc-switch/skills`、`.grok/skills`

反面样本：`~/Developer/open-design` 的 151 个 `design-systems/` 是换名模板，只取其名字作索引（见 `overlays/open-design-index.md`），不复用内容。

## 更新纪律

- 新风格复制 `schema/style-entry.template.md`，八节写满后再改 `status: ready`。
- 图 1 未知的风格只占位（`styles/_slot-0N.md`），不猜名字。`_slot-04` 已于 2026-09-30 由用户提供的样张定名为 `halftone-duotone`，余 `_slot-05`…`_slot-07`。
- 第三方 skill 只在 `overlays/` 写引用，不改对方文件。
- 改完跑 `python3 scripts/lint_entries.py`；CI（`.github/workflows/ci.yml`）会自动跑 `check_yaml.py` + `lint_entries.py`。
- 潘通文件不收录色号数值表。

## 加条目时容易踩的四个坑（2026-09-30 补）

1. **§6 有一条 lint 没实现的成文契约**：`len(negative) == len(flux.negative_as_positive)`（写在 `prompt-export/interface.md` §6）。lint 不查，得自己对齐。
2. **从样张倒推的条目**：具体 hex 与网角**不可照抄**（JPEG 色度二次采样）。未核实项必须落进 §7，宁缺勿猜。取证方法见 `screenshot-forensics` skill。
3. **占用 `_slot-0N` 要同步三处**：`README.md` 的槽位说明、`SKILL.md` 的「placeholder 槽」行与路由表、`styles/_index.md`；然后删掉槽文件本身。
4. **历史记录里的计数不要改成新数字**：「当时 3 个条目」是带日期的决策记录，改成「4」等于篡改。要改就写成「当时 3 条；现 N 条同样适用」。
