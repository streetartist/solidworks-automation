# EnableFeatureTreeWindow Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EnableFeatureTreeWindow`

Gets or sets whether the FeatureManager design tree is enabled or not.
Gets or sets whether the FeatureManager design tree is enabled or not.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EnableFeatureTreeWindow As System.Boolean
```

```

Dim instance As IFeatureManager
Dim value As System.Boolean
 
instance.EnableFeatureTreeWindow = value
 
value = instance.EnableFeatureTreeWindow
```

```

System.bool EnableFeatureTreeWindow {get; set;}
```

```

property System.bool EnableFeatureTreeWindow {
   System.bool get();
   void set (    System.bool value);
}
```

Remarks

Use this property with [IFeatureManager::EnableFeatureTree](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EnableFeatureTree.md), which temporarily enables or disables the FeatureManager design tree update when an add-in is running a series of operations.  

While the FeatureManager design tree is disabled and not being updated, the FeatureManager tree may become out of date with what is actually in the model. If an interactive user attempts to interact with the FeatureManager design tree while it is in this out-of-date state, problems could occur. Normally, this should not happen because the add-in should only be disabling the FeatureManager design tree update temporarily and then enabling it immediately after the series of operations complete. However, if there is any possibility that an interactive user could interact with the FeatureManager design tree, then use FeatureManager::EnableFeatureTreeWindow, which prohibits any user interaction with the FeatureManager design tree because the control is disabled.

Just as with the IFeatureManager::EnableFeatureTree property, this property is meant to be used for temporary disabling. If it is necessary to disable the FeatureManager design tree control, then it should only be disabled while the add-in is performing some series of operations and enabled immediately after these operations complete. Do not to leave the FeatureManager design tree window disabled when control is returned to SOLIDWORKS, i.e., the interactive user.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::UpdateFeatureTree Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~UpdateFeatureTree.md)
