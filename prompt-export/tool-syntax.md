# 分工具写法差异（tool-syntax）

> 执行卡 E7。本文件规定 atlas 为 5 个图像工具供料时的写法依据，并补上 prompt-master 缺失的 Flux 一节（计划书 §9）。atlas 只供料，成品提示词由 prompt-master 组装，见 `interface.md`。
> 核验日期：2026-09-28。每条语法都标出处，凡官方文档未写明的，一律标「官方未写明」或「待核」，不作推断。
> 落盘时复核项：
> 1. 各工具版本变化快，落盘当日须重开 [1]–[16] 核对；
> 2. prompt-master 原文口径（CFG、步数、SeeDream「先写风格」）须在 `/Users/mac/.agents/skills-master/prompt-master/SKILL.md` 中按章节标题复核，见 `overlays/prompt-master.md`。

---

## 0. 总表

| 工具 | 反向提示词的官方机制 | 权重语法 | atlas 字段 | 与计划书 §9 的差异 |
|---|---|---|---|---|
| Midjourney | `--no`，效果等同于多段提示中权重为 −0.5 的一段 [2] | `::` 多段权重，官方写明仅适用于 V1–V6.1 [3] | `midjourney.params`、`midjourney.no` | Raw 模式的现行写法是 `--raw` [4]；计划书 §9 已于 2026-09-28 由 `--style raw` 改为 `--raw` |
| Stable Diffusion | 独立的反向提示词：WebUI 有专门字段 [6]；Stability API 与 diffusers 有 `negative_prompt` 参数 [7][8] | `(word:1.5)` 是 AUTOMATIC1111 WebUI 语法 [6]；diffusers 须借助外部库 [8] | `stable_diffusion.weights` | 一致；须注明权重语法依赖所用前端 |
| SeeDream | 官方 API 请求参数中没有反向提示词字段 [10] | 官方未写明 | `seedream.art_style`，位置查 `art_style_position` | 字段已改名（原 `art_style_first`）；4.0 / 4.5 / 5.0 lite 为 `tail` [9]，见 §0.1、§3 |
| DALL·E 3 | 官方参数中没有反向提示词字段 [12] | 官方未写明 | `dalle3.prose`，`deprecated: 2026-05-12` | 字段保留，标记已弃用，不设替代字段 [11]，见 §4 |
| Flux | BFL 官方：「Most FLUX models do not support negative prompts.」[13]；当前 BFL API 各模型参数中均无 `negative_prompt` [15] | BFL 官方未写明；diffusers 文档称权重对 Flux 类模型未必有效 [8] | `flux.prose`、`flux.negative_as_positive` | 核实结果与计划书的判断一致，见 §5 |


## 0.1 风格短语位置：`art_style_position`

**用途**
- 风格短语放在提示词句首（`head`）还是句末（`tail`），由本表按「工具＋版本」给出，是 atlas 自己的字段。
- prompt-master 属第三方，不作修改。prompt-master 或任何组装方只需读取本字段，把风格短语放到对应位置，不再沿用自身的「先写艺术风格」规则。
- 取值只有 `head` 和 `tail`。凡无官方依据的，一律写 `待核` 或 `不适用`，不作推断。

```yaml
art_style_position:          # 组装方按「工具 + 版本」查表；没有列出的版本按「待核」处理
  seedream:
    "4.0": tail              # [9] 官方指南：先写主体＋行为＋环境，再补风格；正例风格位于句末
    "4.5": tail              # [9]
    "5.0-lite": tail         # [9]
    "5.0-pro": 待核          # [10] API 已支持该模型，但 [9] 正文只写明覆盖 5.0 lite、4.5、4.0
    "5.0-flash": 待核        # 同上
  flux:
    all: tail                # [13b] BFL 统一提示词指南：先写清主体，再写动作或状态，再补情绪、环境与视觉方向；指南未逐模型区分
  midjourney:
    all: 待核                # 本轮读取的官方页面 [1]–[5] 只规定参数置尾，未规定正文中风格词的位置；prompt-master 的「主体→风格→…」是其自身规则，非官方
  stable_diffusion:
    all: 待核                # [6][8] 未规定风格词位置
  dalle3:
    all: 不适用              # deprecated: 2026-05-12 [11]；atlas 直接给整句 prose，不单独给风格短语
```

