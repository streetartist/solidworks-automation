# SetRange Method (IPropertyManagerPageNumberbox)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~SetRange`

Obsolete. Superseded by PropertyManagerPageNumberbox::SetRange2.
Obsolete. Superseded by [PropertyManagerPageNumberbox::SetRange2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~SetRange2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetRange( _
   ByVal Units As System.Integer, _
   ByVal Minimum As System.Double, _
   ByVal Maximum As System.Double, _
   ByVal Increment As System.Double, _
   ByVal Inclusive As System.Boolean _
) 
```

```

Dim instance As IPropertyManagerPageNumberbox
Dim Units As System.Integer
Dim Minimum As System.Double
Dim Maximum As System.Double
Dim Increment As System.Double
Dim Inclusive As System.Boolean
 
instance.SetRange(Units, Minimum, Maximum, Increment, Inclusive)
```

```

void SetRange( 
   System.int Units,
   System.double Minimum,
   System.double Maximum,
   System.double Increment,
   System.bool Inclusive
)
```

```

void SetRange( 
   System.int Units,
   System.double Minimum,
   System.double Maximum,
   System.double Increment,
   System.bool Inclusive
) 
```

#### Parameters

*Units*
:   Number box units as defined in [swNumberboxUnitType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNumberboxUnitType_e.html)

*Minimum*
:   Number box minimum value

*Maximum*
:   Number box maximum value

*Increment*
:   Number box increment

*Inclusive*
:   True sets the range as inclusive, false sets it as exclusive

Remarks

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Show2.md) and [IProperytManagerPage2::Close](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Close.md).

Example

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageNumberbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox.md)  
[IPropertyManagerPageNumberbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox_members.md)
