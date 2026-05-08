# AddControl2 Method (IPropertyManagerPageGroup)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup~AddControl2`

Adds a control to this PropertyManager page group box.
Adds a control to this PropertyManager page group box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddControl2( _
   ByVal ID As System.Integer, _
   ByVal ControlType As System.Short, _
   ByVal Caption As System.String, _
   ByVal LeftAlign As System.Short, _
   ByVal Options As System.Integer, _
   ByVal Tip As System.String _
) As System.Object
```

```

Dim instance As IPropertyManagerPageGroup
Dim ID As System.Integer
Dim ControlType As System.Short
Dim Caption As System.String
Dim LeftAlign As System.Short
Dim Options As System.Integer
Dim Tip As System.String
Dim value As System.Object
 
value = instance.AddControl2(ID, ControlType, Caption, LeftAlign, Options, Tip)
```

```

System.object AddControl2( 
   System.int ID,
   System.short ControlType,
   System.string Caption,
   System.short LeftAlign,
   System.int Options,
   System.string Tip
)
```

```

System.Object^ AddControl2( 
   System.int ID,
   System.short ControlType,
   System.String^ Caption,
   System.short LeftAlign,
   System.int Options,
   System.String^ Tip
) 
```

#### Parameters

*ID*
:   Resource ID of the control

*ControlType*
:   Type of control as defined in [swPropertyManagerPageControlType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageControlType_e.html)

*Caption*
:   Caption of the control

*LeftAlign*
:   Left alignment of this control as defined in [swPropertyManagerPageControlLeftAlign\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageControlLeftAlign_e.html)

*Options*
:   Options as defined in [swAddControlOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAddControlOptions_e.html) (see **Remarks**)

*Tip*
:   ToolTip text for the control

#### Return Value

Newly created [control for this PropertyManager page group box](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.md)

Remarks

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Show2.md) and [IPropertyManagerPage2::Close](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Close.md).

When you specify swAddControlOptions\_e.swControlOptions\_SmallGapAbove for the Options parameter, the gap created between a new control and the previous control is smaller than the typical gap. Also, the control is hidden unless you specify swAddControlOptions\_e.swControlOptions\_Visible for the Options parameter. In the previous versions of this method, IPropertyManagerPageGroup::AddControl and IPropertyManagerGroup::IAddControl, the control was visible regardless if the Options parameter was set or not set to swAddControlOptions\_e.swControlOptions\_Visible.

Example

See the [IPropertyManagerPageGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup.md) examples.

Example

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup.md)  
[IPropertyManagerPageGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup_members.md)
