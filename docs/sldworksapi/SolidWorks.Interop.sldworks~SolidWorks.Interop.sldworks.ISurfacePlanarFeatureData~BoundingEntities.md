# BoundingEntities Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData~BoundingEntities`

Gets or sets the bounding entities for this planar surface feature.
Gets or sets the bounding entities for this planar surface feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BoundingEntities As System.Object
```

```

Dim instance As ISurfacePlanarFeatureData
Dim value As System.Object
 
instance.BoundingEntities = value
 
value = instance.BoundingEntities
```

```

System.object BoundingEntities {get; set;}
```

```

property System.Object^ BoundingEntities {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of bounding entities

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [ISurfacePlanarFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfacePlanarFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData.md)  
[ISurfacePlanarFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData_members.md)  
[ISurfacePlanarSurfaceData::GetBoundingEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData~GetBoundingEntitiesCount.md)  
[ISurfacePlanarSurfaceData::IGetBoundingEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData~IGetBoundingEntities.md)  
[ISurfacePlanarSurfaceData::ISetBoundingEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData~ISetBoundingEntities.md)
