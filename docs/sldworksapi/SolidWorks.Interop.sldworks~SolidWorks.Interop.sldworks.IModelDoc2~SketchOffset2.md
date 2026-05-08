# SketchOffset2 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffset2`

Obsolete. Superseded by ISketchManager::SketchOffset.
Obsolete. Superseded by [ISketchManager::SketchOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchOffset.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SketchOffset2( _
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
 
value = instance.SketchOffset2(Offset, BothDirections, Chain)
```

```

System.bool SketchOffset2( 
   System.double Offset,
   System.bool BothDirections,
   System.bool Chain
)
```

```

System.bool SketchOffset2( 
   System.double Offset,
   System.bool BothDirections,
   System.bool Chain
) 
```

#### Parameters

*Offset*
:   Offset value; negative value offsets in opposite direction

*BothDirections*
:   True to offset in both directions, false to not

*Chain*
:   True if you want the entire chain of entities offset, false if you want only the selected sketch entities offset (see **Remarks**)

#### Return Value

True if the offset is successful, false if not

Remarks

Specifying true for the Chain argument offsets the selected entity and any other entities that belong to the same contour or chain (contiguous, geometric entities like edges).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::SketchOffsetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEdges.md)  
[IModelDoc2::SketchOffsetEntities2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEntities2.md)
