# Select Method (IEdgePoint)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgePoint~Select`

Selects a midpoint on an edge or an endpoint or midpoint on a reference curve.
Selects a midpoint on an [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) or an endpoint or midpoint on a [reference curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Select( _
   ByVal BAppend As System.Boolean, _
   ByVal SelMark As System.Integer _
) As System.Boolean
```

```

Dim instance As IEdgePoint
Dim BAppend As System.Boolean
Dim SelMark As System.Integer
Dim value As System.Boolean
 
value = instance.Select(BAppend, SelMark)
```

```

System.bool Select( 
   System.bool BAppend,
   System.int SelMark
)
```

```

System.bool Select( 
   System.bool BAppend,
   System.int SelMark
) 
```

#### Parameters

*BAppend*
:   True to add this selection to the current selection, false to replace the current selection list with this selection

*SelMark*
:   Selection mark to assign to this midpoint or endpoint

#### Return Value

True if an endpoint or midpoint is selected, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdgePoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgePoint.md)  
[IEdgePoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgePoint_members.md)
