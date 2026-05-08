# FeatureXpert Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FeatureXpert`

Executes FeatureXpert, powered by SOLIDWORKS Intelligent Feature Technology ( SWIFT), in parts.
Executes FeatureXpert, powered by SOLIDWORKS Intelligent Feature Technology ( SWIFT), in parts.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub FeatureXpert() 
```

```

Dim instance As IPartDoc
 
instance.FeatureXpert()
```

```

void FeatureXpert()
```

```

void FeatureXpert(); 
```

Remarks

FeatureXpert works behind the scenes to resolve feature errors in [constant radius fillets](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md), [neutral plane drafts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.md), and [reference planes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md).

You must enable the FeatureXpert system option before using this method:

swApp.SetUserPreferenceToggle swUserEnableAutoFix, True

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IFeatureManager::DraftXpertChange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~DraftXpertChange.md)  
[IFeatureManager::DraftXpertRemove Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~DraftXpertRemove.md)
