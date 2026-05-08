# IGetSegments Method (IReferenceCurve)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~IGetSegments`

Gets the segments in this reference curve.
Gets the segments in this reference curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSegments( _
   ByVal NumSegments As System.Integer _
) As Edge
```

```

Dim instance As IReferenceCurve
Dim NumSegments As System.Integer
Dim value As Edge
 
value = instance.IGetSegments(NumSegments)
```

```

Edge IGetSegments( 
   System.int NumSegments
)
```

```

Edge^ IGetSegments( 
   System.int NumSegments
) 
```

#### Parameters

*NumSegments*
:   Number of segments in the reference curve

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [segments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) in the reference curve

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IReferenceCurve::GetSegmentCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~GetSegmentCount.md) to get NumSegments.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IReferenceCurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve.md)  
[IReferenceCurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve_members.md)  
[IReferenceCurve::GetSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~GetSegments.md)  
[IReferenceCurve::IGetFirstSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~IGetFirstSegment.md)  
[IReferenceCurve::IGetNextSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~IGetNextSegment.md)  
[IReferenceCurve::GetFirstSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~GetFirstSegment.md)  
[IReferenceCurve::GetNextSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~GetNextSegment.md)