**依据摘录**
- SeeDream：《Seedream 4.0-5.0 提示词指南》正文首句写明覆盖 Seedream 5.0 lite、4.5、4.0。通用规则第 1 条要求先写「主体＋行为＋环境」，再补充风格、色彩、光影、构图；官方正例「……走在林荫道上，莫奈油画风格。」风格位于句末 [9]。
- Flux：BFL「Building a Good Prompt」建议先写清主体，再加动作或状态，最后在确有帮助时补充情绪、环境与视觉方向 [13b]。

---

## 1. Midjourney

**官方状态**：当前默认版本为 V8.2，2026-07-24 起成为默认 [5]。

**写法要点**（均引自官方文档）
- 参数一律放在提示词末尾：与正文之间留一个空格，参数内部不加逗号、句号等标点，参数之后不再写正文 [1]。
- 反向提示用 `--no`，后接一个或多个元素，多个元素用逗号分隔，例如 `--no fruit, apple, pear` [2]。
- 官方把「without any fruit」「please don't add fruit」列为反例 [2]，所以反向内容不要写进正文。
- 审核系统会把 `--no` 后的每个词单独读取。官方示例：`--no modern clothing` 会被读成「no modern」和「no clothing」，可能触发警告 [2]。因此 `midjourney.no` 里只放单个名词，不放「形容词＋名词」短语。
- `--no` 等同于多段提示中权重为 −0.5 的一段 [2]。
- 多段提示以 `::` 分段，`::` 左侧不留空格、右侧留一个空格。它只适用于 V1、2、3、4、Niji 4、5、Niji 5、6、Niji 6、6.1 [3]。负权重允许使用，但所有权重之和必须为正 [3]。V7 以上是否支持，官方页面未列出，atlas 不供 `::` 权重料。
- Raw 模式的写法是 `--raw`，兼容 V5.1 及以后版本 [4]。旧写法 `--style raw` 在 V8.2 是否仍被接受，官方 Raw 页未写，**待核**。

**atlas 字段映射**
- `midjourney.params`：默认 `"--raw"`。
- `midjourney.no`：取自 §2 反模式的单名词清单。
- 正文四槽按「风格 / 情绪 / 光线 / 构图」给出，不放参数（契约见 `interface.md`）。

---

## 2. Stable Diffusion

**写法要点**
- **权重（AUTOMATIC1111 WebUI 语法）** [6]：
  - `(word)` 提高 1.1 倍，`((word))` 提高 1.21 倍，`[word]` 降低 1.1 倍；
  - `(word:1.5)` 指定倍数，`(word:0.25)` 降至四分之一；
  - 只有 `()` 能指定数值，`[]` 不能；字面括号用反斜杠转义。
  - 这是社区广泛使用的 WebUI 仓库文档，不是 Stability AI 的官方规范。
- **diffusers**：管线本身不解析上述括号语法，须通过 `prompt_embeds` 传入加权嵌入，官方文档推荐 sd_embed 或 Compel 库 [8]。给 diffusers 用户供料时，须注明「权重语法需外部库」。
- **反向提示词**：
  - WebUI 的反向提示词在采样中用作无条件条件（unconditional conditioning），替代空字符串 [6]。
  - diffusers 的 SD 系列管线通过 `negative_prompt` 与 `guidance_scale` 生效 [8]。
  - Stability AI 的 Stable Image Core 接口有 `negative_prompt` 参数，最长 10,000 字符 [7]。该条引自 AWS Bedrock 的模型参数文档；Stability 自家的 API 参考页是动态页面，本轮未能读取。
- **CFG 7–12、步数 20–30 / 40–50、反向提示必填**：这是 prompt-master 原文的口径（`差集比对-20260928.md` §3.1），本轮未对照官方文档复核，atlas 不改写这些数值，也不另给。

**atlas 字段映射**
- `stable_diffusion.weights`：用 `(短语:数值)` 格式，数值限定在 1.1–1.3，只给该风格的核心特征。
- 反向词用 `negative` 顶层字段，由 prompt-master 放进反向块。

---

## 3. SeeDream（火山引擎 Seedream 4.0–5.0）

**官方状态**：图片生成 API 覆盖 Seedream 5.0 pro、5.0 flash、5.0 lite、4.5、4.0 [10]。

