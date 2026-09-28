# 与 prompt-master 的供料契约

分工：atlas 供料，`prompt-master` 组装。atlas **不**输出成品提示词，**不**改 `prompt-master` 文件。

WorkBuddy 加载位 `~/.workbuddy-ai/skills/prompt-master` 不存在。overlay 指向 Developer 实体：

`/Users/mac/Developer/skill-libraries/prompt-master`（git HEAD `d15eabbe5d2122eedc060bae8a771381e9873d1b`）

`~/.agents/skills-master/prompt-master` 是 5 文件薄副本，不用它供料。

## 每个风格条目 §6 的 YAML

```yaml
prompt_export:
  positive:
    style: []
    mood: []
    light: []
    composition: []
  negative: []
  tools:
    midjourney: { params: "--style raw", no: [] }
    stable_diffusion: { weights: [] }
    seedream: { art_style_first: "" }
    dalle3: { prose: "" }
    flux: { prose: "", negative_as_positive: [] }
```

- `positive` 四槽按 Midjourney 习惯：风格 / 情绪 / 光线 / 构图。主体由用户请求提供，atlas 不写主体。
- `negative` 来自该条目 §2 反模式，永远单独一块。
- 与 prompt-master 铁律对齐：正向与反向永远分两块。引用写章节标题「Image AI — Generation」，不写行号。

Flux 无原生稳定反向时，把「不要 X」改写成「要 Y」放进 `negative_as_positive`。见 `tool-syntax.md`。
