# FeatureLocalSketchDrivenPattern Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureLocalSketchDrivenPattern`

Obsolete. See IFeatureManager::CreateFeature and the Remarks in ILocalSketchPatternFeatureData.
Obsolete. See [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md) and the Remarks in [ILocalSketchPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureLocalSketchDrivenPattern( _
   ByVal ReferencePoint As System.Integer _
) As Feature
```

```

Dim instance As IFeatureManager
Dim ReferencePoint As System.Integer
Dim value As Feature
 
value = instance.FeatureLocalSketchDrivenPattern(ReferencePoint)
```

```

Feature FeatureLocalSketchDrivenPattern( 
   System.int ReferencePoint
)
```

```

Feature^ FeatureLocalSketchDrivenPattern( 
   System.int ReferencePoint
) 
```

#### Parameters

*ReferencePoint*
:   Type of selected reference point as defined in [swLocalSketchPatternReferencePoint\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLocalSketchPatternReferencePoint_e.html) (see **Remarks**)

#### Return Value

Local sketch pattern [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

|  |  |
| --- | --- |
| **To** [**select**](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md)**...** | **Use a mark of...** |
| Components to pattern | 1 |
| Sketch to define the pattern | 16 |
| Reference point for ReferencePoint  **NOTE:** If ReferencePoint is set to swLocalSketchPatternReferencePoint\_e.swLocalSketchPatternSelectedPoint, then the selected reference point must be a vertex. | 32 |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
