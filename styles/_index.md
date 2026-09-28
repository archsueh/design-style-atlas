# 风格总览与选择器

| # | id | 中文 | status | 激活 |
|---|---|---|---|---|
| 1 | `international-typographic` | 国际主义 | draft | `style: international-typographic` |
| 2 | `collage` | 拼贴 | draft | `style: collage` |
| 3 | `acid` | 酸性设计 | draft | `style: acid` |
| 4 | `_slot-04` | 待用户补名 | placeholder | 不可用 |
| 5 | `_slot-05` | 待用户补名 | placeholder | 不可用 |
| 6 | `_slot-06` | 待用户补名 | placeholder | 不可用 |
| 7 | `_slot-07` | 待用户补名 | placeholder | 不可用 |

选择：用户点名用哪条就用哪条。未点名 → 不选本表任何一行。

国际主义本机已有完整实现，本库只做薄入口。酸性与默认纪律冲突，必须显式声明；覆盖范围写在 `styles/acid.md` §9「例外通道」（schema 只允许 `exception: true` 的条目有 §9）。拼贴补的是泛化方法论，不是孟菲斯复古配方。
