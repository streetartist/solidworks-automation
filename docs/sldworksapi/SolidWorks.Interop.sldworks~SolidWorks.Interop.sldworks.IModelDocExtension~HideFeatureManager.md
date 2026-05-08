# HideFeatureManager Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HideFeatureManager`

Hides or shows the Manager Pane.
Hides or shows the Manager Pane.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function HideFeatureManager( _
   ByVal Hide As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim Hide As System.Boolean
Dim value As System.Boolean
 
value = instance.HideFeatureManager(Hide)
```

```

System.bool HideFeatureManager( 
   System.bool Hide
)
```

```

System.bool HideFeatureManager( 
   System.bool Hide
) 
```

#### Parameters

*Hide*
:   True to hide the Manager Pane, false to not

#### Return Value

True if successful, false if not

Remarks

The FeatureManager design tree, PropertyManager, ConfigurationManager, DimXpertManager, DisplayManager, and custum tabs reside in the Manager Pane.

Example

[Hide the FeatureManager Design Tree (VBA)](Hide_the_FeatureManager_Example_VB.htm)  
[Hide the FeatureManager Design Tree (VB.NET)](Hide_the_FeatureManager_Example_VBNET.htm)  
[Hide the FeatureManager Design Tree (C#)](Hide_the_FeatureManager_Example_CSharp.htm)  
[Change Active Tab in Manager Pane (C#)](Change_Active_Tab_in_Manager_Pane_Example_CSharp.htm)  
[Change Active Tab in Manager Pane (VB.NET)](Change_Active_Tab_in_Manager_Pane_Example_VBNET.htm)  
[Change Active Tab in Manager Pane (VBA)](Change_Active_Tab_in_Manager_Pane_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::FeatureManagerFilterString Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FeatureManagerFilterString.md)  
[IModelViewManager::FeatureManagerTabsVisible Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~FeatureManagerTabsVisible.md)
