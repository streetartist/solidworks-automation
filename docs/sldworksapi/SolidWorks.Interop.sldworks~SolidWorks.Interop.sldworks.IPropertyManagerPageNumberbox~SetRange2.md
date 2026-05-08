# SetRange2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~SetRange2`

Sets the range and increment for the slider.
Sets the range and increment for the slider.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetRange2( _
   ByVal Units As System.Integer, _
   ByVal Minimum As System.Double, _
   ByVal Maximum As System.Double, _
   ByVal Inclusive As System.Boolean, _
   ByVal Increment As System.Double, _
   ByVal FastIncr As System.Double, _
   ByVal SlowIncr As System.Double _
) 
```

```

Dim instance As IPropertyManagerPageNumberbox
Dim Units As System.Integer
Dim Minimum As System.Double
Dim Maximum As System.Double
Dim Inclusive As System.Boolean
Dim Increment As System.Double
Dim FastIncr As System.Double
Dim SlowIncr As System.Double
 
instance.SetRange2(Units, Minimum, Maximum, Inclusive, Increment, FastIncr, SlowIncr)
```

```

void SetRange2( 
   System.int Units,
   System.double Minimum,
   System.double Maximum,
   System.bool Inclusive,
   System.double Increment,
   System.double FastIncr,
   System.double SlowIncr
)
```

```

void SetRange2( 
   System.int Units,
   System.double Minimum,
   System.double Maximum,
   System.bool Inclusive,
   System.double Increment,
   System.double FastIncr,
   System.double SlowIncr
) 
```

#### Parameters

*Units*
:   Number box units as defined in [swNumberboxUnitType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNumberboxUnitType_e.html) (see **Remarks**)

*Minimum*
:   Minimum value

*Maximum*
:   Maximum value

*Inclusive*
:   True sets the range as inclusive, false sets it as exclusive

*Increment*
:   Increment value

*FastIncr*
:   Fast increment value for scrolling and mouse-wheel

*SlowIncr*
:   Slow increment value for scrolling and mouse-wheel

Remarks

This method works while a PropertyManager page is displayed with these restrictions:

- You cannot change Units once the page is displayed. The Units parameter is ignored if specified while the page is displayed.
- If the range is changed to an invalid value by this method, then you must immediately call [IPropertyManagerPageNumberbox::Value](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~Value.md) and set a valid value to prevent displaying the dialog that requests the user to enter a valid value.

Example

[Create PropertyManager Page With Many Controls (VBA)](Create_PropertyManager_Page_With_Many_Controls_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageNumberbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox.md)  
[IPropertyManagerPageNumberbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox_members.md)  
[IPropertyManagerPageNumberbox::SetSliderParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~SetSliderParameters.md)  
[IPropertyManagerPageNumberbox::DisplayedUnit Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~DisplayedUnit.md)
