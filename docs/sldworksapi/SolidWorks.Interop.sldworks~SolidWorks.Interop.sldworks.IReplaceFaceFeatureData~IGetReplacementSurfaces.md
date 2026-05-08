# IGetReplacementSurfaces Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~IGetReplacementSurfaces`

Gets the replacement surfaces for this feature.
Gets the replacement surfaces for this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetReplacementSurfaces( _
   ByVal Count As System.Integer _
) As Feature
```

```

Dim instance As IReplaceFaceFeatureData
Dim Count As System.Integer
Dim value As Feature
 
value = instance.IGetReplacementSurfaces(Count)
```

```

Feature IGetReplacementSurfaces( 
   System.int Count
)
```

```

Feature^ IGetReplacementSurfaces( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of replacement surfaces

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [replacement surfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) of size Count
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IReplaceFaceFeatureData::GetReplacementSurfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~GetReplacementSurfacesCount.md) before calling this method to get the size of Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IReplaceFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData.md)  
[IReplaceFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData_members.md)  
[IReplaceFaceFeatureData::ISetReplacementSurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~ISetReplacementSurfaces.md)  
[IReplaceFaceFeatureData::ReplacementSurfaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~ReplacementSurfaces.md)
