# IsSpeedPak Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSpeedPak`

Gets whether the active configuration for this component is SpeedPak.
Gets whether the active configuration for this component is SpeedPak.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property IsSpeedPak As System.Boolean
```

```

Dim instance As IComponent2
Dim value As System.Boolean
 
value = instance.IsSpeedPak
```

```

System.bool IsSpeedPak {get;}
```

```

property System.bool IsSpeedPak {
   System.bool get();
}
```

#### Property Value

True if the active configuration for this component is SpeedPak, false if not

Example

[Create SpeedPak for Subassemblies (C#)](Create_SpeedPak_for_Subassemblies_Example_CSharp.htm)  
[Create SpeedPak for Subassemblies (VB.NET)](Create_SpeedPak_for_Subassemblies_Example_VBNET.htm)  
[Create SpeedPak for Subassemblies (VBA)](Create_SpeedPak_for_Subassemblies_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IAssemblyDoc::CreateSpeedPak Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateSpeedPak.md)  
[IAssemblyDoc::SetSpeedPakConfigurations Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetSpeedPakConfigurations.md)  
[IAssemblyDoc::SetSpeedPakToParent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetSpeedPakToParent.md)  
[IAssemblyDoc::UpdateSpeedPak Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateSpeedPak.md)  
[IAssemblyDoc::UseSpeedPak Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UseSpeedPak.md)  
[IConfiguration::IsSpeedPak Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IsSpeedPak.md)
