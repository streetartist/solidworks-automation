# IsDirty Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IsDirty`

Gets whether this configuration is dirty (i.e., needs to be updated).
Gets whether this configuration is dirty (i.e., needs to be updated).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsDirty() As System.Boolean
```

```

Dim instance As IConfiguration
Dim value As System.Boolean
 
value = instance.IsDirty()
```

```

System.bool IsDirty()
```

```

System.bool IsDirty(); 
```

#### Return Value

True if the configuration is dirty, false if not

Remarks

If the configuration is dirty, then you can update its date by:

1. [Activating the configuration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowConfiguration2.md).
2. [Saving the document](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Save3.md) while the configuration is active.

Example

[Are the Assembly Configurations Loaded (C#)](Are_the_Assembly_Configurations_Loaded_Example_CSharp.htm)  
[Are the Assembly Configurations Loaded (VB.NET)](Are_the_Assembly_Configurations_Loaded_Example_VBNET.htm)  
[Are the Assembly Configurations Loaded (VBA)](Are_the_Assembly_Configurations_Loaded_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::NeedsRebuild Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~NeedsRebuild.md)  
[IModelDoc2::GetSaveFlag Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetSaveFlag.md)  
[IConfigurationManager::ActiveConfiguration Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.md)
