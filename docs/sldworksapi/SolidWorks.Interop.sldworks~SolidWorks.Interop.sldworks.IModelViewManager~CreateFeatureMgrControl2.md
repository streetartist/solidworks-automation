# CreateFeatureMgrControl2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl2`

Obsolete. Superseded by IModelViewManager::CreateFeatureMgrControl3.
Obsolete. Superseded by [IModelViewManager::CreateFeatureMgrControl3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateFeatureMgrControl2( _
   ByVal BitMapFile As System.String, _
   ByVal Class As System.String, _
   ByVal LicKey As System.String, _
   ByVal ToolTip As System.String, _
   ByVal WhichPane As System.Integer _
) As FeatMgrView
```

```

Dim instance As IModelViewManager
Dim BitMapFile As System.String
Dim Class As System.String
Dim LicKey As System.String
Dim ToolTip As System.String
Dim WhichPane As System.Integer
Dim value As FeatMgrView
 
value = instance.CreateFeatureMgrControl2(BitMapFile, Class, LicKey, ToolTip, WhichPane)
```

```

FeatMgrView CreateFeatureMgrControl2( 
   System.string BitMapFile,
   System.string Class,
   System.string LicKey,
   System.string ToolTip,
   System.int WhichPane
)
```

```

FeatMgrView^ CreateFeatureMgrControl2( 
   System.String^ BitMapFile,
   System.String^ Class,
   System.String^ LicKey,
   System.String^ ToolTip,
   System.int WhichPane
) 
```

#### Parameters

*BitMapFile*
:   Fully qualified path to the bitmap file that you want to use for the tab

*Class*
:   Class ID for the ActiveX control

*LicKey*
:   License key for the ActiveX control

*ToolTip*
:   Text for the ToolTip

*WhichPane*
:   Pane to use as defined in [swFeatMgrPane\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatMgrPane_e.html)

#### Return Value

Pointer to the new [tab](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView.md)

Remarks

This method lets you add a tab for a registered ActiveX control to the FeatureManager design tree. A user can click the tab to activate the ActiveX control.

To add a tab to the FeatureManager design tree, specify swFeatMgrPane\_e.FeatMgrPaneBottom for WhichPane. To add a tab to a FeatureManager design tree that has been split, specify swFeatMgrPane\_e.swFeatMgrPaneTop and swFeatMgrPane\_e.swFeatMgrPaneBottom, respectively, for WhichPane. See [IModelDoc2::FeatureManagerSplitterPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureManagerSplitterPosition.md) for details on splitting and positioning the split panel bar on a split FeatureManager design tree.

To delete a tab created by this method, use [IFeatMgrView::DeleteView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~DeleteView.md).

Class can be either the name of the registered control (ProgID) or its class ID (CLSID), for example, "MSCAL.calendar" or "{8E27C92B-1264-101C-8A2F-040224009C02}".  You must obtain these strings by searching for the registered ActiveX control in the registry editor. The ActiveX control library names displayed in the Object Browser may not be the same as the ActiveX control names in the registry. Do not use the Object Browser to specify Class.

See also [Keystrokes and Accelerator Keys in ActiveX Modeless Dialogs and PropertyManager Pages](sldworksapiprogguide.chm::/overview/Keystrokes_and_Accelerator_Keys_and_ActiveX_Modeless_Dialogs_and_PropertyManager_Pages.htm).

Example

[Add ActiveX Tabs to FeatureManager Design Tree (C#)](Add_ActiveX_Tabs_to_FeatureManager_Design_Tree_Example_CSharp.htm)  
[Add ActiveX Tabs to FeatureManager Design Tree (VB.NET)](Add_ActiveX_Tabs_to_FeatureManager_Design_Tree_Example_VBNET.htm)  
[Add ActiveX Tabs to FeatureManager Design Tree (VBA)](Add_ActiveX_Tabs_to_FeatureManager_Design_Tree_Example_VB.htm)  
[Split FeatureManager Design Tree and Position Splitter (C#)](Split_FeatureManager_Design_Tree_and_Position_Splitter_Example_CSharp.htm)  
[Split FeatureManager Design Tree and Position Splitter (VB.NET)](Split_FeatureManager_Design_Tree_and_Position_Splitter_Example_VBNET.htm)  
[Split FeatureManager Design Tree and Position Splitter (VBA)](Split_FeatureManager_Design_Tree_and_Position_Splitter_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md)  
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.md)  
[IModelViewManager::CreateFeatureMgrView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrView2.md)