**写法要点**（官方提示词指南 [9]、API 文档 [10]）
- 用简洁连贯的自然语言，写明「主体＋行为＋环境」。如对美学有要求，再用自然语言或短语补充风格、色彩、光影、构图 [9]。
  - 官方正例：「一个穿着华丽服装的女孩，撑着遮阳伞走在林荫道上，莫奈油画风格。」风格短语位于句末 [9]。
  - 官方反例是碎片化的词组堆叠 [9]。
- 有明确应用场景时，写明图像用途和类型 [9]。
- 需要渲染的文字放在双引号中 [9]。
- 有明确风格需求时，用精准的风格词，或提供参考图 [9]。
- 字数：中文不超过 300 字，英文不超过 600 词。过长会导致细节被忽略 [10]。
- 请求体参数为 `prompt`、`image`、`size`、`optimize_prompt_options`、`output_format`、`response_format`、`sequential_image_generation`、`stream`、`tools`、`watermark`、`model` 等，**没有反向提示词字段** [10]。

**atlas 字段映射**（2026-09-28 按幕僚长决定修订）
- `seedream.art_style`：风格短语，中文。原字段名 `art_style_first` 已改为 `art_style`，因为名称本身隐含「句首」。
- 位置不由字段名决定，而查 §0.1 的 `art_style_position`：4.0、4.5、5.0 lite 为 `tail` [9]；5.0 pro、5.0 flash 为 `待核`。
- prompt-master 写的「先指定艺术风格，再写场景」与官方指南相反。prompt-master 不作修改，组装时以本字段为准。
- 反向内容先用 `flux.negative_as_positive` 转成正向约束，再并入正文（见 `interface.md` §4）。

---

## 4. DALL·E 3

**官方状态**
- OpenAI 于 2025-11-14 通知：DALL·E 模型快照将于 **2026-05-12** 从 API 移除，推荐替代为 `gpt-image-2`、`gpt-image-1`、`gpt-image-1-mini` [11]。
- 模型页现写明「DALL·E 3 has been deprecated and removed from the API」[11]。
- ChatGPT 内是否仍可使用，本轮**未核**。

**写法要点**（DALL·E 3 时期的官方说明 [12]）
- 用自然语言详细描述。API 会先用 GPT-4 改写所有提示词再交给 DALL·E 3，官方称详细提示词效果明显更好 [12]。
- 参数包括 `style`（`vivid` / `natural`）与 `quality`（`standard` / `hd`）[12]。其中 natural 风格更接近写实，适合 logo、库存照片一类需求 [12]。
- 官方列出的参数中没有反向提示词字段 [12]。反向内容须转成正向描述写进正文。
- 当前 OpenAI 图像生成指南说明，经 Responses API 调用图像工具时，主模型也会自动改写提示词，改写结果见 `revised_prompt` 字段 [16]。

**atlas 字段映射**
- `dalle3.prose`：一到两句完整英文，包含该风格的判据性特征。反向内容按 `negative_as_positive` 的规则改写后并入。
- `dalle3.deprecated: 2026-05-12`（2026-09-28 按幕僚长决定）：字段保留，标记为已弃用，依据 [11]。不设替代字段。
- 组装方遇到 `deprecated` 时，应向用户说明该模型已从 OpenAI API 下线，不要静默改投其他模型。

---

## 5. Flux（Black Forest Labs）

### 5.1 官方怎么说反向提示词（逐字引用）

BFL 官方提示词指南「Technical Parameters」页「Working Without Negative Prompts」一节 [13]：

> "Most FLUX models do not support negative prompts. Even when they can process them, AI models generally struggle with negation — writing *"a person without glasses"* causes the model to focus on "glasses" and often generate exactly what you were trying to avoid."

同节给出的替代方法（Replacement Strategy）分三步 [13]：
1. 识别不想要的元素，例如 *no crowds*；
2. 问那个位置会看到什么；
3. 用正向描述写出来，例如 *peaceful solitude*、*empty pathways*。

同节还有替换对照表，例如 "no text" → "clean surfaces", "unmarked", "blank"；"no colors" → "monochrome", "black and white", "grayscale" [13]。

### 5.2 分模型核实

