# AddGroupBox Method (IPropertyManagerPage2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddGroupBox`

Adds a group box to a PropertyManager page.
Adds a group box to a PropertyManager page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddGroupBox( _
   ByVal ID As System.Integer, _
   ByVal Caption As System.String, _
   ByVal Options As System.Integer _
) As System.Object
```

```

Dim instance As IPropertyManagerPage2
Dim ID As System.Integer
Dim Caption As System.String
Dim Options As System.Integer
Dim value As System.Object
 
value = instance.AddGroupBox(ID, Caption, Options)
```

```

System.object AddGroupBox( 
   System.int ID,
   System.string Caption,
   System.int Options
)
```

```

System.Object^ AddGroupBox( 
   System.int ID,
   System.String^ Caption,
   System.int Options
) 
```

#### Parameters

*ID*
:   Resource ID of the group box

*Caption*
:   Title of the group box

*Options*
:   Options as defined in [swAddGroupBoxOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAddGroupBoxOptions_e.html)

#### Return Value

Newly created [PropertyManager page group box](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup.md)

Remarks

Use this method to set properties on the PropertyManager page before the page is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Show2.md) and [PropertyManagerPage2::Close](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Close.md) for details.

To change the title of an existing group box, use [IPropertyManagerPageGroup::Caption](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup~Caption.md).

Example

See the [IPropertyManagerPage2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md) examples.

Example

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md)  
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.md)  
[IPropertyManagerPage2::IAddGroupBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~IAddGroupBox.md)
