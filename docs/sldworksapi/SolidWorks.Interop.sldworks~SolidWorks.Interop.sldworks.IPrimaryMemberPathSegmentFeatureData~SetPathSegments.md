# SetPathSegments Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData~SetPathSegments`

Gets the path segments, curves, and edges to create the structure system member.
Gets the path segments, curves, and edges to create the structure system member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetPathSegments( _
   ByVal PathSegments As System.Object _
) As System.Boolean
```

```

Dim instance As IPrimaryMemberPathSegmentFeatureData
Dim PathSegments As System.Object
Dim value As System.Boolean
 
value = instance.SetPathSegments(PathSegments)
```

```

System.bool SetPathSegments( 
   System.object PathSegments
)
```

```

System.bool SetPathSegments( 
   System.Object^ PathSegments
) 
```

#### Parameters

*PathSegments*
:   Array of [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)s, [IReferenceCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve.md)s, and/or [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)s

#### Return Value

True if path segments successfully set, false if not

Remarks

For .NET applications, you must marshal the PathSegments array to IDispatch object arrays before calling this method. See [IDispatch Object Arrays as Input in .NET](ms-its:sldworksapiprogguide.chm::/Overview/IDispatch_Object_Arrays_as_Input_in_.NET.htm).

Example

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.md) examples.

See the [IPrimaryMemberPathSegmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrimaryMemberPathSegmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.md)  
[IPrimaryMemberPathSegmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData_members.md)
