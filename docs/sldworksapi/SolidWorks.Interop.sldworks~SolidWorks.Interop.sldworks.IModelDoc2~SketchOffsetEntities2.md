# SketchOffsetEntities2 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEntities2`

Generates entities in the active sketch by offsetting the selected geometry by the specified amount.
Generates entities in the active sketch by offsetting the selected geometry by the specified amount.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SketchOffsetEntities2( _
   ByVal Offset As System.Double, _
   ByVal BothDirections As System.Boolean, _
   ByVal Chain As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim Offset As System.Double
Dim BothDirections As System.Boolean
Dim Chain As System.Boolean
Dim value As System.Boolean
 
value = instance.SketchOffsetEntities2(Offset, BothDirections, Chain)
```

```

System.bool SketchOffsetEntities2( 
   System.double Offset,
   System.bool BothDirections,
   System.bool Chain
)
```

```

System.bool SketchOffsetEntities2( 
   System.double Offset,
   System.bool BothDirections,
   System.bool Chain
) 
```

#### Parameters

*Offset*
:   Offset distance in meters

*BothDirections*
:   True to offset in both directions, false to not

*Chain*
:   True if you want entire chain of entities offset, false if you want only selected sketch entities offset (see **Remarks**)

#### Return Value

True if the offset is successful, false if not

Remarks

The geometry selected for offset can be an edge, loop, face, external sketch curve, external sketch contour, set of edges, or set of external sketch curves.

Specifying true for the Chain argument offsets the selected entity and any other entities that belong to the same contour or chain (contiguous, geometric entities like edges).

NOTE: If the selected geometry is a sketch item, it must be an external sketch curve (for example, it cannot be an item in the active sketch). To offset sketch segments within the active sketch, use [IModelDoc2::SketchOffset2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffset2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::SketchOffsetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEdges.md)  
[ISketchManager::SketchUseEdge2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchUseEdge2.md)  
[IModelDocExtension::SketchOffsetOnSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SketchOffsetOnSurface.md)
