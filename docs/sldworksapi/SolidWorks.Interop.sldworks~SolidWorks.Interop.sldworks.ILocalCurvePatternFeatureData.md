# ILocalCurvePatternFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData`

Allows access to a curve-driven component pattern feature in an assembly.
Allows access to a curve-driven component pattern feature in an assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ILocalCurvePatternFeatureData 
```

```

Dim instance As ILocalCurvePatternFeatureData
```

```

public interface ILocalCurvePatternFeatureData 
```

```

public interface class ILocalCurvePatternFeatureData 
```

Remarks

Read [Pattern Features and their Feature Data Objects](sldworksapiprogguide.chm::/OVERVIEW/Pattern_Features_and_their_Feature_Data_Objects.htm).

Before calling [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.md), you must pre-select the entities needed to create the curve-driven component pattern feature.

|  |  |
| --- | --- |
| **To** [**select**](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md)**...** | **Use Mark=...** |
| Components to pattern | 1 |
| Curve, edge, sketch, or sketch entity for Direction 1 | 2 |
| Curve, edge, sketch, or sketch entity for Direction 2 | 4 |
| Reference point (only needed if [ILocalCurvePatternFeatureData::D1ReferencePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1ReferencePoint.md) is set to [swLocalCurvePatternReferencePoint\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLocalCurvePatternReferencePoint_e.html).swLocalCurvePatternSelectedPoint) | 32 |
| Face normal (face on which a 3D curve lies) | 64 |

After calling IFeatureManager::CreateDefinition, you can explicitly set other properties on the feature data object.

You must call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md) after initializing this feature data object in order to successfully create the curve-driven component pattern feature.

For more information, see the **Assemblies > Basic Component Operations > Component Patterns > Curve Driven Component Pattern** topic in the SOLIDWORKS user-interface help.

Example

[Create Local Curve-driven Pattern (C#)](Create_Local_Curve-driven_Pattern_Example_CSharp.htm)  
[Create Local Curve-driven Pattern (VB.NET)](Create_Local_Curve-driven_Pattern_Example_VBNET.htm)  
[Create Local Curve-driven Pattern (VBA)](Create_Local_Curve-driven_Pattern_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalCurvePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.md)
