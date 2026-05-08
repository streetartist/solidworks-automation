<p align="center">
  <img src="logo.png" alt="solidworks-com logo" width="180">
</p>

# solidworks-com

> 中文 | [English](README.md)

`solidworks-com` 是一个面向 SOLIDWORKS COM API 的 Python 轻量封装库。它的目标不是替代官方 API，而是在保留原始 COM 访问能力的同时，把建模脚本里最常用、最容易踩坑的部分封装成更稳定、更容易组合的 Python 接口。

当前库重点覆盖：

- 连接、启动和操作 SOLIDWORKS 桌面程序
- 新建、打开、保存、另存、导出零件和装配体
- 草图绘制、方程曲线、样条、圆弧、轮廓选择
- 拉伸、切除、旋转、圆角、曲面、加厚、圆周阵列
- 装配体插入组件、模板查找、组件选择
- 装配配合，包括普通配合和齿轮配合的基础封装
- 使用射线选择面/边，方便做相切、重合、距离等配合
- 保留 `.com` 原始对象入口，用于调用尚未封装的官方 API

本项目只封装 SOLIDWORKS 已安装实例的 COM 接口，不包含 SOLIDWORKS 本体、模板、许可证或 Dassault/SOLIDWORKS 官方 API 文件。

## 混合 CAD 到 SOLIDWORKS 工作流

对于复杂模型和复杂装配，本项目可以作为两阶段流程里的 SOLIDWORKS 精修阶段：

