# ISetReplacementSurfaces Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~ISetReplacementSurfaces`

Sets the replacement surfaces for this feature.
Sets the replacement surfaces for this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetReplacementSurfaces( _
   ByVal Count As System.Integer, _
   ByRef SurfDisp As Feature _
) 
```

```

Dim instance As IReplaceFaceFeatureData
Dim Count As System.Integer
Dim SurfDisp As Feature
 
instance.ISetReplacementSurfaces(Count, SurfDisp)
```

```

void ISetReplacementSurfaces( 
   System.int Count,
   ref Feature SurfDisp
)
```

```

void ISetReplacementSurfaces( 
   System.int Count,
   Feature^% SurfDisp
) 
```

#### Parameters

*Count*
:   Number of replacement surfaces

*SurfDisp*
:   - in-process, unmanaged C++: Pointer to an array of [replacement surfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) of size Count
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IReplaceFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData.md)  
[IReplaceFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData_members.md)  
[IReplaceFaceFeatureData::GetReplacementSurfacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~GetReplacementSurfacesCount.md)  
[IReplaceFaceFeatureData::IGetReplacementSurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~IGetReplacementSurfaces.md)  
[IReplaceFaceFeatureData::ReplacementSurfaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~ReplacementSurfaces.md)
