<p align="center">
  <img src="logo.png" alt="solidworks-com logo" width="180">
</p>

# solidworks-com

> [中文](README.zh-CN.md) | English

`solidworks-com` is a lightweight Python wrapper around the SOLIDWORKS COM API. It does not try to replace the official API. Instead, it wraps the repetitive and fragile parts of everyday SOLIDWORKS automation while keeping raw COM objects available through `.com`.

The library currently focuses on:

- Connecting to and controlling the SOLIDWORKS desktop application
- Creating, opening, saving, exporting parts and assemblies
- Sketch creation, equation-driven splines, splines, arcs, sketch relations, and contour selection
- Extrudes, cuts, revolves, fillets, surfaces, thicken, and circular patterns
- Assembly creation, component insertion, template discovery, and component selection
- Basic assembly mates, including gear mates
- Face and edge selection by ray for tangent, coincident, and distance mate workflows
- Direct access to raw COM objects for APIs not wrapped yet

This project only wraps an installed SOLIDWORKS COM server. It does not include SOLIDWORKS, templates, licenses, or Dassault/SOLIDWORKS official API files.

## Hybrid CAD-to-SOLIDWORKS Workflow

For complex models and assemblies, this repository can be used as the SOLIDWORKS finishing stage in a two-step workflow:

