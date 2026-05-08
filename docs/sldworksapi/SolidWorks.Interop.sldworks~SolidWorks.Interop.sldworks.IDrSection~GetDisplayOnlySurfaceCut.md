# GetDisplayOnlySurfaceCut Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetDisplayOnlySurfaceCut`

Gets whether to display only the surface cut by the section line.
Gets whether to display only the surface cut by the section line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDisplayOnlySurfaceCut() As System.Boolean
```

```

Dim instance As IDrSection
Dim value As System.Boolean
 
value = instance.GetDisplayOnlySurfaceCut()
```

```

System.bool GetDisplayOnlySurfaceCut()
```

```

System.bool GetDisplayOnlySurfaceCut(); 
```

#### Return Value

True to display only the surface cut by the section line, false to not

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
[IDrSection::SetDisplayOnlySurfaceCut Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetDisplayOnlySurfaceCut.md)  
[IDrSection::CutSurfaceBodies Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~CutSurfaceBodies.md)
