# UpgradeLegacyCustomProperties Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpgradeLegacyCustomProperties`

Upgrades custom properties in this legacy (created prior to SOLIDWORKS 2018) model to the latest custom properties architecture.
Upgrades custom properties in this legacy (created prior to SOLIDWORKS 2018) model to the latest custom properties architecture.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function UpgradeLegacyCustomProperties( _
   ByVal UpgradeAllAssemComps As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim UpgradeAllAssemComps As System.Boolean
Dim value As System.Boolean
 
value = instance.UpgradeLegacyCustomProperties(UpgradeAllAssemComps)
```

```

System.bool UpgradeLegacyCustomProperties( 
   System.bool UpgradeAllAssemComps
)
```

```

System.bool UpgradeLegacyCustomProperties( 
   System.bool UpgradeAllAssemComps
) 
```

#### Parameters

*UpgradeAllAssemComps*
:   True to upgrade custom properties of this top-level assembly and all of its components, false to upgrade custom properties of this top-level assembly only

#### Return Value

True if custom properties are successfully upgraded, false if not

Remarks

This method is valid only for parts, assemblies, and drawings:

- created prior to 2018.
- opened in resolved mode.
- corresponds to the user-interface command, *feature\_manager\_design\_tree\_top\_node* **RMB** **> Upgrade custom properties**.

This method upgrades the custom properties of:

- parent parts only, not derived parts
- drawings, but not models in drawing views
- weldment cutlists
- (optionally) all components in assemblies

After running this method, you:

- must rebuild configurations to have their custom properties updated.
- cannot return to the old custom properties architecture.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
