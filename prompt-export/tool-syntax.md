# 分工具写法差异

atlas 只供料。组装仍由 `prompt-master` 做。下列差异补 `prompt-master` 未覆盖的 Flux，并复述其对 MJ / SD / SeeDream / DALL·E 3 的既有铁律（章节「Image AI — Generation」）。

## Midjourney

逗号分隔描述符，非散文。顺序：主体（用户给）→ 风格 → 情绪 → 光线 → 构图。参数置尾，例 `--ar 16:9 --v 6 --style raw`。反向用 `--no`。

## Stable Diffusion

`(word:weight)`。CFG 常用 7–12。反向提示词强制。步数按模型习惯，不在 atlas 写死。

## SeeDream（即梦）

先写艺术风格（anime / cinematic / painterly / 本条目的风格名），再写场景。建议带反向。

## DALL·E 3

自然语言散文。把 §6 `positive` 四槽连成通顺句子；反向单独一段。

## Flux

`prompt-master` 清单无 Flux。本库补这一节。

官方文档页（落地前复核）：

- Black Forest Labs prompting guide：`https://docs.bfl.ml/guides/prompting_summary`
- Hugging Face Diffusers `FluxPipeline`：`https://huggingface.co/docs/diffusers/en/api/pipelines/flux`

Diffusers 文档（检索摘要，2026-09-28）：`negative_prompt` 存在，但 **在未使用 guidance 时被忽略**——即 `true_cfg_scale` 不大于 1 时无效。timestep-distilled 变体还要求 `guidance_scale = 0`。

因此 atlas 给 Flux 两路：

1. 调用方若显式设 `true_cfg_scale > 1`：可传 `negative_prompt`。
2. 默认（多数托管 API / 蒸馏权重）：**不要依赖反向**。把反模式改写成正向约束，填 `negative_as_positive`。例：「不要杂乱背景」→「干净的单色背景」。

BFL 官方引导页本次抓取失败（计费拦截），执行时若与上两条冲突，以 BFL 当时文档为准，并改本文件。
