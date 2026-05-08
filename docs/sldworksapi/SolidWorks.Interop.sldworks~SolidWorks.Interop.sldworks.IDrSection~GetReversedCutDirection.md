# GetReversedCutDirection Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetReversedCutDirection`

Gets whether the section cut direction is reversed from the default direction.
Gets whether the section cut direction is reversed from the default direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetReversedCutDirection() As System.Boolean
```

```

Dim instance As IDrSection
Dim value As System.Boolean
 
value = instance.GetReversedCutDirection()
```

```

System.bool GetReversedCutDirection()
```

```

System.bool GetReversedCutDirection(); 
```

#### Return Value

True if the section cut direction is reversed from the default, false if it is not

Example

[Create Section View and Get Some Data (C#)](Create_Section_View_and_Get_Some_Data_Example_CSharp.htm)  
[Create Section View and Get Some Data (VB.NET)](Create_Section_View_and_Get_Some_Data_Example_VBNET.htm)  
[Create Section View and Get Some Data (VBA)](Create_Section_View_and_Get_Some_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md)  
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.md)  
[IDrSection::SetPartialSection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetPartialSection.md)
