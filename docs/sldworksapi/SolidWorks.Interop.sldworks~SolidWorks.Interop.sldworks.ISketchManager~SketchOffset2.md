# SketchOffset2 Method (ISketchManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchOffset2`

Offsets the selected sketch entities.
Offsets the selected sketch entities.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SketchOffset2( _
   ByVal Offset As System.Double, _
   ByVal BothDirections As System.Boolean, _
   ByVal Chain As System.Boolean, _
   ByVal CapEnds As System.Integer, _
   ByVal MakeConstruction As System.Integer, _
   ByVal AddDimensions As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISketchManager
Dim Offset As System.Double
Dim BothDirections As System.Boolean
Dim Chain As System.Boolean
Dim CapEnds As System.Integer
Dim MakeConstruction As System.Integer
Dim AddDimensions As System.Boolean
Dim value As System.Boolean
 
value = instance.SketchOffset2(Offset, BothDirections, Chain, CapEnds, MakeConstruction, AddDimensions)
```

```

System.bool SketchOffset2( 
   System.double Offset,
   System.bool BothDirections,
   System.bool Chain,
   System.int CapEnds,
   System.int MakeConstruction,
   System.bool AddDimensions
)
```

```

System.bool SketchOffset2( 
   System.double Offset,
   System.bool BothDirections,
   System.bool Chain,
   System.int CapEnds,
   System.int MakeConstruction,
   System.bool AddDimensions
) 
```

#### Parameters

*Offset*
:   Offset value; negative value offsets the sketch entities in the opposite direction

*BothDirections*
:   True to offset the sketch entities in both directions, false to offset the sketch entities in one direction

*Chain*
:   True to offset the chain of sketch entities, false to offset only the selected sketch entities (see **Remarks**)

*CapEnds*
:   Cap the ends as defined by [swSkOffsetCapEndType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSkOffsetCapEndType_e.html)

*MakeConstruction*
:   Convert original and offset sketch entities to construction sketch entities as defined by [swSkOffsetMakeConstructionType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSkOffsetMakeConstructionType_e.html)

*AddDimensions*
:   True to include the offset distance in the sketch, false to not

#### Return Value

True if the selected sketch entities are offset, false if not

Remarks

Specifying true for Chain offsets the selected sketch entities and any other sketch entities that belong to the same contour or chain (contiguous geometric entities like edges).

Example

[Offset Sketch (C#)](Sketch_Offset_Example_CSharp.htm)  
[Offset Sketch (VB.NET)](Sketch_Offset_Example_VBNET.htm)  
[Offset Sketch (VBA)](Sketch_Offset_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[IModelDoc2::SketchOffsetEntities2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEntities2.md)  
[IModelDoc2::SketchOffsetEdges Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEdges.md)  
[IModelDocExtension::SketchOffsetOnSurface Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SketchOffsetOnSurface.md)
