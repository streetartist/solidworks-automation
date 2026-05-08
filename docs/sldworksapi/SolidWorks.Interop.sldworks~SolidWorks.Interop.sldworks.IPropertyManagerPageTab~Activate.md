# Activate Method (IPropertyManagerPageTab)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab~Activate`

Activates this tab in the PropertyManager page.
Activates this tab in the PropertyManager page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Activate() As System.Boolean
```

```

Dim instance As IPropertyManagerPageTab
Dim value As System.Boolean
 
value = instance.Activate()
```

```

System.bool Activate()
```

```

System.bool Activate(); 
```

#### Return Value

True if successful, false if not

Remarks

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Show2.md) and [IPropertyManagerPage2::Close](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Close.md).

Example

[Activate PropertyManager Page Tab (VBA)](Activate_Property_Manager_Page_Tab_Example_VB.htm)  
[Activate PropertyManager Page Tab (VB.NET)](Activate_Property_Manager_Page_Tab_Example_VBNET.htm)  
[Activate PropertyManager Page Tab (C#)](Activate_Property_Manager_Page_Tab_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageTab Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab.md)  
[IPropertyManagerPageTab Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab_members.md)
