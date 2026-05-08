# GetAutoHatch Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetAutoHatch`

Gets whether auto hatching is enabled for the section view resulting from this section cut.
Gets whether auto hatching is enabled for the section view resulting from this section cut.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAutoHatch() As System.Boolean
```

```

Dim instance As IDrSection
Dim value As System.Boolean
 
value = instance.GetAutoHatch()
```

```

System.bool GetAutoHatch()
```

```

System.bool GetAutoHatch(); 
```

#### Return Value

True if auto hatching is enabled for the section view, false if it is disabled

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
[IDrSection::SetAutoHatch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetAutoHatch.md)  
[IDrSection::ScaleHatchPattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ScaleHatchPattern.md)
