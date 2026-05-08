# FullyDefineSketch Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~FullyDefineSketch`

Fully defines a sketch.
Fully defines a sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FullyDefineSketch( _
   ByVal EntitiesToFullyDefine As System.Boolean, _
   ByVal UseRelations As System.Boolean, _
   ByVal RelationsToApply As System.Integer, _
   ByVal UseDimensions As System.Boolean, _
   ByVal HorizontalDimScheme As System.Integer, _
   ByVal HorizontalDatumDisp As System.Object, _
   ByVal VerticalDimScheme As System.Integer, _
   ByVal VerticalDatumDisp As System.Object, _
   ByVal HorizontalDimPlacement As System.Integer, _
   ByVal VerticalDimPlacement As System.Integer _
) As System.Integer
```

```

Dim instance As ISketchManager
Dim EntitiesToFullyDefine As System.Boolean
Dim UseRelations As System.Boolean
Dim RelationsToApply As System.Integer
Dim UseDimensions As System.Boolean
Dim HorizontalDimScheme As System.Integer
Dim HorizontalDatumDisp As System.Object
Dim VerticalDimScheme As System.Integer
Dim VerticalDatumDisp As System.Object
Dim HorizontalDimPlacement As System.Integer
Dim VerticalDimPlacement As System.Integer
Dim value As System.Integer
 
value = instance.FullyDefineSketch(EntitiesToFullyDefine, UseRelations, RelationsToApply, UseDimensions, HorizontalDimScheme, HorizontalDatumDisp, VerticalDimScheme, VerticalDatumDisp, HorizontalDimPlacement, VerticalDimPlacement)
```

```

System.int FullyDefineSketch( 
   System.bool EntitiesToFullyDefine,
   System.bool UseRelations,
   System.int RelationsToApply,
   System.bool UseDimensions,
   System.int HorizontalDimScheme,
   System.object HorizontalDatumDisp,
   System.int VerticalDimScheme,
   System.object VerticalDatumDisp,
   System.int HorizontalDimPlacement,
   System.int VerticalDimPlacement
)
```

```

System.int FullyDefineSketch( 
   System.bool EntitiesToFullyDefine,
   System.bool UseRelations,
   System.int RelationsToApply,
   System.bool UseDimensions,
   System.int HorizontalDimScheme,
   System.Object^ HorizontalDatumDisp,
   System.int VerticalDimScheme,
   System.Object^ VerticalDatumDisp,
   System.int HorizontalDimPlacement,
   System.int VerticalDimPlacement
) 
```

#### Parameters

*EntitiesToFullyDefine*
:   True to fully define all entities, false to fully define only the entities selected

*UseRelations*
:   True to use relations, false to not

*RelationsToApply*
:   Relations to apply as defined in [swSketchFullyDefineRelationType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchFullyDefineRelationType_e.html)

*UseDimensions*
:   True to use dimensions, false to not

*HorizontalDimScheme*
:   - 0 = Chain

    1 = Baseline

    2 = Ordinate

*HorizontalDatumDisp*
:   Horizontal datum (model edge, model vertex, sketch line, sketch point), or, if Nothing or null, use entity with selection mark = 6

*VerticalDimScheme*
:   - 0 = Chain

    1 = Baseline

    2 = Ordinate

*VerticalDatumDisp*
:   Vertical datum (model edge, model vertex, sketch line, sketch point), or, if Nothing or null, use entity with selection mark = 6

*HorizontalDimPlacement*
:   - 0 = Above sketch

    1 = Below sketch

*VerticalDimPlacement*
:   - 0 = Right of sketch

    1 = Left of sketch

#### Return Value

Not currently defined

Example

[Fully Define Under Defined Sketch (VBA)](Fully_Define_Underdefined_Sketch_Example_VB.htm)  
[Fully Define Under Defined Sketch (VB.NET)](Fully_Define_Underdefined_Sketch_Example_VBNET.htm)  
[Fully Define Under Defined Sketch (C#)](Fully_Define_Underdefined_Sketch_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::AddAlongXDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddAlongXDimension.md)  
[ISketchManager::AddAlongYDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddAlongYDimension.md)  
[ISketchManager::AddAlongZDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddAlongZDimension.md)
