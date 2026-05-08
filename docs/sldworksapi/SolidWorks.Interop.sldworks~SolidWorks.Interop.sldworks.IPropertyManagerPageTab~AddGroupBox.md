# AddGroupBox Method (IPropertyManagerPageTab)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab~AddGroupBox`

Adds a group box to this tab on a PropertyManager page.
Adds a group box to this tab on a PropertyManager page.

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

Dim instance As IPropertyManagerPageTab
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

Newly created [PropertyManager Page group box](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup.md)

Remarks

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Show2.md) and [IPropertyManagerPage2::Close](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Close.md).

To change the title of an existing group box, use [IPropertyManagerPageTab::Caption](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab~Caption.md).

Example

See the [IPropertyManagerPage2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageTab Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab.md)  
[IPropertyManagerPageTab Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab_members.md)  
[IPropertyManagerPageTab::IAddGroupBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab~IAddGroupBox.md)
