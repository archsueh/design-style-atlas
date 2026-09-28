# 网格案例标注法

激活：`style: ref/grid-annotate`

与 `muller-brockmann-grid-systems` 的分工：它给**自己的页面**画可开关网格并做 0px 贴合验证；本文件给**别人的成品图**做可读标注。

## 图层约定

套用 `templates/annotation-layer.svg`。色与线型固定，不改。

| 层 | id 前缀 | 色（示例，屏幕用） | 线型 |
|---|---|---|---|
| 版心 | `MB` | `#E11D48` | 实线 2px |
| 栏 | `COL` | `#2563EB` | 实线 1px |
| 模块 | `MOD` | `#059669` | 虚线 1px |
| 基线 | `BL` | `#CA8A04` | 极细实线 0.5px |
| 对齐轴 | `AX` | `#7C3AED` | 点线 |
| 破格点 | `BRK` | `#EA580C` | 圆标记 + 引出线 |

（色是标注层的编码色，不是被标注作品的配色。）

## 标签格式

`[层]-[序号] 数值`

例：

- `COL-3 w=48px gutter=16px`
- `MB 720×1020 margin=48/48/64/48`（上右下左）
- `BL 8px × 3 = 24px leading`
- `BRK-1 主标题右缘超出 COL-4，服务曲目名远距识别`

## 输出物

1. 原图（合法来源，本库不存版权图）
2. 标注 SVG 叠层（`templates/annotation-layer.svg` 复制后改数字）
3. 九步拆分表（`decomposition-method.md`）

缺任一则标注未完成。
