# SketchOffset Method (ISketchManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchOffset`

Obsolete. Superseded by ISketchManager::SketchOffset2.
Obsolete. Superseded by [ISketchManager::SketchOffset2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchOffset2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SketchOffset( _
   ByVal Offset As System.Double, _
   ByVal BothDirections As System.Boolean, _
   ByVal Chain As System.Boolean, _
   ByVal CapEnds As System.Boolean, _
   ByVal MakeConstruction As System.Boolean, _
   ByVal AddDimensions As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISketchManager
Dim Offset As System.Double
Dim BothDirections As System.Boolean
Dim Chain As System.Boolean
Dim CapEnds As System.Boolean
Dim MakeConstruction As System.Boolean
Dim AddDimensions As System.Boolean
Dim value As System.Boolean
 
value = instance.SketchOffset(Offset, BothDirections, Chain, CapEnds, MakeConstruction, AddDimensions)
```

```

System.bool SketchOffset( 
   System.double Offset,
   System.bool BothDirections,
   System.bool Chain,
   System.bool CapEnds,
   System.bool MakeConstruction,
   System.bool AddDimensions
)
```

```

System.bool SketchOffset( 
   System.double Offset,
   System.bool BothDirections,
   System.bool Chain,
   System.bool CapEnds,
   System.bool MakeConstruction,
   System.bool AddDimensions
) 
```

#### Parameters

*Offset*
:   Offset value; negative value offsets in opposite direction

*BothDirections*
:   True to offset the sketch entities in both directions, false to not

*Chain*
:   True to offset the chain of sketch entities, false if you want only the selected sketch entities offset (see **Remarks**)

*CapEnds*
:   True to cap the bidirectional offset with arcs, false to not

*MakeConstruction*
:   True to make the sketch entities construction geometry after offsetting, false to not

*AddDimensions*
:   True to include the offset distance in the sketch, false to not

#### Return Value

True if the sketch entities are offset, false if not

Remarks

Specifying true to the Chain argument offsets the selected entity and any other entities that belong to the same contour or chain (contiguous geometric entities like edges).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)
