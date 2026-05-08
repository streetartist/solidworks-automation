# UpgradeLegacyCThreads Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpgradeLegacyCThreads`

Upgrades cosmetic thread features in this legacy model to the latest cosmetic thread architecture.
Upgrades cosmetic thread features in this legacy model to the latest cosmetic thread architecture.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function UpgradeLegacyCThreads() As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim value As System.Boolean
 
value = instance.UpgradeLegacyCThreads()
```

```

System.bool UpgradeLegacyCThreads()
```

```

System.bool UpgradeLegacyCThreads(); 
```

#### Return Value

True if cosmetic threads upgraded successfully in this legacy model, false if not

Remarks

This method:

- is valid only if the system option allowing the upgrade of legacy files containing cosmetic threads is selected.
- corresponds to the user-interface command, *feature\_manager\_design\_tree\_top\_node* **RMB** **> Upgrade cosmetic thread features**.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::HasLegacyCThreads Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasLegacyCThreads.md)
