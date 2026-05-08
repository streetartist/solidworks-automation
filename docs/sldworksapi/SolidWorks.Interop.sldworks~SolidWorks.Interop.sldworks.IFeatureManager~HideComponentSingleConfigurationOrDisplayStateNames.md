# HideComponentSingleConfigurationOrDisplayStateNames Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~HideComponentSingleConfigurationOrDisplayStateNames`

Gets or sets whether to hide a component's only configuration or display state.
Gets or sets whether to hide a component's only configuration or display state.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property HideComponentSingleConfigurationOrDisplayStateNames As System.Boolean
```

```

Dim instance As IFeatureManager
Dim value As System.Boolean
 
instance.HideComponentSingleConfigurationOrDisplayStateNames = value
 
value = instance.HideComponentSingleConfigurationOrDisplayStateNames
```

```

System.bool HideComponentSingleConfigurationOrDisplayStateNames {get; set;}
```

```

property System.bool HideComponentSingleConfigurationOrDisplayStateNames {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to hide the single configuration or display state, false to display it

Remarks

This property:

- Works in both SOLIDWORKS Desktop and [SOLIDWORKS Connected](sldworksapiprogguide.chm::/Overview/SOLIDWORKS_Connected.htm).
- Is analogous to the **Do not show Configuration or Display State name if only one exists** check box on the Component Name and Description dialog that appears after right-clicking on the top-level component in the FeatureManager design tree and selecting **Tree Display > Component Name and Description**.

Example

See the [IFeatureManager::SetComponentIdentifiers](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetComponentIdentifiers.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
