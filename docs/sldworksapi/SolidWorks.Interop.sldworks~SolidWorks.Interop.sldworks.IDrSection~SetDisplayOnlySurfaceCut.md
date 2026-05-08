# SetDisplayOnlySurfaceCut Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetDisplayOnlySurfaceCut`

Sets whether to display only the surface cut by the section line.
Sets whether to display only the surface cut by the section line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetDisplayOnlySurfaceCut( _
   ByVal Display As System.Boolean _
) 
```

```

Dim instance As IDrSection
Dim Display As System.Boolean
 
instance.SetDisplayOnlySurfaceCut(Display)
```

```

void SetDisplayOnlySurfaceCut( 
   System.bool Display
)
```

```

void SetDisplayOnlySurfaceCut( 
   System.bool Display
) 
```

#### Parameters

*Display*
:   True displays only the surface cut by the section line, false does not

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
[IDrSection::GetDisplayOnlySurfaceCut Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetDisplayOnlySurfaceCut.md)  
[IDrSection::CutSurfaceBodies Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~CutSurfaceBodies.md)