1. Generate the initial B-Rep geometry with the CAD skill from [`earthtojake/text-to-cad`](https://github.com/earthtojake/text-to-cad), which is an open-source coding-agent harness for STEP-first CAD generation.
2. Inspect and validate the generated STEP model.
3. Import the STEP result into SOLIDWORKS and use `solidworks_com` scripts for cleanup, micro-adjustments, native reference features, mates, final saves, and exports.

Use this hybrid path only when the model complexity justifies a CAD-first pass. Do not use it when the user needs a fully traceable native SOLIDWORKS feature tree, when the task is a simple part or ordinary small assembly, or when the user explicitly asks not to use STEP/build123d/text-to-cad.

## License

**GNU General Public License v3.0**

## Requirements

- Windows
- SOLIDWORKS installed and able to start normally
- Python 3.9+
- `pywin32`

Install in editable mode:

```powershell
pip install -e .
```

Or install only the runtime dependency:

```powershell
pip install pywin32
```

## Quick Start

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

## Units

Most SOLIDWORKS COM geometry calls use meters. The package provides small conversion helpers:

```python
from solidworks_com import mm, cm, inch, deg
```

Equation-driven curves may be interpreted in document units, so check your template settings.

## Documents

```python
part = sw.new_part()
assembly = sw.new_assembly()
drawing = sw.new_drawing()

doc = sw.open(r"D:\models\part.SLDPRT")
```

Saving and exporting:

```python
part.save()
part.save_as(r"D:\tmp\model.SLDPRT")
part.export(r"D:\tmp\model.step")
```

## Templates

`new_part()`, `new_assembly()`, and `new_drawing()` try several template sources:

1. Environment variables
2. SOLIDWORKS `GetDocumentTemplate`
3. SOLIDWORKS default template user preferences
4. Existing templates found in SOLIDWORKS template folders

Environment variables:

- `SOLIDWORKS_PART_TEMPLATE`
- `SOLIDWORKS_ASSEMBLY_TEMPLATE`
- `SOLIDWORKS_DRAWING_TEMPLATE`

## Sketches

```python
part.select_plane("Top Plane")

with part.sketch() as sk:
    sk.line(0, 0, 0, mm(20), 0, 0)
    sk.circle(0, 0, mm(10))
    sk.spline([(0, 0), (mm(10), mm(5)), (mm(20), 0)])
```

Equation-driven spline:

```python
with part.sketch() as sk:
    sk.equation_spline(
        "10*(cos(t)+t*sin(t))",
        "10*(sin(t)-t*cos(t))",
        range_start="0",
        range_end="1.0",
    )
```

## Sketch Relations and Contours

```python
with part.sketch() as sk:
    a = sk.line(0, 0, 0, mm(10), 0, 0)
    b = sk.line(mm(10), 0, 0, mm(10), mm(10), 0)
    sk.coincident_endpoints(a, b)
```

Selecting a closed contour for a feature:

```python
with part.sketch() as sk:
    sk.polyline([(0, 0), (mm(10), 0), (mm(10), mm(10)), (0, mm(10))])
    sk.select_closed_contours(min_segments=4)

part.features.cut_midplane(mm(20))
```

## Features

```python
part.features.extrude_blind(mm(10))
part.features.extrude_midplane(mm(10))
part.features.cut_blind(mm(5))
part.features.cut_midplane(mm(20))
part.features.revolve()
part.features.fillet_selected(mm(1))
```

Raw FeatureManager access:

```python
part.features.call("SomeFeatureManagerMethod", arg1, arg2)
```

## History Editing

Do not edit a sketch consumed by downstream features and then blindly rebuild. SOLIDWORKS features keep selection, contour, and region references. If sketch topology changes, the old feature can resolve to the wrong contour.

The library exposes generic history-editing building blocks:

```python
old_feature = part.find_feature(lambda f: part.feature_name(f) == "Cut-Extrude1")

with part.replace_feature_at_history(old_feature, delete_old_on_success=True):
    parent_sketch = part.find_feature(lambda f: part.feature_type(f) == "ProfileFeature")

    with part.edit_sketch_feature(parent_sketch) as editor:
        editor.delete_segments(lambda segment: ...)
        # Create replacement sketch entities with SketchManager or editor.model.sketch_manager.

    contours = part.active_sketch_contours(require=False)
    selected = [contour for contour in contours if ...]
    part.select_sketch_contours(selected)
    part.features.cut_midplane(mm(4))
```

These APIs are not specific to circles, rectangles, or holes. Callers decide what to match with predicates:

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

Localized feature names are supported, for example `find_feature_by_name("草图8")`. When invoking Python through a PowerShell pipe or temporary standard-input script, make sure the script text reaches Python as UTF-8; otherwise the Chinese text may become `??` before the library sees it.

## Assemblies and Mates

```python
asm = sw.new_assembly()
comp_a = asm.add_component(r"D:\tmp\a.SLDPRT", x=0, y=0, z=0)
comp_b = asm.add_component(r"D:\tmp\b.SLDPRT", x=mm(50), y=0, z=0)
```

Mate helpers work on the current selection:

```python
asm.add_coincident_mate_selected()
asm.add_concentric_mate_selected()
asm.add_parallel_mate_selected()
asm.add_tangent_mate_selected()
asm.add_distance_mate_selected(mm(20))
asm.add_gear_mate_selected(numerator=36, denominator=24)
```

Gear mate example:

```python
asm.clear_selection()
asm.select_component_feature(comp_a, "driver center axis", "AXIS")
asm.select_component_feature(comp_b, "driven center axis", "AXIS", append=True)
asm.add_gear_mate_selected(numerator=36, denominator=24)
```

## Selecting Faces and Edges by Ray

```python
part.select_face_by_ray(
    origin=(0, 0, mm(20)),
    direction=(0, 0, -1),
    radius=mm(1),
)

face = part.selected_object()
```

Assembly tangent mate using ray-selected faces:

```python
asm.add_tangent_mate_between_ray_faces(
    first_origin=(0.02, 0, 0),
    first_direction=(-1, 0, 0),
    second_origin=(0.05, 0, 0),
    second_direction=(1, 0, 0),
    radius=0.001,
)
```

## Raw COM Access

```python
model = sw.active_doc()
model.com.EditRebuild3()
sw.com.SendMsgToUser2("Done", 0, 0)
```

## API Overview

Application and documents:

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

General model operations:

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

Sketches and contours:

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

Feature tools:

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

Assemblies:

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

Builders and low-level helpers:

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

## Examples

Run the meshing gear example:

```powershell
python examples\model_meshing_gears.py --output-dir output\gears
```

Only save native files:

```powershell
python examples\model_meshing_gears.py --no-step --output-dir output\gears
```

## Project Layout

```text
solidworks_com/
  app.py
  model.py
  assembly.py
  builders.py
  constants.py
  com.py
  geometry.py
  units.py
examples/
  *.py
docs/
  ...
```

## Known Limitations

- Windows and SOLIDWORKS desktop only.
- Behavior depends on the installed SOLIDWORKS version, templates, language, and user settings.
- Some COM members appear as properties under pywin32 and as methods under makepy-generated wrappers; the library handles common cases but version differences can still occur.
- Face and edge selection currently relies mainly on `SelectByRay`; full B-Rep filtering is not implemented yet.
- Mate helpers currently use `AddMate5`; newer `CreateMateData/CreateMate` wrappers can be added later.

## Contributing

Useful contribution areas:

- More SOLIDWORKS enum values
- Better face/edge/body traversal and filtering
- Modern mate API wrappers
- Additional feature wrappers
- More reproducible smoke tests
- More engineering examples



