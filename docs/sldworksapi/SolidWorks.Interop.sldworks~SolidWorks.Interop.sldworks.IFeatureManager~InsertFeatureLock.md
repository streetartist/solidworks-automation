# InsertFeatureLock Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFeatureLock`

Locks or freezes a selected feature.
Locks or freezes a selected feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertFeatureLock() As Feature
```

```

Dim instance As IFeatureManager
Dim value As Feature
 
value = instance.InsertFeatureLock()
```

```

Feature InsertFeatureLock()
```

```

Feature^ InsertFeatureLock(); 
```

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

After calling this method, a temporary freeze bar displays after the feature in the FeatureManager design tree. If you move the freeze bar to the top, the feature unlocks and the freeze bar disappears. To permanently enable the freeze bar, select **Tools > Options > System Options > General > Enable Freeze bar**.

This method is analogous to freezing a feature. For more information, see **SOLIDWORKS user-interface help > Parts and Features > Features > Feature Freeze > Freezing Features**.

Example

'VBA

' Preconditions:

' 1. Open a part.

' 2. Select a feature.

' Postconditions: Observe that the selected feature is locked, and a gold freeze bar appears after the feature in the FeatureManager design tree.

Option Explicit  
Dim swApp As SldWorks.SldWorks  
Dim swModel As SldWorks.ModelDoc2  
Dim swSelMgr As SldWorks.SelectionMgr  
Dim swFeat, swLockFeat As SldWorks.Feature  
Dim swFeatMgr As SldWorks.FeatureManager

Sub main()

    Set swApp = Application.SldWorks  
    Set swModel = swApp.ActiveDoc  
    Set swSelMgr = swModel.SelectionManager  
    Set swFeatMgr = swModel.FeatureManager  
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)  
    Set swLockFeat = swFeatMgr.**InsertFeatureLock**

End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeature::IsFrozen Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsFrozen.md)
