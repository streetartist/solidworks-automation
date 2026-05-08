# SetUIState Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetUIState`

Sets the user-interface state of the current feature.
Sets the user-interface state of the current feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetUIState( _
   ByVal StateType As System.Integer, _
   ByVal Flag As System.Boolean _
) 
```

```

Dim instance As IFeature
Dim StateType As System.Integer
Dim Flag As System.Boolean
 
instance.SetUIState(StateType, Flag)
```

```

void SetUIState( 
   System.int StateType,
   System.bool Flag
)
```

```

void SetUIState( 
   System.int StateType,
   System.bool Flag
) 
```

#### Parameters

*StateType*
:   User interface state type as defined in [swUIStates\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUIStates_e.html)

*Flag*
:   True to set the user-interface state, false to not

Remarks

If you pass in StateType of swIsHiddenInFeatureMgr and flag of True, then this method hides the display of the feature in the FeatureManager design tree. To see your changes in the FeatureManager design tree , use [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md).

Features are initialized with all user-interface state type values set to false. However, in the case of attributes, you can use [IAttributeDef::CreateInstance5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~CreateInstance5.md) to set the desired display state of the attribute at the time of creation.

A change in a the state setting of a feature causes all its dependents to inherit the same behavior, without actually setting the state type values of those dependents. Therefore, to get the actual user-interface state value of a feature, you can query its owner.

The user-interface state is not a property.

Example

[Display of Item in FeatureManager Design Tree (C++)](Display_of_Item_in_Feature_Manager_Example_CPlusPlus_COM.htm)  
[Hide Feature in FeatureManager Design Tree (VBA)](Hide_Feature_in_FeatureManager_Design_Tree_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::Visible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Visible.md)  
[IFeature::GetUIState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetUIState.md)
