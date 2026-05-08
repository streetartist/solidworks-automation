# AddControl3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddControl3`

Adds a tab to this model view that supports tab traversal using the specified ActiveX control.
Adds a tab to this model view that supports tab traversal using the specified ActiveX control.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddControl3( _
   ByVal Name As System.String, _
   ByVal ControlName As System.String, _
   ByVal BstrLicKey As System.String, _
   ByVal SplitWindow As System.Boolean _
) As System.Object
```

```

Dim instance As IModelViewManager
Dim Name As System.String
Dim ControlName As System.String
Dim BstrLicKey As System.String
Dim SplitWindow As System.Boolean
Dim value As System.Object
 
value = instance.AddControl3(Name, ControlName, BstrLicKey, SplitWindow)
```

```

System.object AddControl3( 
   System.string Name,
   System.string ControlName,
   System.string BstrLicKey,
   System.bool SplitWindow
)
```

```

System.Object^ AddControl3( 
   System.String^ Name,
   System.String^ ControlName,
   System.String^ BstrLicKey,
   System.bool SplitWindow
) 
```

#### Parameters

*Name*
:   User-defined label that appears on the tab

*ControlName*
:   Name or class ID for the ActiveX control

*BstrLicKey*
:   Optional license key; this data is needed to create ActiveX controls that require a runtime license key; if the ActiveX control supports licensing, then provide a license key for the creation of the ActiveX control; default value is NULL

*SplitWindow*
:   True to add a splitter window, false to not

#### Return Value

Pointer to the new ActiveX control

Remarks

If your ActiveX control does not need tab traversal support, then use [IModelViewManager::AddControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddControl.md).

This method sets the class ID and license key information for the ActiveX control when the API PropertyManager page is shown and the ActiveX control is created. The controlName argument can be either the name of the control (ProgID) or the class ID (CLSID), for example, "MSCAL.calendar" or "{8E27C92B-1264-101C-8A2F-040224009C02}". Both provide the calendar protocol. You can obtain these strings using a combination of the Microsoft OLE/COM Object Viewer and the registry editor.

For example:

' ProgID

bRet = m\_pActiveXControl.SetClass("MSCAL.Calendar", "")

bRet = m\_pActiveXControl2.SetClass("MSComctlLib.ListViewCtrl", "")

' CLSID

bRet = m\_pActiveXControl.SetClass("{8E27C92B-1264-101C-8A2F-040224009C02}", "")

bRet = m\_pActiveXControl2.SetClass("{BDD1F04B-858B-11D1-B16A-00C0F0283628}", "")

Two or more tabs cannot be added with the same name.

To delete a tab created by this method, use [IModelViewManager::DeleteControlTab](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DeleteControlTab.md). Each use of IModelViewManager::AddControl3 must use a corresponding IModelViewManager::DeleteControlTab before exiting your macro or application.

See also [Keystrokes and Accelerator Keys in ActiveX Modeless Dialogs and PropertyManager Pages](sldworksapiprogguide.chm::/overview/Keystrokes_and_Accelerator_Keys_and_ActiveX_Modeless_Dialogs_and_PropertyManager_Pages.htm).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md)  
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.md)  
[IModelViewManager::ActivateControlTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ActivateControlTab.md)  
[IModelViewManager::ActivateModelTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ActivateModelTab.md)  
[IModelViewManager::GetControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetControl.md)  
[IModelViewManager::IGetControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~IGetControl.md)  
[IModelViewManager::IsControlTabActive Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~IsControlTabActive.md)  
[IModelViewManager::IsModelTabActive Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~IsModelTabActive.md)  
[IModelViewManager::DeleteControlTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DeleteControlTab.md)  
[IModelViewManager::CreateFeatureMgrView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrView2.md)
