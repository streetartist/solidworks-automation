# GetDragPoint Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~GetDragPoint`

Gets the drag point.
Gets the drag point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDragPoint( _
   ByRef Point As System.Object _
) As System.Boolean
```

```

Dim instance As IDragOperator
Dim Point As System.Object
Dim value As System.Boolean
 
value = instance.GetDragPoint(Point)
```

```

System.bool GetDragPoint( 
   out System.object Point
)
```

```

System.bool GetDragPoint( 
   [Out] System.Object^ Point
) 
```

#### Parameters

*Point*
:   Array containing the X, Y, Z coordinates of the drag point

#### Return Value

True if successful, false if not

Remarks

Unless set to another value by [IDragOperator::SetDragPoint,](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~ISetDragPoint.md) this value is the origin of the component.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.md)  
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.md)  
[IDragOperator::IGetDragPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IGetDragPoint.md)  
[IDragOperator::ISetDragPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~ISetDragPoint.md)
