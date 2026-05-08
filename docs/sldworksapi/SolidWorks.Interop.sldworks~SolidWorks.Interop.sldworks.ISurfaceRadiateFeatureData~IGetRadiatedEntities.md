# IGetRadiatedEntities Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~IGetRadiatedEntities`

Gets the radiated entities for this surface radiate feature.
Gets the radiated entities for this surface radiate feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetRadiatedEntities( _
   ByVal Count As System.Integer _
) As System.Object
```

```

Dim instance As ISurfaceRadiateFeatureData
Dim Count As System.Integer
Dim value As System.Object
 
value = instance.IGetRadiatedEntities(Count)
```

```

System.object IGetRadiatedEntities( 
   System.int Count
)
```

```

System.Object^ IGetRadiatedEntities( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of radiated entities

#### Return Value

- in-process, unmanaged C++: Pointer to an array of radiated entities of size Count

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [ISurfaceRadiateFeatureData::GetRadiatedEntitiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~GetRadiatedEntitiesCount.md) before calling this method to get the value of Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceRadiateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData.md)  
[ISurfaceRadiateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData_members.md)
