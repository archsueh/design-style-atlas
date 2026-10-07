---
name: design-style-atlas
description: "Use when the request contains an explicit `style:` token (e.g. `style: acid`, `style: collage`, `style: halftone-duotone`, `style: international-typographic`, or method refs `style: ref/cn-type`, `style: ref/layout-decompose`, `style: ref/grid-annotate`, `style: ref/pantone`). Knowledge base for Chinese type classes, layout teardown, grid annotation, Pantone print workflow, and per-style criteria. Do not load when no `style:` token is present — default Bauhaus/Swiss path stays with existing skills."
---

# design-style-atlas

只在显式 `style:` 时启用。无声明则本文件以下全部不读。

## 激活规则

- `style: <id>` → 读 `styles/<id>.md`（`<id>` 与文件名一致）。
- 方法模块：
  - `style: ref/cn-type` → `typography/cn-type-classes.md`
  - `style: ref/layout-decompose` → `layout/decomposition-method.md`
  - `style: ref/grid-annotate` → `layout/grid-annotation.md`
  - `style: ref/pantone` → `color/pantone-print-system.md`
- `status: placeholder` 的槽（`_slot-05`…`_slot-07`）没有名字，不得当风格用。
- `exception: true`（目前仅 `acid`）只覆盖**当前请求**的评审纪律，不改 huashu 或其他文件；覆盖范围写在该条目 §9「例外通道」。

## 路由表

| token | 文件 |
|---|---|
| `style: international-typographic` | `styles/international-typographic.md` |
| `style: collage` | `styles/collage.md` |
| `style: acid` | `styles/acid.md` |
| `style: halftone-duotone` | `styles/halftone-duotone.md` |
| `style: ref/cn-type` | `typography/cn-type-classes.md` |
| `style: ref/layout-decompose` | `layout/decomposition-method.md` |
| `style: ref/grid-annotate` | `layout/grid-annotation.md` |
| `style: ref/pantone` | `color/pantone-print-system.md` |

总览：`styles/_index.md`。条目 schema：`schema/style-entry.md`。提示词供料：`prompt-export/interface.md`。第三方引用：`overlays/`。影像三项不在本库：`interfaces/imaging-grok.md`。

## 工作流（触发后）

1. 解析 `style:` 值。未知 id → 停，列出上表，不猜。
2. 读对应文件全文。风格条目再按需读 §5 指向的 `typography/cn-type-classes.md` 与 `prompt-export/tool-syntax.md`。
3. 产出必须满足该条目 §1 判据，并避开 §2 反模式。
4. 需要生图提示词时，按条目 §6 把正/负两块交给 `prompt-master` 组装；风格短语放句首还是句末查 `prompt-export/tool-syntax.md` §0.1 `art_style_position`。本库不输出成品提示词。
5. 酸性：写明「本请求局部覆盖 huashu 赛博霓虹禁区」，默认路径的其他请求不受影响。

## 不要做

- 无 `style:` 时塞进默认设计路径。
- 改第三方仓里的任何文件。
- 把 `open-design/design-systems/` 的 DESIGN.md 当风格实现。
- 收录潘通色号数值表。
