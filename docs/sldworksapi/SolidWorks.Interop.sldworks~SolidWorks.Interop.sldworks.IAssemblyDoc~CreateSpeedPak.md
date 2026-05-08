# CreateSpeedPak Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateSpeedPak`

Creates the specified type of SpeedPak for the active configurations of the selected subassemblies in this assembly.
Creates the specified type of SpeedPak for the active configurations of the selected subassemblies in this assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateSpeedPak( _
   ByVal SpeedPakType As System.Integer _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim SpeedPakType As System.Integer
Dim value As System.Boolean
 
value = instance.CreateSpeedPak(SpeedPakType)
```

```

System.bool CreateSpeedPak( 
   System.int SpeedPakType
)
```

```

System.bool CreateSpeedPak( 
   System.int SpeedPakType
) 
```

#### Parameters

*SpeedPakType*
:   - 1 = Mated
    - 2 = Graphics

#### Return Value

True if SpeedPak is created for the active configurations of the selected subassemblies in this assembly, false if not

Remarks

If a selected subassembly already has SpeedPak, then calling this method again does not create another SpeedPak, regardless if the type of SpeedPak to create is different than the existing SpeedPak.

Example

[Create SpeedPak for Subassemblies (C#)](Create_SpeedPak_for_Subassemblies_Example_CSharp.htm)  
[Create SpeedPak for Subassemblies (VB.NET)](Create_SpeedPak_for_Subassemblies_Example_VBNET.htm)  
[Create SpeedPak for Subassemblies (VBA)](Create_SpeedPak_for_Subassemblies_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::SetSpeedPakConfigurations Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetSpeedPakConfigurations.md)  
[IAssemblyDoc::SetSpeedPakToParent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetSpeedPakToParent.md)  
[IAssemblyDoc::UpdateSpeedPak Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateSpeedPak.md)  
[IAssemblyDoc::UseSpeedPak Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UseSpeedPak.md)  
[IComponent2::IsSpeedPak Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSpeedPak.md)  
[IConfigurationManager::AddSpeedPak2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddSpeedPak2.md)
