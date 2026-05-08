# IAddGroupBox Method (IPropertyManagerPage2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~IAddGroupBox`

Adds a group box to a PropertyManager page.
Adds a group box to a PropertyManager page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddGroupBox( _
   ByVal ID As System.Integer, _
   ByVal Caption As System.String, _
   ByVal Options As System.Integer _
) As PropertyManagerPageGroup
```

```

Dim instance As IPropertyManagerPage2
Dim ID As System.Integer
Dim Caption As System.String
Dim Options As System.Integer
Dim value As PropertyManagerPageGroup
 
value = instance.IAddGroupBox(ID, Caption, Options)
```

```

PropertyManagerPageGroup IAddGroupBox( 
   System.int ID,
   System.string Caption,
   System.int Options
)
```

```

PropertyManagerPageGroup^ IAddGroupBox( 
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

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md)  
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.md)  
[IPropertyManagerPage2::AddGroupBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddGroupBox.md)
