---
name: design-style-atlas
description: 风格与版式知识库，仅在请求中显式出现 `style: <id>` 时启用。风格条目用 `style: <id>`（例 `style: acid`），方法模块用 `style: ref/<id>`（`ref/cn-type`、`ref/layout-decompose`、`ref/grid-annotate`、`ref/pantone`）。未出现 `style:` 时不参与，默认 Bauhaus / Swiss 路径不变。
---

# design-style-atlas

## 激活规则

- 只有请求中出现 `style: <id>`（例：`style: acid`）才加载对应 `styles/<id>.md`。
- 方法模块同样走显式前缀 `style: ref/<id>`：
  - `style: ref/cn-type` → `typography/cn-type-classes.md`
  - `style: ref/layout-decompose` → `layout/decomposition-method.md`
  - `style: ref/grid-annotate` → `layout/grid-annotation.md`
  - `style: ref/pantone` → `color/pantone-print-system.md`
- 未出现 `style:` 时 atlas 不参与；默认 Bauhaus / Swiss 路径由用户既有 skill 负责，atlas 不改它们。

## 路由表

（E2 起补）
