# RemoveMarkForAllConfigurations Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~RemoveMarkForAllConfigurations`

Remove all marks indicating whether configurations need to be rebuilt and their configuration data saved every time the model document is saved.
Remove all marks indicating whether configurations need to be rebuilt and their configuration data saved every time the model document is saved.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveMarkForAllConfigurations() As System.Boolean
```

```

Dim instance As IConfigurationManager
Dim value As System.Boolean
 
value = instance.RemoveMarkForAllConfigurations()
```

```

System.bool RemoveMarkForAllConfigurations()
```

```

System.bool RemoveMarkForAllConfigurations(); 
```

#### Return Value

True if marks removed successfully, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.md)  
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.md)  
[IConfigurationManager::AddRebuildSaveMark Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddRebuildSaveMark.md)
