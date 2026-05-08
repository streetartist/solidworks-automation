# GetBoundingEntitiesCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData~GetBoundingEntitiesCount`

Gets the number of bounding entities for this planar surface feature.
Gets the number of bounding entities for this planar surface feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBoundingEntitiesCount() As System.Integer
```

```

Dim instance As ISurfacePlanarFeatureData
Dim value As System.Integer
 
value = instance.GetBoundingEntitiesCount()
```

```

System.int GetBoundingEntitiesCount()
```

```

System.int GetBoundingEntitiesCount(); 
```

#### Return Value

Number of bounding entities

Remarks

Call this method before calling [ISurfacePlanarFeatureData::IGetBoundingEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData~IGetBoundingEntities.md) to get the size of the array for that method.

Example

See the [ISurfacePlanarFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfacePlanarFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData.md)  
[ISurfacePlanarFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData_members.md)  
[ISurfacePlanarFeatureData::ISetBoundingEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData~ISetBoundingEntities.md)  
[ISurfacePlanarFeatureData::BoundingEntities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData~BoundingEntities.md)
