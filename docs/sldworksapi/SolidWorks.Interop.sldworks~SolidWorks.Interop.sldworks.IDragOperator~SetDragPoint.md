# SetDragPoint Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~SetDragPoint`

Sets the drag point.
Sets the drag point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetDragPoint( _
   ByVal Point As System.Object _
) As System.Boolean
```

```

Dim instance As IDragOperator
Dim Point As System.Object
Dim value As System.Boolean
 
value = instance.SetDragPoint(Point)
```

```

System.bool SetDragPoint( 
   System.object Point
)
```

```

System.bool SetDragPoint( 
   System.Object^ Point
) 
```

#### Parameters

*Point*
:   Array of size 3 containing the X, Y, Z coordinate of the drag point

#### Return Value

True if successful, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.md)  
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.md)  
[IDragOperator::GetDragPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~GetDragPoint.md)  
[IDragOperator::IGetDragPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IGetDragPoint.md)  
[IDragOperator::ISetDragPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~ISetDragPoint.md)
