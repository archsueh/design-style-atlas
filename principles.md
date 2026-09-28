# 设计原则

1. **标签加通用 token 等于没有风格。** 反面样本是 `open-design`：`brutalism/DESIGN.md` 与 `bento/DESIGN.md` 同为 71 行，差异集中在标题、分类、一句描述、标签和若干 hex；§4 Spacing 到 §9 Anti-patterns 共用同一套通用条款。12 个风格抽样里 8 个 primary 是 Tailwind `#3B82F6`。每条 atlas 风格必须写出只属于它的判据、反模式、排版机制，由 `scripts/lint_entries.py` 机检句子不重复。

2. **判据必须可检验。** 写成看图能答「是 / 否」的句子。禁止「有张力」「很高级」。

3. **关系优先于数值。** 色彩写关系与印刷/屏幕条件；字体写分类与场景。一组 hex 或一个字体名不能代表一套风格。

4. **不重复既有实现。** 国际主义已有 `muller-brockmann-grid-systems`、`vignelli-canon-design-system`。atlas 只写总览入口与区分句，内容走 overlay。

5. **默认路径不动。** 无 `style:` 声明时，Bauhaus / Swiss 仍是默认审美。atlas 不改既有 skill。

6. **不照搬二手原文。** 只取设计史事实与公开方法论。小红书等图文只作选题线索。

7. **不猜。** 用户没给名字的风格保留占位槽。
