# IAddControl Method (IPropertyManagerPageTab)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab~IAddControl`

Obsolete. Superseded by IPropertyManagerPageTab::AddControl2.
Obsolete. Superseded by [IPropertyManagerPageTab::AddControl2.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab~AddControl2.md)

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddControl( _
   ByVal ID As System.Integer, _
   ByVal ControlType As System.Short, _
   ByVal Caption As System.String, _
   ByVal LeftAlign As System.Short, _
   ByVal Options As System.Integer, _
   ByVal Tip As System.String _
) As PropertyManagerPageControl
```

```

Dim instance As IPropertyManagerPageTab
Dim ID As System.Integer
Dim ControlType As System.Short
Dim Caption As System.String
Dim LeftAlign As System.Short
Dim Options As System.Integer
Dim Tip As System.String
Dim value As PropertyManagerPageControl
 
value = instance.IAddControl(ID, ControlType, Caption, LeftAlign, Options, Tip)
```

```

PropertyManagerPageControl IAddControl( 
   System.int ID,
   System.short ControlType,
   System.string Caption,
   System.short LeftAlign,
   System.int Options,
   System.string Tip
)
```

```

PropertyManagerPageControl^ IAddControl( 
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
:   Resource ID of this control

*ControlType*
:   Type of control as defined in [swPropertyManagerPageControlType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageControlType_e.html)

*Caption*
:   Caption of the control

*LeftAlign*
:   Left align property of this control as defined in [swPropertyManagerPageControlLeftAlign\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageControlLeftAlign_e.html)

*Options*
:   Options as defined in [swAddControlOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAddControlOptions_e.html) (see **Remarks**)

*Tip*
:   Tool tip text for the control

#### Return Value

Newly created [PropertyManager page tab control](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.md)

Remarks

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Show2.md) and [IPropertyManagerPage2::Close](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Close.md).

This method associates controls with a tab. When a user clicks a tab, controls associated with that tab are automatically shown and controls not associated with that tab are automatically hidden.

However, any controls added to a tab using [IPropertyManagerPage2::AddControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddControl.md) or [IPropertyManagerPage2::IAddControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~IAddControl.md) are not associated with the tab; you must still hide and show those controls. But, because the name of this method and its parameters are identical to IPropertyManagerPage2::AddControl or IPropertyManagerPage2::IAddControl, switching to this method and cleaning up your handler code should be easy.

To add a control to a group box associated with a tab, add the controls from the [group box](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~IAddGroupBox.md). Only use this method to add controls not associated with group boxes.

When you specify swControlOptions\_SmallGapAbove for the Options parameter, gap is used between a new control and the previous control that is smaller than the typical gap.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageTab Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab.md)  
[IPropertyManagerPageTab Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab_members.md)  
[IPropertyManagerPageTab::AddControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab~AddControl.md)
