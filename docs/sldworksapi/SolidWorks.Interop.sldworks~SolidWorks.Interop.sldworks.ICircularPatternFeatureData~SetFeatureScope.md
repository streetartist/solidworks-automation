# SetFeatureScope Method (ICircularPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~SetFeatureScope`

Sets the feature scope, whether to autoselect the affected bodies, and the affected bodies in this circular pattern feature.
Sets the feature scope, whether to autoselect the affected bodies, and the affected bodies in this circular pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetFeatureScope( _
   ByVal FeatureScopeOption As System.Boolean, _
   ByVal AutoSelectBodies As System.Boolean, _
   ByVal Bodies As System.Object _
) As System.Boolean
```

```

Dim instance As ICircularPatternFeatureData
Dim FeatureScopeOption As System.Boolean
Dim AutoSelectBodies As System.Boolean
Dim Bodies As System.Object
Dim value As System.Boolean
 
value = instance.SetFeatureScope(FeatureScopeOption, AutoSelectBodies, Bodies)
```

```

System.bool SetFeatureScope( 
   System.bool FeatureScopeOption,
   System.bool AutoSelectBodies,
   System.object Bodies
)
```

```

System.bool SetFeatureScope( 
   System.bool FeatureScopeOption,
   System.bool AutoSelectBodies,
   System.Object^ Bodies
) 
```

#### Parameters

*FeatureScopeOption*
:   True (default) to specify affected bodies, false to apply the pattern to all bodies every time the feature regenerates (see **Remarks**)

*AutoSelectBodies*
:   True (default) to automatically select all bodies intersected by this pattern feature, false to specify affected bodies (see **Remarks**)

*Bodies*
:   Array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) to be affected; valid only if FeatureScopeOption is true and AutoSelectBodies is false

#### Return Value

True if feature scope set successfully, false if not (see **Remarks**)

Remarks

If this method returns false, then default values for FeatureScopeOption and AutoSelectBodies are set. A subsequent call to [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md) creates the feature with a FeatureScopeOption of true and an AutoSelectBodies of true.

After calling IFeature::ModifyDefinition, call [IFeature::GetErrorCode2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetErrorCode2.md) to determine what's wrong and then take necessary remedial action.

For more information, see the **Circular Pattern PropertyManager** topic in the SOLIDWORKS user-interface help.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.md)  
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.md)  
[ICircularPatternFeatureData::AutoSelect Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~AutoSelect.md)  
[ICircularPatternFeatureData::FeatureScope Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~FeatureScope.md)  
[ICircularPatternFeatureData::FeatureScopeBodies Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~FeatureScopeBodies.md)
