# ActivateControlTab Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ActivateControlTab`

Selects a control tab on the model view to be the active tab.
Selects a control tab on the model view to be the active tab.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ActivateControlTab( _
   ByVal Name As System.String _
) As System.Boolean
```

```

Dim instance As IModelViewManager
Dim Name As System.String
Dim value As System.Boolean
 
value = instance.ActivateControlTab(Name)
```

```

System.bool ActivateControlTab( 
   System.string Name
)
```

```

System.bool ActivateControlTab( 
   System.String^ Name
) 
```

#### Parameters

*Name*
:   Name of control tab

#### Return Value

True if the selected control tab is active, false if not

Example

[Add ActiveX Tabs to Model View (C#)](Add_ActiveX_Tabs_to_Model_View_Example_CSharp.htm)  
[Add ActiveX Tabs to Model View (VB.NET)](Add_ActiveX_Tabs_to_Model_View_Example_VBNET.htm)  
[Add ActiveX Tabs to Model View (VBA)](Add_ActiveX_Tabs_to_Model_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md)  
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.md)  
[IModelViewManager::ActivateModelTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ActivateModelTab.md)  
[IModelViewManager::AddControl3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddControl3.md)  
[IModelViewManager::DeleteControlTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DeleteControlTab.md)  
[IModelViewManager::GetControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetControl.md)  
[IModelViewManager::IGetControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~IGetControl.md)  
[IModelViewManager::IsControlTabActive Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~IsControlTabActive.md)  
[IModelViewManager::IsModelTabActive Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~IsModelTabActive.md)
