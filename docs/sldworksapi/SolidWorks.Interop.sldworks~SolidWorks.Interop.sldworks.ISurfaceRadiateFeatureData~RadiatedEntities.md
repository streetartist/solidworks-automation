# RadiatedEntities Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~RadiatedEntities`

Gets or sets the radiated entities for this surface radiate feature.
Gets or sets the radiated entities for this surface radiate feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RadiatedEntities As System.Object
```

```

Dim instance As ISurfaceRadiateFeatureData
Dim value As System.Object
 
instance.RadiatedEntities = value
 
value = instance.RadiatedEntities
```

```

System.object RadiatedEntities {get; set;}
```

```

property System.Object^ RadiatedEntities {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of radiated entities

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [ISurfaceRadiateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceRadiateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData.md)  
[ISurfaceRadiateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData_members.md)  
[ISurfaceRadiateSurfaceData::GetRadiatedEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~GetRadiatedEntitiesCount.md)  
[ISurfaceRadiateSurfaceData::IGetRadiatedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~IGetRadiatedEntities.md)  
[ISurfaceRadiateSurfaceData::ISetRadiatedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~ISetRadiatedEntities.md)