| 模型 | 官方 API 请求参数中有无 `negative_prompt` | 其他官方陈述 | 结论 |
|---|---|---|---|
| FLUX.1 [dev] | 无。参数为 prompt、image_prompt、width、height、steps、prompt_upsampling、seed、guidance、safety_tolerance、output_format 等 [15] | 模型卡：以 guidance distillation 训练 [14]，未提反向提示词 | 官方 API 不提供；模型卡未写明 |
| FLUX.1 [schnell] | BFL API 参考中没有该模型的页面 [15] | 模型卡：以 latent adversarial diffusion distillation 训练，1–4 步出图 [14]，未提反向提示词 | 官方未写明，**待核** |
| FLUX.1 [pro]（初代） | 当前 BFL API 参考未列出 [15] | — | 官方未写明，**待核** |
| FLUX1.1 [pro] | 无 [15] | — | 官方 API 不提供 |
| FLUX1.1 [pro] ultra | 无。有 `raw` 参数，但它不是反向提示词 [15] | — | 官方 API 不提供 |
| FLUX.1 Kontext [pro] / [max] | 无。参数为 prompt、input_image、aspect_ratio 等 [15] | 模型卡（Kontext [dev]）：guidance distillation [14]，未提反向提示词 | 官方 API 不提供 |
| FLUX.2 [pro] / [max] / [flex] / [klein] | 无 [15] | — | 官方 API 不提供 |

**BFL 之外的实现（非官方，只作说明）**
- Hugging Face diffusers 文档称，在 Flux 等较新模型上，经典 CFG 通常以 `true_cfg_scale` 配合 `negative_prompt` 实现：当 `true_cfg_scale > 1` 且提供了 `negative_prompt` 时，反向提示词才生效 [8]。
- 这是第三方推理库的实现方式，不是 BFL 对模型能力的声明。atlas 不据此给 Flux 供反向词。

**权重**
- BFL 指南未写明任何权重语法，**待核**。
- diffusers 文档称，提示词加权对已经紧密遵循提示词的 Flux 类模型未必有帮助 [8]。
- 所以不给 Flux 供 `(word:1.2)` 式权重。

### 5.3 正向写法要点

- 按官方建议先写清主体，再写动作或状态，最后在确有帮助时补充情绪、环境与视觉方向 [13b]。
- 官方给出的组件包括 image type、subject、location、style、camera、lighting、colors、effect、additional elements [13b]。
- FLUX.2 支持最长 32K token 的提示词，但官方建议从短写起，只加改变画面的内容 [13b]。

### 5.4 `negative_as_positive` 转换规则（atlas 自定，依据 [13] 的替代方法）

1. **一一对应**：`negative` 中每一项必须在 `flux.negative_as_positive` 中有且只有一条对应的正向约束，顺序一致，便于 lint 检查。
2. **写「那里是什么」，不写「那里没有什么」**：正向约束描述占据该位置或该属性的内容。禁止出现 no、without、not、avoid、free of、instead of 等否定或对照词，也不要复述被排除的元素名，因为官方指出点名反而会引出该元素 [13]。
3. **具体到本风格**：约束必须用本风格的判据语言，不写「clean」「high quality」这类通用词。例如：
   - 拼贴的「clean die-cut stickers」→「hand-cut paper edges with visible paper thickness」；
   - 酸性的「neon glow and bloom」→「flat matte fluorescent color fields」。
4. **并入位置**：转换后的约束写进 `flux.prose` 对应的组件位置（背景约束放在 location / colors，字形约束放在 style），而不是附在句尾当清单。
5. **与 prompt-master 铁律的关系**：prompt-master 仍然输出两块。Flux 的反向块写明「本工具无反向参数；已由 negative_as_positive 并入正向」，并列出原反向词以便人工核对，但不把它发给 Flux（见 `interface.md` §4）。
6. **同样适用于 SeeDream 与 DALL·E 3**：两者的官方参数中同样没有反向提示词字段 [10][12]。

---

## 来源

访问日期均为 2026-09-28。

