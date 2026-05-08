# GetTargetPoint Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~GetTargetPoint`

Gets the target point for the specified row in this callout.
Gets the target point for the specified row in this callout.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetTargetPoint( _
   ByVal RowID As System.Integer, _
   ByRef XPos As System.Double, _
   ByRef YPos As System.Double, _
   ByRef ZPos As System.Double _
) 
```

```

Dim instance As ICallout
Dim RowID As System.Integer
Dim XPos As System.Double
Dim YPos As System.Double
Dim ZPos As System.Double
 
instance.GetTargetPoint(RowID, XPos, YPos, ZPos)
```

```

void GetTargetPoint( 
   System.int RowID,
   out System.double XPos,
   out System.double YPos,
   out System.double ZPos
)
```

```

void GetTargetPoint( 
   System.int RowID,
   [Out] System.double XPos,
   [Out] System.double YPos,
   [Out] System.double ZPos
) 
```

#### Parameters

*RowID*
:   Row in callout

*XPos*
:   x coordinate of target point

*YPos*
:   y coordinate of target point

*ZPos*
:   z coordinate of target point

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.md)  
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.md)  
[ICallout::SetTargetPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~SetTargetPoint.md)  
[ICallout::UpdatePosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~UpdatePosition.md)
