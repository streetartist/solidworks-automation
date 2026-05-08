# SetFocus Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetFocus`

Sets focus on the specified control on this PropertyManager page.
Sets focus on the specified control on this PropertyManager page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetFocus( _
   ByVal ID As System.Integer _
) As System.Boolean
```

```

Dim instance As IPropertyManagerPage2
Dim ID As System.Integer
Dim value As System.Boolean
 
value = instance.SetFocus(ID)
```

```

System.bool SetFocus( 
   System.int ID
)
```

```

System.bool SetFocus( 
   System.int ID
) 
```

#### Parameters

*ID*
:   User-defined ID of the control where to set focus

#### Return Value

True if focus is set on the control, false if not

Example

[Set Focus on PropertyManager Page Control (C#)](Set_Focus_on_PropertyManager_Page_Control_Example_CSharp.htm)  
[Set Focus on PropertyManager Page Control (VB.NET)](Set_Focus_on_PropertyManager_Page_Control_Example_VBNET.htm)  
[Set Focus on PropertyManager Page Control (VBA)](Set_Focus_on_PropertyManager_Page_Control_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md)  
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.md)  
[IPropertyManagerPage2::GetFocus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~GetFocus.md)