1. Midjourney Docs, "Parameter List", https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List 。支持：参数置尾、空格与标点规则；参数全表中 Raw 写作 `--raw`。
2. Midjourney Docs, "No", https://docs.midjourney.com/hc/en-us/articles/32173351982093-No 。支持：`--no` 用法与逗号分隔；正文否定写法为反例；审核系统逐词读取；等同于 −0.5 权重。
3. Midjourney Docs, "Multi-Prompts & Weights", https://docs.midjourney.com/hc/en-us/articles/32658968492557-Multi-Prompts-Weights 。支持：`::` 分段与空格规则；适用版本 V1–V6.1（含 Niji 4–6）；负权重与总和为正的要求。
4. Midjourney Docs, "Raw", https://docs.midjourney.com/hc/en-us/articles/32634113811853-Raw-Mode 。支持：`--raw` 写法；兼容 V5.1 及以后。
5. Midjourney Docs, "Version", https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version 。支持：当前默认 V8.2，2026-07-24 起成为默认。
6. AUTOMATIC1111/stable-diffusion-webui Wiki, "Features"（Attention/emphasis、Negative prompt 两节）, https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features 。支持：括号权重语法与数值；反向提示词作为无条件条件。社区仓库文档，非 Stability 官方。
7. AWS Bedrock 用户指南, "Stable Image Core request and response", https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-diffusion-stable-image-core-text-image-request-response.html 。支持：Stable Image Core 的 `negative_prompt` 参数，最长 10,000 字符。注：Stability 自家 API 参考为动态页，本轮未读到。
8. Hugging Face diffusers 文档源文件, "Prompting"（weighted_prompts.md）, https://github.com/huggingface/diffusers/blob/main/docs/source/en/using-diffusers/weighted_prompts.md 。支持：SD 管线的 `negative_prompt` 与 `guidance_scale`；Flux 在 `true_cfg_scale > 1` 时反向提示词才生效；权重须借助 sd_embed 或 Compel；权重对 Flux 类模型未必有效。
9. 火山引擎文档, 《Seedream 4.0-5.0 提示词指南》（最近更新 2026-05-11）, https://www.volcengine.com/docs/82379/1829186 。支持：主体＋行为＋环境，再补风格、色彩、光影、构图；风格短语放在句末的正例；应用场景、双引号文字、风格词或参考图。
10. 火山引擎文档, 《图片生成 API》（最近更新 2026-09-22）, https://www.volcengine.com/docs/82379/1541523 。支持：覆盖的模型版本；请求参数清单（无反向提示词字段）；中文 300 字、英文 600 词的字数建议。
11. OpenAI API 文档, "Deprecations", https://developers.openai.com/api/docs/deprecations ；模型页 "DALL·E 3", https://developers.openai.com/api/docs/models/dall-e-3 。支持：2025-11-14 通知，dall-e-2 与 dall-e-3 于 2026-05-12 从 API 移除，推荐替代模型；模型页的下线说明。
12. OpenAI Cookbook, "What's new with DALL·E-3?", https://github.com/openai/openai-cookbook/blob/main/articles/what_is_new_with_dalle_3.mdx 。支持：API 以 GPT-4 改写提示词；`style`（vivid / natural）与 `quality`（standard / hd）参数；natural 风格的适用场景。
13. Black Forest Labs Docs, "Technical Parameters"（Working Without Negative Prompts）, https://docs.bfl.ml/guides/prompting_unified_technical.md 。支持：「Most FLUX models do not support negative prompts」原文；替代方法与替换对照表。
    - 13b. 同站 "Building a Good Prompt", https://docs.bfl.ml/guides/prompting_unified_building.md 。支持：主体、动作、情绪的顺序建议；提示词组件表；FLUX.2 支持 32K token。
    - 文档索引见 https://docs.bfl.ai/llms.txt 。
14. Hugging Face 模型卡（Black Forest Labs）, https://huggingface.co/black-forest-labs/FLUX.1-dev 、https://huggingface.co/black-forest-labs/FLUX.1-schnell 、https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev 。支持：dev 与 Kontext dev 以 guidance distillation 训练；schnell 以 latent adversarial diffusion distillation 训练、1–4 步出图；三份模型卡公开部分均未提及反向提示词。
15. Black Forest Labs API 参考（OpenAPI 页面）, 例如 https://docs.bfl.ml/api-reference/models/generate-an-image-with-flux1-[dev].md 、https://docs.bfl.ml/api-reference/models/generate-an-image-with-flux11-[pro].md 、https://docs.bfl.ml/api-reference/models/edit-or-create-an-image-with-flux1-kontext-[pro].md 、https://docs.bfl.ml/api-reference/models/generate-or-edit-an-image-with-flux2-[pro].md 。支持：逐页检索 llms.txt 所列 30 个 API 参考页，任何图像模型的请求参数中均无 `negative_prompt`。唯一命中「negative」的是 outpaint 页的「偏移量可为负值」，与提示词无关。
16. OpenAI API 文档, "Image generation", https://developers.openai.com/api/docs/guides/image-generation 。支持：经 Responses API 调用图像工具时主模型自动改写提示词，结果见 `revised_prompt`。
