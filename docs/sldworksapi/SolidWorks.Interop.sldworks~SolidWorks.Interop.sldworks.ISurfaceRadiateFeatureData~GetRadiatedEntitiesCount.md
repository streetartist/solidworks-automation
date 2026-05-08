# GetRadiatedEntitiesCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~GetRadiatedEntitiesCount`

Gets the number of radiated entities for this surface radiate feature.
Gets the number of radiated entities for this surface radiate feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRadiatedEntitiesCount() As System.Integer
```

```

Dim instance As ISurfaceRadiateFeatureData
Dim value As System.Integer
 
value = instance.GetRadiatedEntitiesCount()
```

```

System.int GetRadiatedEntitiesCount()
```

```

System.int GetRadiatedEntitiesCount(); 
```

#### Return Value

Number of radiated entities

Remarks

Call this method before calling [ISurfaceRadiateFeatureData::IGetRadiatedEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~IGetRadiatedEntities.md) to get the size of the array for that method.

Example

See the [ISurfaceRadiateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceRadiateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData.md)  
[ISurfaceRadiateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData_members.md)  
[ISurfaceRadiateFeatureData::ISetRadiatedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~ISetRadiatedEntities.md)  
[ISurfaceRadiateFeatureData::RadiatedEntities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~RadiatedEntities.md)
