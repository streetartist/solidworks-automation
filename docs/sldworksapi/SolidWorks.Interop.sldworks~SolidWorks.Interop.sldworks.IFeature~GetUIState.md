# GetUIState Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetUIState`

Gets the user-interface state of the current feature.
Gets the user-interface state of the current feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUIState( _
   ByVal StateType As System.Integer _
) As System.Boolean
```

```

Dim instance As IFeature
Dim StateType As System.Integer
Dim value As System.Boolean
 
value = instance.GetUIState(StateType)
```

```

System.bool GetUIState( 
   System.int StateType
)
```

```

System.bool GetUIState( 
   System.int StateType
) 
```

#### Parameters

*StateType*
:   User interface state type as defined in [swUIStates\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUIStates_e.html)

#### Return Value

True if the state type is set, false if it is not

Remarks

If you pass in the user-interface state type of swIsHiddenInFeatureMgr, this method returns True if the current feature is hidden in the FeatureManager design tree or false if the current feature is visible in the FeatureManager design tree.

The user-interface state is not a property.

To see your changes in the FeatureManager design tree, call [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md). Currently, the user-interface state data is runtime only.

Features are initialized with all user-interface state type values set to false.

A change in a feature state setting causes all the dependents of the feature to inherit the same behavior, without actually setting the state type values of those dependents. Therefore, to get the actual user-interface state value of a feature, you must check the owning feature.

Example

[Hide Feature in FeatureManager Design Tree (VBA)](Hide_Feature_in_FeatureManager_Design_Tree_Example_VB.htm)  
[Display of Item in FeatureManager Design Tree (C++)](Display_of_Item_in_Feature_Manager_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::SetUIState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetUIState.md)  
[IFeature::Visible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Visible.md)
