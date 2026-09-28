---
id: collage
name_zh: 拼贴
name_en: Collage
lineage: "Pablo Picasso / Georges Braque papier collé; later graphic collage as layout method (superimposition, not one-point perspective). Not Memphis revival."
status: ready
nearest: [memphis-maximalism]
overlays: [handraw-style, huashu-design]
exception: false
---

# 拼贴

补泛化方法论。花叔只有 Memphis Maximalism（绑定复古做旧）。本条讲「叠加建空间」，不讲孟菲斯几何积木。

`handraw-style/styles_200_reorganized.md` 的 #050 Lane Smith、#064 Paul Rand、#225 OscarAI、#256 Morph 是**插画风格**参照，不是版式方法论。可看材料感，不可当网格规则抄。

## §1 判据

1. 空间层次来自图层覆盖（前景压住中景、中景压住背景），而不是一点透视消失点。
2. 至少两块来源不同的图像或纹理在边缘互相切断，切断线是设计结果不是裁切事故。
3. 全页有一种色彩关系把冲突的图绑在一起（统一色罩、统一纸底、或统一油墨套）。
4. 元素允许「撞」，但每个撞点能指出谁在上、谁在下。

## §2 反模式

1. 把许多 PNG 贴纸均匀撒在浅色底上，彼此不重叠，叫「拼贴」。
2. 冲突来自没对齐的网格，而不是被选择的切断。
3. 没有统一色机制，每张图保留自己的原色拍照白平衡。
4. 用孟菲斯三角形+波浪线冒充拼贴结构。

## §3 排版机制

结构从**叠层顺序**来，不从栏数来。先定三层（底纸 / 图像床 / 文字或图形刀口），再决定切断线。

允许打破：文字可以骑在切断线上，条件是文字仍能成句、且骑线服务于「谁压谁」。不允许：为了满而把第四、第五层无顺序堆上去。

需要读别人的成品时，仍可用九步拆分（`layout/decomposition-method.md`），但第 2 步允许结论为「无栏网格，结构是叠层」。

## §4 色彩

关系：用一套关系（邻近或单一色罩）去管住多图冲突；互补色可以用在**一层**里当撞击，不能每层一对互补。

屏幕：统一色罩可在叠层上用同一混合模式。印刷：多图建议先统一到同一纸色再专色或四色；荧光只有在明确要酸性时才出现（那是 `style: acid`，不是本条）。

示例（示例，非规范色）：底纸暖灰，图像床降饱和，刀口一层留一个强调色。

## §5 字体

中文：复古旧字体可作标题刀口；正文仍用粗黑无衬线短词，长文不要复古体（`cn-type-classes.md`）。

英文：木刻/老衬线可作切断标题；正文 Grotesque 短词。授权：OFL 的 Source Han 系列可作稳定正文；装饰复古英文字未核则标未核。

## §6 提示词出口

```yaml
prompt_export:
  positive:
    style: ["graphic collage layout", "layered cut paper", "superimposed photographs"]
    mood: ["chosen collision", "tactile paper"]
    light: ["overhead scan light", "no studio glamour"]
    composition: ["foreground overlapping midground", "cut edges", "one unifying tint"]
  negative: ["stickers evenly spaced", "Memphis squiggle pattern as structure", "one-point perspective cityscape", "no overlap"]
  tools:
    midjourney: { params: "--style raw --v 6", no: ["sticker pack", "isometric city", "neon"] }
    stable_diffusion: { weights: ["papier colle:1.2", "overlapping layers:1.2"] }
    seedream: { art_style_first: "graphic design collage, layered paper cuts" }
    dalle3: { prose: "A graphic-design collage: photographs cut and stacked, one unifying tint, type riding a cut edge." }
    flux:
      prose: "Graphic collage poster, stacked cut photographs, one unifying paper tint, type on a cut edge."
      negative_as_positive: ["overlapping layers with clear stacking order", "single unifying tint"]
```

## §7 来源与既有实现

- 拼贴作为绘画手段：Picasso / Braque papier collé（公开美术史事实）。
- 花叔 Memphis Maximalism：还原度有限且绑定孟菲斯，见 `overlays/huashu-design.md`。
- `overlays/handraw-style.md`：四条插画参照，注明非版式方法。

## §8 区分度自检

与孟菲斯最大化的差别：孟菲斯用几何积木、亮色块和复古图案**铺满**；本条用**切断与叠层顺序**建空间，色彩是绑住冲突的机制，不是积木本身。
