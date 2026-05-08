# IGetBoundingEntities Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData~IGetBoundingEntities`

Gets the bounding entities for this planar surface feature.
Gets the bounding entities for this planar surface feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetBoundingEntities( _
   ByVal Count As System.Integer _
) As System.Object
```

```

Dim instance As ISurfacePlanarFeatureData
Dim Count As System.Integer
Dim value As System.Object
 
value = instance.IGetBoundingEntities(Count)
```

```

System.object IGetBoundingEntities( 
   System.int Count
)
```

```

System.Object^ IGetBoundingEntities( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of bounding entities

#### Return Value

- in-process, unmanaged C++: Pointer to an array of bounding entities of size Count

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [ISurfacePlanarFeatureData::GetBoundingEntitiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData~GetBoundingEntitiesCount.md) before calling this method to get the value for Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfacePlanarFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData.md)  
[ISurfacePlanarFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData_members.md)  
[ISurfacePlanarFeatureData::ISetBoundingEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData~ISetBoundingEntities.md)  
[ISurfacePlanarFeatureData::BoundingEntities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData~BoundingEntities.md)
