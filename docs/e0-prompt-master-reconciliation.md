# E0 prompt-master 预检冲突 — 调和记录（2026-09-28）

## 冲突
两份 E0 预检对 prompt-master 的权威实体认定不一致：
- **Mac 侧** `design-style-atlas-E0-预检-20260928.json`（line 9）：overlay 指向 Developer 实体 `~/Developer/skill-libraries/prompt-master`（git HEAD `d15eabbe5d2122eedc060bae8a771381e9873d1b`），并称 skills-master 的 5 文件薄副本「不作为供料对象」。
- **/workspace 侧** E0 预检 §6.1：定 `~/.agents/skills-master/prompt-master` 为 B。

## 事实核对
A = `~/Developer/skill-libraries/prompt-master`（27 文件）与 B = `~/.agents/skills-master/prompt-master`（5 文件薄副本）`diff` 仅 1 行 `description` 差异，Image-AI 段逐字节相同 → **功能等价**。

## 裁定（Jev 决策 C，conf 0.53，2026-09-28）
- 两份预检记录为**等价**，注明功能同一性。
- 合并版 `b9d06dd` 实际采用 **B**（`~/.agents/skills-master/prompt-master`），与 /workspace 预检一致。
- atlas overlay `overlays/prompt-master.md` 继续引用 B；因 A/B 功能等价，内容无差异，无需改代码。
