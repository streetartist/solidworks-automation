# IGetPatchBoundary Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~IGetPatchBoundary`

Gets the entities used to define the patch boundary for this fill-surface feature.
Gets the entities used to define the patch boundary for this fill-surface feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetPatchBoundary( _
   ByVal Count As System.Integer, _
   ByRef EntType As System.Integer _
) As System.Object
```

```

Dim instance As IFillSurfaceFeatureData
Dim Count As System.Integer
Dim EntType As System.Integer
Dim value As System.Object
 
value = instance.IGetPatchBoundary(Count, EntType)
```

```

System.object IGetPatchBoundary( 
   System.int Count,
   out System.int EntType
)
```

```

System.Object^ IGetPatchBoundary( 
   System.int Count,
   [Out] System.int EntType
) 
```

#### Parameters

*Count*
:   Number of entities used to define the patch boundary

*EntType*
:   - in-process, unmanaged C++: Pointer to an array of types of entities used to define the patch boundary as defined by [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html):
      - edges (swSelEDGES)
      - sketches (swSelSKETCHES)
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

- in-process, unmanaged C++: Pointer to an array of entities used to define the patch boundary of size Count

- VBA, VB.NET, C#, and C++/CLI: Not supported

Remarks

Call [IFillSurfaceFeatureData::GetPatchBoundaryCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetPatchBoundaryCount.md) before calling this method.

[IFillSurfaceFeatureData::GetCurvatureControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetCurvatureControl.md) uses the return value as input, so call IFillSurfaceFeatureData::IGetPatchBoundary before calling IFillSurfaceFeatureData::GetCurvatureControl.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.md)  
[IFillSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.md)  
[IFillSurfaceFeatureData::GetAlternateFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetAlternateFace.md)  
[IFillSurfaceFeatureData::GetPatchBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetPatchBoundary.md)  
[IFillSurfaceFeatureData::ISetPatchBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ISetPatchBoundary.md)  
[IFillSurfaceFeatureData::SetPatchBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~SetPatchBoundary.md)  
[IFillSurfaceFeatureData::ToggleAlternateFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ToggleAlternateFace.md)  
[IFillSurfaceFeatureData::TryToFormSolid Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~TryToFormSolid.md)
