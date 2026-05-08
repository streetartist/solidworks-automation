# SetTargetPoint Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~SetTargetPoint`

Sets the target point for the specified row in this callout.
Sets the target point for the specified row in this callout.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetTargetPoint( _
   ByVal RowID As System.Integer, _
   ByVal XPos As System.Double, _
   ByVal YPos As System.Double, _
   ByVal ZPos As System.Double _
) 
```

```

Dim instance As ICallout
Dim RowID As System.Integer
Dim XPos As System.Double
Dim YPos As System.Double
Dim ZPos As System.Double
 
instance.SetTargetPoint(RowID, XPos, YPos, ZPos)
```

```

void SetTargetPoint( 
   System.int RowID,
   System.double XPos,
   System.double YPos,
   System.double ZPos
)
```

```

void SetTargetPoint( 
   System.int RowID,
   System.double XPos,
   System.double YPos,
   System.double ZPos
) 
```

#### Parameters

*RowID*
:   Row in callout

*XPos*
:   x coordinate for this target point

*YPos*
:   y coordinate for this target point

*ZPos*
:   z coordinate for this target poi

Example

[Create Multi-row Callouts (VBA)](Create_Multi-row_Callouts_Example_VB.htm)  
[Create a Callout Independent of a Selection (C#)](Create_a_Callout_Independent_of_a_Selection_Example_CSharp.htm)  
[Create a Callout Independent of a Selection (VB.NET)](Create_a_Callout_Independent_of_a_Selection_Example_VBNET.htm)  
[Create a Callout Independent of a Selection (VBA)](Create_a_Callout_Independent_of_a_Selection_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.md)  
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.md)  
[ICallout::GetTargetPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~GetTargetPoint.md)  
[ICallout::UpdatePosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~UpdatePosition.md)
