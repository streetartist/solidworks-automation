# CreateFeatureMgrView2 Method (IModelViewManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrView2`

Creates a new view (tab) in this FeatureManager design tree.
Creates a new view (tab) in this FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateFeatureMgrView2( _
   ByVal BitMapFile As System.String, _
   ByVal ToolTip As System.String, _
   ByVal WhichPane As System.Integer _
) As FeatMgrView
```

```

Dim instance As IModelViewManager
Dim BitMapFile As System.String
Dim ToolTip As System.String
Dim WhichPane As System.Integer
Dim value As FeatMgrView
 
value = instance.CreateFeatureMgrView2(BitMapFile, ToolTip, WhichPane)
```

```

FeatMgrView CreateFeatureMgrView2( 
   System.string BitMapFile,
   System.string ToolTip,
   System.int WhichPane
)
```

```

FeatMgrView^ CreateFeatureMgrView2( 
   System.String^ BitMapFile,
   System.String^ ToolTip,
   System.int WhichPane
) 
```

#### Parameters

*BitMapFile*
:   Bitmap file that you want to use for the tab

*ToolTip*
:   Text for the ToolTip

*WhichPane*
:   Pane to use as defined in [swFeatMgrPane\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatMgrPane_e.html)

#### Return Value

Pointer to the new [tab](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView.md)

Remarks

This method provides the ability to place your newly created Feature Manager tab on either the top or bottom pane. The pane may or may not be visible. However, the tab is added to the specified pane.

Under certain conditions, for example while the Surface, Extend command is active in the user interface, SOLIDWORKS locks the bottom pane and does not allow the activation of any other tab. If your application needs the ability to activate your new tab at all times, consider adding it either to the top pane or to both panes. If you add it to the top pane only, it may not be apparent to the user until the top pane is made visible.

If you receive a non-NULL return value, you can use [IFeatMgrView::GetFeatMgrViewWnd](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~GetFeatMgrViewWnd.md) or [IFeatureMgrView::GetFeatMgrViewWndx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~GetFeatMgrViewWndx64.md) to get the new view handle. Because the view created is empty, you can use the new view handle in combination with standard MFC calls to draw, as desired, into the view.

The FeatureManager design tree view added to this document is not persistent. In other words, the FeatureManager design tree view is not stored with this document and must be recreated upon reloading the document.

This method automatically sets up to receive FeatMgrView [ActivateNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DFeatMgrViewEvents_ActivateNotifyEventHandler.md) and [DeactivateNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DFeatMgrViewEvents_DeactivateNotifyEventHandler.md) events. On the appropriate notification, you can call [IModelDoc2::DeleteFeatureMgrView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteFeatureMgrView.md) or [IModelDocExtension::DeleteFeatureMgrViewx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteFeatureMgrViewx64.md) to clean up and delete your view.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md)  
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.md)  
[IModelViewManager::CreateFeatureMgrControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl.md)  
[IModelViewManager::CreateFeatureMgrControl2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl2.md)  
[IModelViewManager::CreateFeatureMgrControl3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl3.md)
