# IProjectionCurveFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData`

Allows access to a projection curve feature.
Allows access to a projection curve feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IProjectionCurveFeatureData 
```

```

Dim instance As IProjectionCurveFeatureData
```

```

public interface IProjectionCurveFeatureData 
```

```

public interface class IProjectionCurveFeatureData 
```

Remarks

To create a projection curve feature:

1. Use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to pre-select the necessary entities using the following Marks:  
     
   > - target faces on which to project a sketch = 1
   > - sketch to project = 2
   > - target sketch on which to project a sketch = 4
   > - projection direction entity = 8
2. Call IFeatureManager::CreateDefinition(swFmRefCurve) to access this interface.
3. Set non-entity properties on this interface.
4. Call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md) to create the projection curve feature.

See the SOLIDWORKS Help for more information about projection curve features.

Example

[Get Projected Curve (VBA)](Get_Projected_Curve_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IProjectionCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
