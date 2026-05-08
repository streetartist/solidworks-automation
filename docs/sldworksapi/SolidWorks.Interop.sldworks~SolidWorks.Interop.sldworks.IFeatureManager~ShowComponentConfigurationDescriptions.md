# ShowComponentConfigurationDescriptions Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowComponentConfigurationDescriptions`

Gets or sets whether to show the active configuration's component configuration descriptions in the FeatureManager design tree.
Gets or sets whether to show the active configuration's component configuration descriptions in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowComponentConfigurationDescriptions As System.Boolean
```

```

Dim instance As IFeatureManager
Dim value As System.Boolean
 
instance.ShowComponentConfigurationDescriptions = value
 
value = instance.ShowComponentConfigurationDescriptions
```

```

System.bool ShowComponentConfigurationDescriptions {get; set;}
```

```

property System.bool ShowComponentConfigurationDescriptions {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True shows the active configuration's component configuration descriptions, false does not

Example

[Show Components and Component Configurations Names and Descriptions (VBA)](Show_Components_and_Component_Configurations_Names_and_Descriptions_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::ShowComponentConfigurationNames Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowComponentConfigurationNames.md)  
[IFeatureManager::ShowComponentDescriptions Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowComponentDescriptions.md)  
[IFeatureManager::ShowComponentNames Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowComponentNames.md)  
[IFeatureManager::ShowFeatureDescription Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowFeatureDescription.md)  
[IFeatureManager::ShowFeatureName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowFeatureName.md)  
[IFeatureManager::ShowDisplayStateNames Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowDisplayStateNames.md)
