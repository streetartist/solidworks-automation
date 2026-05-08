# CreateFeatureMgrControl4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl4`

Creates a new FeatureManager design tree view containing the specified ActiveX control with a tab that displays the specified scaleable icon.
Creates a new FeatureManager design tree view containing the specified ActiveX control with a tab that displays the specified scaleable icon.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateFeatureMgrControl4( _
   ByVal BitMapFileNames As System.Object, _
   ByVal Class As System.String, _
   ByVal LicKey As System.String, _
   ByVal ToolTip As System.String, _
   ByVal WhichPane As System.Integer _
) As FeatMgrView
```

```

Dim instance As IModelViewManager
Dim BitMapFileNames As System.Object
Dim Class As System.String
Dim LicKey As System.String
Dim ToolTip As System.String
Dim WhichPane As System.Integer
Dim value As FeatMgrView
 
value = instance.CreateFeatureMgrControl4(BitMapFileNames, Class, LicKey, ToolTip, WhichPane)
```

```

FeatMgrView CreateFeatureMgrControl4( 
   System.object BitMapFileNames,
   System.string Class,
   System.string LicKey,
   System.string ToolTip,
   System.int WhichPane
)
```

```

FeatMgrView^ CreateFeatureMgrControl4( 
   System.Object^ BitMapFileNames,
   System.String^ Class,
   System.String^ LicKey,
   System.String^ ToolTip,
   System.int WhichPane
) 
```

#### Parameters

*BitMapFileNames*
:   Array of fully qualified paths to three bitmap files, one for each size (small, medium, and large), to be used for the tab icon in different screen resolutions

*Class*
:   CLSID or ProgID for the ActiveX control (see **Remarks**)

*LicKey*
:   License key for the ActiveX control; empty string if unknown

*ToolTip*
:   Text to display when hovering over the tab icon

*WhichPane*
:   Pane where to add the tab as defined in [swFeatMgrPane\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatMgrPane_e.html) (see **Remarks**)

#### Return Value

Pointer to the new [tab](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView.md)

Remarks

To:

- Add a tab to the FeatureManager design tree, specify WhichPane with swFeatMgrPane\_e.FeatMgrPaneBottom.
- Add a tab to a split FeatureManager design tree, specify WhichPane with either swFeatMgrPane\_e.swFeatMgrPaneTop or swFeatMgrPane\_e.swFeatMgrPaneBottom. See [IModelDoc2::FeatureManagerSplitterPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureManagerSplitterPosition.md) for details on splitting and positioning the split panel bar in the FeatureManager design tree.
- Delete the tab created by this method, use [IFeatMgrView::DeleteView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~DeleteView.md).

Specify Class with either the ProgID or the CLSID of the registered ActiveX control. You can obtain these strings by searching for the registered ActiveX control in the registry editor.

For example, **RichEditCtrol.ocx** resides in **c:\Program files\SOLIDWORKS Corp\SOLIDWORKS\sldUtils**. It is registered during the SOLIDWORKS installation. When you search for **RichEditCtrl.ocx** in the registry, you find ProgID = GTSWRICHEDITCTRL.RichEditCtrlCtrl.1 and CLSID = {7632C33C-A935-48FF-84D9-F0F173EF543D}. Use either the registry's ActiveX ProgID or CLSID to specify Class. The ActiveX control library names displayed in the Object Browser may not be the same as the ActiveX control names in the registry. Do not use the Object Browser to specify Class.

See also [Keystrokes and Accelerator Keys in ActiveX Modeless Dialogs and PropertyManager Pages](sldworksapiprogguide.chm::/overview/Keystrokes_and_Accelerator_Keys_and_ActiveX_Modeless_Dialogs_and_PropertyManager_Pages.htm).

Example

[Add ActiveX Tab to FeatureManager Design Tree (VBA)](Add_ActiveX_Tab_to_FeatureManager_Design_Tree_Example_VB.htm)  
[Add ActiveX Tab to FeatureManager Design Tree (VB.NET)](Add_ActiveX_Tab_to_FeatureManager_Design_Tree_Example_VBNET.htm)  
[Add ActiveX Tab to FeatureManager Design Tree (C#)](Add_ActiveX_Tab_to_FeatureManager_Design_Tree_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md)  
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.md)  
[IModelViewManager::CreateFeatureMgrView2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrView2.md)  
[IModelViewManager::AddControl3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddControl3.md)
