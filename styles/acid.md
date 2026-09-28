---
id: acid
name_zh: 酸性设计
name_en: Acid Graphics
lineage: "1960s psychedelia → late-1980s/1990s Acid House naming → 2000s lull → 2010s digital revival (Acid Graphics). Not generic cyber-neon UI."
status: ready
nearest: [cyber-neon]
overlays: [huashu-design]
exception: true
---

# 酸性设计

`exception: true`。只在 `style: acid` 下生效。本条在**当前请求内**局部覆盖 huashu `critique-guide`「赛博霓虹滥用」禁区第 9 条。不修改 huashu 任何文件。无 `style: acid` 时该禁区仍在。

## §1 判据

1. 底是近黑或深色，主色是高饱和荧光（粉/绿/黄/蓝里至少两色成套），不是单根霓虹描边。
2. 图形语言至少占下列之一且贯穿全页：几何线框、液态熔融、镭射/金属流、可见 glitch 位移。
3. 排版有一处故意不对齐、挤压或重叠，且该处仍可读关键词。
4. 第一眼刺激先于「好看」：远距能感到攻击性，近距仍能指出主信息。

## §2 反模式

1. 退化为深蓝底 `#0D1117` 加一层霓虹发光描边，其余仍是普通卡片布局。
2. 多色是默认彩虹节点，没有成套关系（看不出哪两色在对话）。
3. 全页不可读：重叠把主标题吃掉且没有第二阅读层。
4. 用酸性皮肤套在瑞士网格海报上，网格纪律与荧光两套同时成立、互相取消。

## §3 排版机制

结构从**反网格的节奏**来：先定一条故意破坏的轴（斜切、重叠字、错位重复），再把其余信息收进仍可读的层。

允许打破：对齐、字距、甚至正文字向。不允许打破：主信息完全消失、或回到普通 UI 卡片栅格却声称酸性。

与拼贴不同：拼贴的冲突是层叠切断；酸性的冲突是光学刺激与失真。

## §4 色彩

关系：高饱和、高明度差。常用互补或分裂互补（例：品红对绿，再加一黄作分裂）。多色必须成套：能数出 2–4 个主荧光，而不是 8 个随机色。

屏幕：允许发光与 glitch。印刷：荧光需专色或接受四色变灰；交付必须写「屏幕预览非印刷依据」（`color/pantone-print-system.md`）。不要把年度色当荧光系统。

示例（示例）：黑底 + 品红 + 酸绿；第三色只用在一处 glitch。

## §5 字体

中文：粗黑无衬线的最重档作被扭曲的标题；不要新中式毛笔，不要铅印做旧（那是复古型）。

英文：尖锐、倾斜或被扭曲的无衬线 display；正文若需要可读，另用 Grotesque 短词，不把花体铺满。授权：可变 OFL 黑体可变形；专用酸性英文字体未核则标未核。

## §6 提示词出口

```yaml
prompt_export:
  positive:
    style: ["acid graphics", "psychedelic rave poster", "liquid metal type"]
    mood: ["aggressive", "carnival", "subcultural"]
    light: ["blacklight", "laser"]
    composition: ["intentional misalignment", "glitch offset", "wireframe overlay"]
  negative: ["navy dashboard UI", "single neon outline on cards", "Swiss grid poster", "readable corporate landing page"]
  tools:
    midjourney: { params: "--style raw --v 6", no: ["corporate website", "navy dashboard", "subtle beige"] }
    stable_diffusion: { weights: ["acid graphics:1.3", "glitch:1.1"] }
    seedream: { art_style_first: "acid graphics, neon psychedelic poster" }
    dalle3: { prose: "An acid-graphics poster: near-black field, two fluorescent colors as a set, liquid-metal type, one readable headline despite overlap." }
    flux:
      prose: "Acid graphics poster, black field, magenta and acid-green as a set, liquid metal type, one glitch offset, headline still readable."
      negative_as_positive: ["fluorescent color set of two to four hues", "near-black field", "one readable headline"]
```

## §7 来源与既有实现

- 公开设计史脉络：迷幻平面 → Acid House 命名 → 数字复兴（Acid Graphics）。
- 花叔禁区：`overlays/huashu-design.md` 指向 `critique-guide`「赛博霓虹滥用」。本条覆盖范围仅当前请求。
- `easy-vibe` 文档有一行「酸性设计」关键词表，只作命名先例，不是方法论。

## §8 区分度自检

与赛博霓虹的差别：赛博霓虹是**深色 UI 上的发光描边与网格 HUD**；酸性是**荧光成套 + 失真图形语言 + 故意破坏的排版**，刺激优先于界面可用。只有描边发光、没有成套荧光与失真，判为赛博霓虹，不是本条。
