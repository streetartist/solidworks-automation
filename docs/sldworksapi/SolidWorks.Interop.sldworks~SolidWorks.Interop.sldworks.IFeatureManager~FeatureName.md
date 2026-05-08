# FeatureName Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureName`

Gets the feature name for the specified feature ID.
Gets the feature name for the specified feature ID.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property FeatureName( _
   ByVal NameID As System.Integer _
) As System.String
```

```

Dim instance As IFeatureManager
Dim NameID As System.Integer
Dim value As System.String
 
value = instance.FeatureName(NameID)
```

```

System.string FeatureName( 
   System.int NameID
) {get;}
```

```

property System.String^ FeatureName {
   System.String^ get(System.int NameID);
}
```

#### Parameters

*NameID*
:   Feature ID as defined in [swFeatureNameID\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureNameID_e.html)

#### Property Value

Feature name

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeature::GetTypeName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName.md)  
[IFeatureManager::ShowFeatureName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowFeatureName.md)  
[IFeature::Name Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Name.md)
