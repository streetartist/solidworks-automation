# FeatureManagerTabsVisible Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~FeatureManagerTabsVisible`

Gets or sets whether all of the tabs in the Manager Pane are visible.
Gets or sets whether all of the tabs in the Manager Pane are visible.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FeatureManagerTabsVisible As System.Boolean
```

```

Dim instance As IModelViewManager
Dim value As System.Boolean
 
instance.FeatureManagerTabsVisible = value
 
value = instance.FeatureManagerTabsVisible
```

```

System.bool FeatureManagerTabsVisible {get; set;}
```

```

property System.bool FeatureManagerTabsVisible {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if all of the tabs in the Manager Pane are visible, false if none of the tabs in the Manager Pane are visible

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md)  
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.md)  
[IModelDocExtension::HideFeatureManager Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HideFeatureManager.md)  
[IModelViewManager::GetConfigurationManagerTabIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetConfigurationManagerTabIndex.md)  
[IModelViewManager::GetDimXpertManagerTabIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetDimXpertManagerTabIndex.md)  
[IModelViewManager::GetDisplayManagerTabIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetDisplayManagerTabIndex.md)  
[IModelViewManager::GetFeatureManagerTabs Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureManagerTabs.md)  
[IModelViewManager::GetFeatureManagerTreeTabIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureManagerTreeTabIndex.md)  
[IModelViewManager::GetPropertyManagerTabIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetPropertyManagerTabIndex.md)  
[IModelViewManager::ActiveFeatureManagerTabIndex Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ActiveFeatureManagerTabIndex.md)