1. 先使用来自 [`earthtojake/text-to-cad`](https://github.com/earthtojake/text-to-cad) 的 CAD skill 生成初始 B-Rep 几何。该项目是面向 coding agent 的开源 STEP-first CAD 生成 harness。
2. 对生成的 STEP 模型进行检查和验证。
3. 将 STEP 结果导入 SOLIDWORKS，再用 `solidworks_com` 脚本进行清理、微调、原生参考特征、装配配合、最终保存和导出。

只有在模型复杂度确实需要 CAD-first 初稿时才使用这个混合路径。如果用户要求完整可追溯的 SOLIDWORKS 原生特征树、任务只是简单零件或普通小装配，或者用户明确要求不要使用 STEP/build123d/text-to-cad，就直接用 `solidworks_com` 建模，不先走 CAD skill。

## 许可证

**GNU General Public License v3.0**

## 运行环境

必需：

- Windows
- 已安装并可正常启动的 SOLIDWORKS
- Python 3.9+
- `pywin32`

安装依赖：

```powershell
pip install -e .
```

或只安装运行依赖：

```powershell
pip install pywin32
```

注意：

- SOLIDWORKS COM 自动化只能在 Windows 上使用。
- 脚本会控制本机 SOLIDWORKS 桌面程序，适合交互式建模、批量建模和自动导出。
- 模板路径依赖本机 SOLIDWORKS 配置。库会优先使用 SOLIDWORKS 用户偏好和模板目录自动查找，也支持环境变量覆盖。

## 快速开始

创建一个简单拉伸块：

```python
from pathlib import Path

from solidworks_com import SolidWorks, mm

sw = SolidWorks.connect(visible=True)

part = sw.new_part()
part.select_plane("Front Plane")

with part.sketch() as sk:
    sk.corner_rectangle(-mm(25), -mm(15), mm(25), mm(15))

part.features.extrude_blind(mm(10))
part.save_as(Path(r"D:\tmp\block.SLDPRT"))
part.export(Path(r"D:\tmp\block.step"))
```

## 单位

SOLIDWORKS COM 几何接口通常使用米。库提供了简单单位转换函数：

```python
from solidworks_com import mm, cm, inch, deg

length = mm(20)
angle = deg(90)
```

方程曲线需要特别注意：某些 SOLIDWORKS 方程曲线表达式会按当前文档单位解释。示例脚本中针对毫米模板做了表达式转换。

## 连接 SOLIDWORKS

```python
from solidworks_com import SolidWorks

sw = SolidWorks.connect(visible=True)
```

常用参数：

```python
sw = SolidWorks.connect(
    visible=True,
    start=True,
    new_instance=False,
    prog_id="SldWorks.Application",
)
```

说明：

- `visible=True` 显示 SOLIDWORKS 窗口
- `start=True` 在没有运行实例时启动 SOLIDWORKS
- `new_instance=True` 尝试启动新实例
- `prog_id` 可用于切换 COM ProgID

## 文档操作

```python
from solidworks_com import DocumentType, OpenDocOptions, bitmask

doc = sw.open(
    r"D:\models\part.SLDPRT",
    options=bitmask(OpenDocOptions.Silent, OpenDocOptions.ReadOnly),
)

part = sw.new_part()
assembly = sw.new_assembly()
drawing = sw.new_drawing()
```

保存和导出：

```python
part.save()
part.save_as(r"D:\tmp\model.SLDPRT")
part.export(r"D:\tmp\model.step")
```

## 模板查找

`new_part()`、`new_assembly()` 和 `new_drawing()` 会尝试：

1. 环境变量指定的模板
2. SOLIDWORKS `GetDocumentTemplate`
3. SOLIDWORKS 用户偏好里的默认模板
4. SOLIDWORKS 用户偏好里的模板目录中实际存在的模板

环境变量：

- `SOLIDWORKS_PART_TEMPLATE`
- `SOLIDWORKS_ASSEMBLY_TEMPLATE`
- `SOLIDWORKS_DRAWING_TEMPLATE`

示例：

```powershell
$env:SOLIDWORKS_ASSEMBLY_TEMPLATE = "D:\SolidWorksData\templates\Assembly.asmdot"
```

## 草图

```python
part.select_plane("Top Plane")

with part.sketch() as sk:
    sk.line(0, 0, 0, mm(20), 0, 0)
    sk.circle(0, 0, mm(10))
    sk.arc(0, 0, mm(10), 0, 0, mm(10), direction=1)
    sk.spline([(0, 0), (mm(10), mm(5)), (mm(20), 0)])
```

支持的常用草图接口包括：

- `line`
- `centerline`
- `corner_rectangle`
- `center_rectangle`
- `circle`
- `arc`
- `three_point_arc`
- `ellipse`
- `polygon`
- `spline`
- `equation_spline`
- `polyline`

## 方程曲线

```python
with part.sketch() as sk:
    sk.equation_spline(
        "10*(cos(t)+t*sin(t))",
        "10*(sin(t)-t*cos(t))",
        range_start="0",
        range_end="1.0",
        lock_start=True,
        lock_end=True,
    )
```

方程曲线用于渐开线、特殊曲线和参数化轮廓很方便，但需要注意：

- 表达式单位可能和普通草图坐标单位不同
- 方程曲线视觉连接不等于 SOLIDWORKS 认为轮廓闭合
- 做切除前应添加草图关系，并显式选择 closed contour

## 草图关系和轮廓选择

库封装了常用草图关系：

```python
with part.sketch() as sk:
    a = sk.line(0, 0, 0, mm(10), 0, 0)
    b = sk.line(mm(10), 0, 0, mm(10), mm(10), 0)
    sk.coincident_endpoints(a, b)
```

也可以直接添加约束：

```python
from solidworks_com import ConstraintType

sk.add_relation([entity_a, entity_b], ConstraintType.Coincident)
```

轮廓选择：

```python
with part.sketch() as sk:
    sk.polyline([(0, 0), (mm(10), 0), (mm(10), mm(10)), (0, mm(10))])
    sk.select_closed_contours(min_segments=4)

part.features.cut_midplane(mm(20))
```

底层对象：

```python
contours = part.active_sketch_contours()
for contour in contours:
    print(contour.is_closed, contour.segment_count)
```

## 特征

常用特征：

```python
part.features.extrude_blind(mm(10))
part.features.extrude_midplane(mm(10))
part.features.cut_blind(mm(5))
part.features.cut_midplane(mm(20))
part.features.revolve()
part.features.fillet_selected(mm(1))
```

圆周阵列：

```python
part.clear_selection()
part.select_object(axis, mark=1)
part.select_object(seed_feature, append=True, mark=4)
part.features.circular_pattern_selected(instances=24)
```

通用调用入口：

```python
part.features.call("SomeFeatureManagerMethod", arg1, arg2)
```

## 历史特征编辑

修改已经被下游特征消费的草图时，不要只改草图后直接重建。SOLIDWORKS 特征会保存当时的选择、轮廓和区域引用；草图拓扑改变后，旧特征可能重解到错误轮廓。

库提供了通用的历史编辑基础能力：

```python
old_feature = part.find_feature(lambda f: part.feature_name(f) == "Cut-Extrude1")

with part.replace_feature_at_history(old_feature, delete_old_on_success=True):
    parent_sketch = part.find_feature(lambda f: part.feature_type(f) == "ProfileFeature")

    with part.edit_sketch_feature(parent_sketch) as editor:
        editor.delete_segments(lambda segment: ...)
        # 使用原始 SketchManager 或 editor.model.sketch_manager 创建新草图实体

    contours = part.active_sketch_contours(require=False)
    selected = [contour for contour in contours if ...]
    part.select_sketch_contours(selected)
    part.features.cut_midplane(mm(4))
```

这些接口不假设草图里是圆、矩形或孔。调用方用 predicate 判断具体 segment 或 contour：

- `iter_features()`
- `find_feature(predicate)`
- `find_feature_by_name(name, type_name=...)`
- `find_features_by_name(name, contains=True, type_name=...)`
- `find_features_by_name_pattern(pattern, type_name=...)`
- `select_feature_by_name(name, type_name=...)`
- `next_feature(feature, type_name=...)`
- `rollback_before(feature)`
- `rollback_after(feature)`
- `rollback_to_end()`
- `suppress_feature(feature)`
- `delete_feature(feature)`
- `edit_sketch_feature(feature)`
- `replace_feature_at_history(feature, ...)`
- `SketchEditor.segments()`
- `SketchEditor.delete_segments(predicate)`
- `SketchEditor.matching_contours(predicate)`

中文特征名可以直接匹配，例如 `find_feature_by_name("草图8")`。如果从 PowerShell 管道或临时标准输入脚本调用 Python，需确认脚本文本以 UTF-8 进入 Python；否则中文可能在到达库之前已经变成 `??`。

## 装配体

```python
asm = sw.new_assembly()

comp_a = asm.add_component(r"D:\tmp\a.SLDPRT", x=0, y=0, z=0)
comp_b = asm.add_component(r"D:\tmp\b.SLDPRT", x=mm(50), y=0, z=0)

asm.rebuild()
asm.save_as(r"D:\tmp\assembly.SLDASM")
```

组件路径会自动转换为绝对路径，以避免 `AddComponent5` 因相对路径失败。

## 装配配合

库提供了基于当前选择集的配合接口：

```python
asm.add_coincident_mate_selected()
asm.add_concentric_mate_selected()
asm.add_parallel_mate_selected()
asm.add_tangent_mate_selected()
asm.add_distance_mate_selected(mm(20))
asm.add_gear_mate_selected(numerator=36, denominator=24)
```

使用模式：

```python
asm.clear_selection()
asm.select_by_id("Front Plane@part_a-1@装配体1", "PLANE")
asm.select_by_id("Front Plane@part_b-1@装配体1", "PLANE", append=True)
asm.add_coincident_mate_selected()
```

齿轮配合：

```python
asm.clear_selection()
asm.select_component_feature(comp_a, "driver center axis", "AXIS")
asm.select_component_feature(comp_b, "driven center axis", "AXIS", append=True)
asm.add_gear_mate_selected(numerator=36, denominator=24)
```

说明：

- `Gear Mate` 是 SOLIDWORKS 机械配合，不检查真实齿面接触，只约束旋转比。
- 几何定位仍需要平面重合、轴线平行、中心距距离等普通 mate。
- 当前封装优先使用 `AddMate5`，后续可继续扩展到 `CreateMateData/CreateMate`。

## 按射线选择面和边

`Face<1>` 这类名称不稳定，因此库增加了 `SelectByRay` 封装：

```python
part.select_face_by_ray(
    origin=(0, 0, mm(20)),
    direction=(0, 0, -1),
    radius=mm(1),
)

face = part.selected_object()
```

选边：

```python
part.select_edge_by_ray(
    origin=(mm(30), 0, 0),
    direction=(-1, 0, 0),
    radius=mm(1),
)
```

装配中用于配合：

```python
asm.add_tangent_mate_between_ray_faces(
    first_origin=(0.02, 0, 0),
    first_direction=(-1, 0, 0),
    second_origin=(0.05, 0, 0),
    second_direction=(1, 0, 0),
    radius=0.001,
)
```

## 直接访问 COM

封装没有覆盖到的官方 API 可以直接通过 `.com` 调用：

```python
model = sw.active_doc()
model.com.EditRebuild3()
sw.com.SendMsgToUser2("Done", 0, 0)
```

这也是本库的设计原则之一：封装常用稳定路径，但不阻断原始 API。

## API 概览

应用和文档：

- `SolidWorks.connect()` / `connect()`
- `revision_number`
- `active_doc()`
- `open()`
- `new_part()` / `new_assembly()` / `new_drawing()`
- `new_document()` / `try_new_document()`
- `document_template_candidates()`
- `default_template()`
- `user_preference_string()`
- `close()` / `exit()`

模型通用操作：

- `title`
- `extension`
- `features`
- `sketch_manager`
- `selection_manager`
- `activate()`
- `rebuild()` / `force_rebuild()`
- `save()` / `save_as()` / `export()`
- `part_box()` / `size()`
- `clear_selection()`
- `selected_object()`
- `create_select_data()`
- `select_by_id()`
- `select_by_ray()`
- `select_face_by_ray()` / `select_edge_by_ray()`
- `select_plane()` / `select_feature()` / `select_axis()` / `select_sketch()`
- `select_object()`
- `delete_selected()` / `suppress_selected()` / `unsuppress_selected()`
- `delete_feature()` / `suppress_feature()` / `unsuppress_feature()`
- `last_feature()` / `rename_last_feature()`
- `feature_name()` / `feature_type()` / `feature_error_code()` / `feature_errors()`

草图和轮廓：

- `sketch()` / `sketch3d()`
- `edit_sketch_feature()`
- `active_sketch()`
- `active_sketch_contours()`
- `select_sketch_contours()`
- `select_closed_sketch_contours()`
- `select_matching_sketch_contours()`
- `SketchBuilder.line()`
- `SketchBuilder.centerline()`
- `SketchBuilder.corner_rectangle()` / `center_rectangle()`
- `SketchBuilder.circle()`
- `SketchBuilder.arc()` / `three_point_arc()`
- `SketchBuilder.ellipse()`
- `SketchBuilder.polygon()`
- `SketchBuilder.spline()`
- `SketchBuilder.equation_spline()`
- `SketchBuilder.polyline()`
- `SketchBuilder.add_relation()`
- `SketchBuilder.coincident()` / `tangent()` / `merge_points()`
- `SketchBuilder.start_point()` / `end_point()` / `coincident_endpoints()`
- `SketchBuilder.contours()` / `select_closed_contours()`
- `SketchEditor.segments()` / `matching_segments()` / `delete_segments()`
- `SketchEditor.contours()` / `matching_contours()` / `select_contours()`
- `SketchSegment.type` / `curve` / `curve_params()` / `select()` / `delete()`
- `SketchContour.is_closed` / `segment_count` / `segments` / `sketch_segments` / `edge_count` / `edges` / `select()` / `deselect()`

特征工具：

- `extrude_blind()` / `extrude_midplane()`
- `cut_blind()` / `cut_midplane()`
- `revolve()`
- `fillet_selected()`
- `circular_pattern_selected()`
- `loft_boss()` / `loft_surface()`
- `thicken_selected()`
- `fill_surface_selected()`
- `knit_selected()`
- `offset_plane()`
- `call()`

装配体：

- `AssemblyDoc.add_component()`
- `AssemblyDoc.add_components()`
- `Component.name`
- `Component.select()`
- `select_component_feature()`
- `add_mate_selected()`
- `add_coincident_mate_selected()`
- `add_concentric_mate_selected()`
- `add_parallel_mate_selected()`
- `add_tangent_mate_selected()`
- `add_distance_mate_selected()`
- `add_gear_mate_selected()`
- `add_gear_mate_between_axes()`
- `select_face_for_mate_by_ray()` / `select_edge_for_mate_by_ray()`
- `add_tangent_mate_between_ray_faces()`
- `add_coincident_mate_between_ray_faces()`

构建器和底层工具：

- `PartBuilder.new()`
- `PartBuilder.box()`
- `PartBuilder.cylinder()`
- `PartBuilder.save_as()`
- `mm()` / `cm()` / `inch()` / `deg()`
- `bitmask()`
- `document_type_from_path()`
- `call_or_value()`
- `member_value()`
- `call_member()`
- `int_byref()` / `empty_dispatch()` / `empty_variant()` / `variant_byref()` / `double_array()` / `variant_array()`

## 示例

当前 `examples/` 包含：

- `test_loft_smoke.py`：放样基础测试
- `test_contour_selection.py`：草图关系和 contour selection 测试
- `test_equation_spline_minimal.py`：方程样条最小测试
- `test_equation_involute_single.py`：单条渐开线方程曲线测试
- `test_equation_involute_curve.py`：渐开线曲线调试
- `test_equation_slot_profile.py`：函数驱动齿槽草图调试
- `model_meshing_gears.py`：两只渐开线直齿轮建模、切齿槽、圆周阵列、装配和导出
- `model_product_propeller.py`：螺旋桨建模示例

运行齿轮示例：

```powershell
python examples\model_meshing_gears.py --output-dir output\gears
```

只生成零件，不导 STEP：

```powershell
python examples\model_meshing_gears.py --no-step --output-dir output\gears
```

隐藏 SOLIDWORKS 窗口：

```powershell
python examples\model_meshing_gears.py --hidden
```

## 齿轮示例说明

`model_meshing_gears.py` 演示了较完整的工程流程：

- 生成齿轮圆柱 blank
- 使用函数驱动渐开线绘制一个齿槽
- 使用草图关系和 contour selection 保证切除轮廓可解
- 切除一个齿槽
- 对齿槽切除做圆周阵列
- 添加中心孔
- 生成两个不同齿数的齿轮
- 创建装配体并按中心距放置
- 添加基础齿轮配合能力
- 保存 SLDASM 并导出 STEP

齿轮几何仍在持续改进中。生产级齿根建议使用受控刀具/齿条生成的齿根过渡，而不是自由样条。

## 项目结构

```text
solidworks_com/
  app.py          # SOLIDWORKS application wrapper
  model.py        # part/model/sketch/feature wrapper
  assembly.py     # assembly, component, mate helpers
  builders.py     # higher-level generic builders
  constants.py    # selected SOLIDWORKS enum values
  com.py          # pywin32 helpers and VARIANT helpers
  geometry.py     # simple geometry data structures
  units.py        # unit conversion helpers
examples/
  *.py            # runnable modeling and API smoke tests
docs/
  ...             # local generated/reference API docs
```

## 设计原则

- 保持薄封装，不隐藏 SOLIDWORKS COM 的本质。
- 常用流程用 Pythonic API 表达。
- 不把具体产品模型固化进库 API，复杂模型放在 `examples/`。
- 所有封装都尽量保留 escape hatch：需要时直接访问 `.com`。
- 对 pywin32 动态 dispatch 和 makepy 生成 wrapper 的差异做兼容。

## 已知限制

- 只支持 Windows + SOLIDWORKS 桌面版。
- 自动化过程依赖本机 SOLIDWORKS 版本、模板、语言和用户设置。
- 部分 SOLIDWORKS COM 方法在 pywin32 下可能表现为属性而不是函数，库已对常见情况做兼容，但仍可能遇到版本差异。
- 面/边自动识别目前以 `SelectByRay` 为主，还没有完整的 B-Rep 几何筛选器。
- 装配 mate 封装目前以 `AddMate5` 为主，后续可以补 `CreateMateData/CreateMate`。

## 贡献

欢迎提交 issue 和 pull request。建议贡献方向：

- 更多 SOLIDWORKS enum 封装
- 更可靠的 face/edge/body 遍历与筛选
- `CreateMateData/CreateMate` 新式 mate API
- 更多特征封装
- 更多可复现的 smoke tests
- 更完整的齿轮、凸轮、曲面等工程示例



