# ISetSegments Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~ISetSegments`

Sets the sketch segments to use in this structural-member group.
Sets the sketch segments to use in this structural-member group.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetSegments( _
   ByVal Count As System.Integer, _
   ByRef SegArr As SketchSegment _
) 
```

```

Dim instance As IStructuralMemberGroup
Dim Count As System.Integer
Dim SegArr As SketchSegment
 
instance.ISetSegments(Count, SegArr)
```

```

void ISetSegments( 
   System.int Count,
   ref SketchSegment SegArr
)
```

```

void ISetSegments( 
   System.int Count,
   SketchSegment^% SegArr
) 
```

#### Parameters

*Count*
:   Number of sketch segments

*SegArr*
:   - in-process, unmanaged C++: Pointer to an array of [sketch segments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before using this method, call [IStructuralMemberGroup::GetSegmentsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~GetSegmentsCount.md) to populate the *Count* parameter.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.md)  
[IStructuralMemberGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup_members.md)  
[IStructuralMemberGroup::IGetSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~IGetSegments.md)  
[IStructuralMemberGroup::Segments Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~Segments.md)
