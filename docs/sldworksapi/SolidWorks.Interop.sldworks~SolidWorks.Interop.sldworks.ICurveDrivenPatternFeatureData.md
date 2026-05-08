# ICurveDrivenPatternFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData`

Allows access to a curve-driven pattern feature.
Allows access to a curve-driven pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ICurveDrivenPatternFeatureData 
```

```

Dim instance As ICurveDrivenPatternFeatureData
```

```

public interface ICurveDrivenPatternFeatureData 
```

```

public interface class ICurveDrivenPatternFeatureData 
```

Remarks

Read [Pattern Features and their Feature Data Objects](sldworksapiprogguide.chm::/OVERVIEW/Pattern_Features_and_their_Feature_Data_Objects.htm).

Before calling [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.md), you must pre-select the entities needed to create the curve-driven pattern feature.

|  |  |
| --- | --- |
| **To** [**select**](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md)**...** | **Use Mark=...** |
| Features to pattern | 4 |
| Direction 1 entity (2D/3D curve, edge, sketch, or sketch entity) | 1 |
| Direction 2 entity (2D/3D curve, edge, sketch, or sketch entity) | 2 |
| Face normal (face on which the Direction 1 3D curve lies); needed only when [ICurveDrivenPatternFeatureData::D1AlignmentMethod](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D1AlignmentMethod.md) is set to [swCurveDrivenPatternAlignment\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCurveDrivenPatternAlignment_e.html).swCurvePatternTangentToCurve and Direction 1 is a 3D curve entity | 1024 |

After calling IFeatureManager::CreateDefinition, you can explicitly set other properties on the feature data object.  
   
You must call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md) after initializing this feature data object in order to successfully create the curve-driven pattern feature.  
   
For more information about curve-driven pattern features, see the **Parts and Features > Features > Patterns and Mirroring > Types of Patterns > Curve Driven Patterns and the Curve Driven Pattern PropertyManager** topic in the SOLIDWORKS user-interface help.

Example

[Create and Access Curve-driven Pattern Feature (C#)](Create_and_Access_Curve-driven_Pattern_Feature_Example_CSharp.htm)  
[Create and Access Curve-driven Pattern Feature (VB.NET)](Create_and_Access_Curve-driven_Pattern_Feature_Example_VBNET.htm)  
[Create and Access Curve-driven Pattern Feature (VBA)](Create_and_Access_Curve-driven_Pattern_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ILocalCurvePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData.md)
