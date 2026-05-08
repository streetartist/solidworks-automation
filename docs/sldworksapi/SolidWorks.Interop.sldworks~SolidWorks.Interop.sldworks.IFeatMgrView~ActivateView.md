# ActivateView Method (IFeatMgrView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~ActivateView`

Activates this view in the FeatureManager design tree.
Activates this view in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ActivateView() As System.Integer
```

```

Dim instance As IFeatMgrView
Dim value As System.Integer
 
value = instance.ActivateView()
```

```

System.int ActivateView()
```

```

System.int ActivateView(); 
```

#### Return Value

Pane on which to activate this tab as defined in [swFeatMgrPane\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatMgrPane_e.html)

Example

[Add ActiveX Tabs to FeatureManager Design Tree (C#)](Add_ActiveX_Tabs_to_FeatureManager_Design_Tree_Example_CSharp.htm)  
[Add ActiveX Tabs to FeatureManager Design Tree (VB.NET)](Add_ActiveX_Tabs_to_FeatureManager_Design_Tree_Example_VBNET.htm)  
[Add ActiveX Tabs to FeatureManager Design Tree (VBA)](Add_ActiveX_Tabs_to_FeatureManager_Design_Tree_Example_VB.htm)  
[Add .NET Controls to SOLIDWORKS Using an Add-in (C#)](Add_.NET_Controls_to_SOLIDWORKS_Using_an_Add-in_Example_CSharp.htm)  
[Add .NET Controls to SOLIDWORKS using an Add-in (VB.NET)](Add_.NET_Controls_to_SolidWorks_Using_an_Add-in_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatMgrView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView.md)  
[IFeatMgrView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView_members.md)  
[IFeatMgrView::DeActivateView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~DeActivateView.md)  
[IFeatMgrView::DeleteView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~DeleteView.md)  
[IModelViewManager::AddControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddControl.md)  
[IModelViewManager::AddControl3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddControl3.md)  
[IModelViewManager::CreateFeatureMgrControl2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl2.md)  
[IModelViewManager::CreateFeatureMgrControl3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl3.md)
