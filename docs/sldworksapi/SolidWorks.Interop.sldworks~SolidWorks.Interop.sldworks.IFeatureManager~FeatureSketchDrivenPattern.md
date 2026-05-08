# FeatureSketchDrivenPattern Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureSketchDrivenPattern`

Obsolete. See IFeatureManager::CreateFeature and the Remarks in ISketchPatternFeatureData.
Obsolete. See [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md) and the Remarks in [ISketchPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureSketchDrivenPattern( _
   ByVal UseCentroid As System.Boolean, _
   ByVal BGeomPatt As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim UseCentroid As System.Boolean
Dim BGeomPatt As System.Boolean
Dim value As Feature
 
value = instance.FeatureSketchDrivenPattern(UseCentroid, BGeomPatt)
```

```

Feature FeatureSketchDrivenPattern( 
   System.bool UseCentroid,
   System.bool BGeomPatt
)
```

```

Feature^ FeatureSketchDrivenPattern( 
   System.bool UseCentroid,
   System.bool BGeomPatt
) 
```

#### Parameters

*UseCentroid*
:   True to use a centroid as the reference point, false to not

*BGeomPatt*
:   True to pattern using only the feature geometry, false to pattern each instance

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

Before calling this method, select the required entities using the proper selection marks:

- features = 4
- points = 32
- sketches = 64
- faces = 128
- bodies = 256

See [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) for details about selecting input entities. See the SOLIDWORKS Help for more information about sketch-driven patterns.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
