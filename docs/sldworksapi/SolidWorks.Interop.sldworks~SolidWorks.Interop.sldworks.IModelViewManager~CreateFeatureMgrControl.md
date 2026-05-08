# CreateFeatureMgrControl Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl`

Obsolete. Superseded by IModelViewManager::CreateFeatureMgrControl2.
Obsolete. Superseded by [IModelViewManager::CreateFeatureMgrControl2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateFeatureMgrControl( _
   ByVal PPicture As System.Object, _
   ByVal Class As System.String, _
   ByVal LicKey As System.String, _
   ByVal ToolTip As System.String, _
   ByVal WhichPane As System.Integer _
) As FeatMgrView
```

```

Dim instance As IModelViewManager
Dim PPicture As System.Object
Dim Class As System.String
Dim LicKey As System.String
Dim ToolTip As System.String
Dim WhichPane As System.Integer
Dim value As FeatMgrView
 
value = instance.CreateFeatureMgrControl(PPicture, Class, LicKey, ToolTip, WhichPane)
```

```

FeatMgrView CreateFeatureMgrControl( 
   System.object PPicture,
   System.string Class,
   System.string LicKey,
   System.string ToolTip,
   System.int WhichPane
)
```

```

FeatMgrView^ CreateFeatureMgrControl( 
   System.Object^ PPicture,
   System.String^ Class,
   System.String^ LicKey,
   System.String^ ToolTip,
   System.int WhichPane
) 
```

#### Parameters

*PPicture*
:   Pointer to the bitmap that you want to use for the tab

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

This method is not supported in applications written in .NET languages.

The user can click the tab to activate an ActiveX control.

This method references the IPictureDisp interface. Use [IModelViewManager::CreateFeatureMgrControl2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl2.md) to specify the fully qualified path to the bitmap file on disk. Use [IModelViewManager::CreateFeatureMgrControl3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl3.md) if tab traversal support is needed and specify a fully qualified path to the bitmap file on disk.

This method sets the class ID and license key information for the ActiveX control when the API PropertyManager page is shown and the ActiveX control is created. The Class argument can be either the name of the control (ProgID) or the class ID (CLSID), for example, "MSCAL.calendar" or "{8E27C92B-1264-101C-8A2F-040224009C02}". Both provide the calendar protocol. You can obtain these strings using a combination of the Microsoft OLE/COM Object Viewer and the registry editor.

For example:

' ProgID

bRet = m\_pActiveXControl.SetClass("MSCAL.Calendar", "")

bRet = m\_pActiveXControl2.SetClass("MSComctlLib.ListViewCtrl", "")

' CLSID

bRet = m\_pActiveXControl.SetClass("{8E27C92B-1264-101C-8A2F-040224009C02}", "")

bRet = m\_pActiveXControl2.SetClass("{BDD1F04B-858B-11D1-B16A-00C0F0283628}", "")

See also [Keystrokes and Accelerator Keys in ActiveX Modeless Dialogs and PropertyManager Pages](sldworksapiprogguide.chm::/overview/Keystrokes_and_Accelerator_Keys_and_ActiveX_Modeless_Dialogs_and_PropertyManager_Pages.htm).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md)  
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.md)
