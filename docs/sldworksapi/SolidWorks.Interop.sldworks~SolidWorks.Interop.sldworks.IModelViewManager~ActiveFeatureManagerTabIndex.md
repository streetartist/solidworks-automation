# ActiveFeatureManagerTabIndex Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ActiveFeatureManagerTabIndex`

Gets or sets the index of the active tab in the Manager Pane.
Gets or sets the index of the active tab in the Manager Pane.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ActiveFeatureManagerTabIndex As System.Integer
```

```

Dim instance As IModelViewManager
Dim value As System.Integer
 
instance.ActiveFeatureManagerTabIndex = value
 
value = instance.ActiveFeatureManagerTabIndex
```

```

System.int ActiveFeatureManagerTabIndex {get; set;}
```

```

property System.int ActiveFeatureManagerTabIndex {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Index of the active tab in the Manager Pane

Example

[Change Active Tab in Manager Pane (C#)](Change_Active_Tab_in_Manager_Pane_Example_CSharp.htm)  
[Change Active Tab in Manager Pane (VB.NET)](Change_Active_Tab_in_Manager_Pane_Example_VBNET.htm)  
[Change Active Tab in Manager Pane (VBA)](Change_Active_Tab_in_Manager_Pane_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md)  
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.md)  
[IModelViewManager::FeatureManagerTabsVisible Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~FeatureManagerTabsVisible.md)  
[IModelViewManager::GetConfigurationManagerTabIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetConfigurationManagerTabIndex.md)  
[IModelViewManager::GetDimXpertManagerTabIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetDimXpertManagerTabIndex.md)  
[IModelViewManager::GetDisplayManagerTabIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetDisplayManagerTabIndex.md)  
[IModelViewManager::GetFeatureManagerTabs Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureManagerTabs.md)  
[IModelViewManager::GetFeatureManagerTreeTabIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureManagerTreeTabIndex.md)  
[IModelViewManager::GetPropertyManagerTabIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetPropertyManagerTabIndex.md)  
[DAssemblyDocEvents\_FeatureManagerTabActivatedNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FeatureManagerTabActivatedNotifyEventHandler.md)  
[DAssemblyDocEvents\_FeatureManagerTabActivatedPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler.md)  
[DDrawingDocEvents\_FeatureManagerTabActivatedNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FeatureManagerTabActivatedNotifyEventHandler.md)  
[DDrawingDocEvents\_FeatureManagerTabActivatedPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler.md)  
[DPartDocEvents\_FeatureManagerTabActivatedNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FeatureManagerTabActivatedNotifyEventHandler.md)  
[DPartDocEvents\_FeatureManagerTabActivatedPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler.md)
