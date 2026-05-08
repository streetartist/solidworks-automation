# SetSliderParameters Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~SetSliderParameters`

Sets the parameters for the slider.
Sets the parameters for the slider.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetSliderParameters( _
   ByVal PositionCount As System.Integer, _
   ByVal DivisionCount As System.Integer _
) 
```

```

Dim instance As IPropertyManagerPageNumberbox
Dim PositionCount As System.Integer
Dim DivisionCount As System.Integer
 
instance.SetSliderParameters(PositionCount, DivisionCount)
```

```

void SetSliderParameters( 
   System.int PositionCount,
   System.int DivisionCount
)
```

```

void SetSliderParameters( 
   System.int PositionCount,
   System.int DivisionCount
) 
```

#### Parameters

*PositionCount*
:   Number of discreet positions on the slider

*DivisionCount*
:   Number of regions separated by tick marks on the slider

Remarks

When a user drags the slider, PositionCount defines how sensitive the slider is. Not all of the specified discreet points are displayed if the PropertyManager page is not wide enough to show them. However, if the user widens the PropertyManager page, then more points are displayed.

When a user drags the slider, the user-interface tends to snap to the nearest tick mark when the drag is nearby, making it easier for the user to set whole values.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageNumberbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox.md)  
[IPropertyManagerPageNumberbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox_members.md)  
[IPropertyManagerNumberbox::SetRange2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~SetRange2.md)
