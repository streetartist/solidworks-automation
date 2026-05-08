# AddControl2 Method (IPropertyManagerPage2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddControl2`

Adds a control to this PropertyManager page.
Adds a control to this PropertyManager page.

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

Dim instance As IPropertyManagerPage2
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
:   Resource ID of this control whose value is passed back to the add-in through the [IPropertyManagerPage2Handler9](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9.md) interface

*ControlType*
:   Type of control as defined in [swPropertyManagerPageControlType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageControlType_e.html)

*Caption*
:   Caption of this control

*LeftAlign*
:   Left alignment of this control as defined in [swPropertyManagerPageControlLeftAlign\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageControlLeftAlign_e.html)

*Options*
:   Options as defined in [swAddControlOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAddControlOptions_e.html) (see **Remarks**)

*Tip*
:   ToolTip for this control

#### Return Value

Newly created [PropertyManager page control](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.md)

Remarks

You can only use this method to set properties on the PropertyManager before the page is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Show2.md) and [IPropertyManagerPage2::Close](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Close.md).

To follow the SOLIDWORKS standards when designing a new PropertyManager page, it is a good idea to use [IPropertyManagerPage2::AddGroupBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddGroupBox.md) or [IPropertyManagerPage2::IAddGroupBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~IAddGroupBox.md) and [IPropertyManagerPageGroup::AddControl2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup~AddControl2.md) to add controls for the page inside group boxes.

When you specify swAddControlOptions\_e.swControlOptions\_SmallGapAbove for the Options parameter, the gap created between the new control and the previous control is smaller than a typical gap. Also, the control is hidden unless you specify swAddControlOptions\_e.swControlOptions\_Visible for the Options parameter. In the previous versions of this method, IPropertyManagerPage2::AddControl and IPropertyManagerPage2::IAddControl, the control was visible regardless if the Options parameter was set or not set to swAddControlOptions\_e.swControlOptions\_Visible.

Example

See the [IPropertyManagerPage2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md)  
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.md)
