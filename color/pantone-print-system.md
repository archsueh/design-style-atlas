# 潘通色体系

激活：`style: ref/pantone`

写法口径：本机**不是全空白**，是「2 行 vs 成体系」。不收录色号数值表。

## 0. 本机已有的 2 行（原样）

出处：`/Users/mac/Developer/skill-libraries/claude-skills/marketing-skill/skills/brand-guidelines/references/brand-identity-and-framework.md`

- 第 253 行：`Always use CMYK values for print production (never RGB or hex)`
- 第 255 行：`Proof against Pantone reference before bulk print runs`

另有 `claude-scholar` 设计指南与 Apple HIG `color.md` 把 CMYK 当色彩模型定义，不含专色、C/U 后缀、年度色。

下面把这 2 行扩成流程，不替代潘通官方色库。

## 1. 屏幕色与印刷色

RGB / hex / OKLCH 是自发光混色；CMYK 是油墨减色。屏幕上的近似值不能作为印刷依据。交付印厂：CMYK 和/或专色色号，外加纸张与工艺说明。不交付「截图像素的 hex」。

## 2. 四色印刷与专色

四色（CMYK）：大批量、照片、渐变。偏暗偏灰是油墨叠印的物理结果，不是调色失败。

必须考虑专色的情况：

- 品牌主色要跨批次稳定
- 金属色、荧光色、大面积平涂要「实」而不是四色仿
- 包装/Logo 需要与色卡对样

专色是额外油墨，不是「更鲜艳的 CMYK」。

## 3. 后缀含义

同一色号在不同纸上不是同一个颜色。常见公开约定：

- **C**（coated，涂布纸）：表面较亮，色更通透
- **U**（uncoated，非涂布）：偏哑、偏吸墨、饱和度下降

C 与 U 不能混用在同一规格书里当「同一个色」。其他后缀以潘通官方当时公布为准，本库不建数值表。

## 4. 色卡与打样

流程节点：

1. 在实体色卡上选定（看纸种对应的 C/U）
2. 打样（数码样 ≠ 上机样；上机样才接近批量）
3. 对样后再放批量
4. 批次间用同一张色卡和同一照明条件

「Proof against Pantone reference before bulk print runs」指的就是第 3 步，不是看屏幕。

## 5. 年度色

年度色是趋势索引，不是品牌选色依据。品牌主色不随年度色改。

## 6. 与风格条目的接口

每个 `styles/*.md` 的 §4 必须写「印刷时怎么处理」：哪些色走四色、哪些必须专色、屏幕预览如何标注「非印刷依据」。

## 7. 反模式

- 用屏幕截图取色直接下印
- 用 hex 向印厂交付
- C/U 混用当同一色
- 把年度色写进 VI 主色
- 在 atlas 或任何 skill 里粘贴潘通色号数值表
