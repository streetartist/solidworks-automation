# ISetPathSegments Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ISetPathSegments`

Sets the path segments to use to create this structural member.
Sets the path segments to use to create this structural member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetPathSegments( _
   ByVal Count As System.Integer, _
   ByRef SegArr As SketchSegment _
) 
```

```

Dim instance As IStructuralMemberFeatureData
Dim Count As System.Integer
Dim SegArr As SketchSegment
 
instance.ISetPathSegments(Count, SegArr)
```

```

void ISetPathSegments( 
   System.int Count,
   ref SketchSegment SegArr
)
```

```

void ISetPathSegments( 
   System.int Count,
   SketchSegment^% SegArr
) 
```

#### Parameters

*Count*
:   Number of path segments

*SegArr*
:   - in-process, unmanaged C++: Pointer to an array of [sketch segments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.md)  
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.md)  
[IStructuralMemberFeatureData::GetPathSegmentAt Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetPathSegmentAt.md)  
[IStructuralMemberFeatureData::GetPathSegmentsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetPathSegmentsCount.md)  
[IStructuralMemberFeatureData::IGetPathSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~IGetPathSegments.md)  
[IStructuralMemberFeatureData::PathSegments Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~PathSegments.md)
