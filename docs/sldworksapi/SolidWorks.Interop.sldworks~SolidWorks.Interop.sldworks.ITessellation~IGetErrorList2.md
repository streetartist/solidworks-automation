# IGetErrorList2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetErrorList2`

Gets the tessellation error list.
Gets the tessellation error list.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IGetErrorList2( _
   ByRef FaceErrArray As Face2, _
   ByRef FacetErrArray As System.Integer, _
   ByRef VertexPointErrArray As System.Integer, _
   ByRef VertexNormalErrArray As System.Integer, _
   ByRef VertexParamsErrArray As System.Integer _
) 
```

```

Dim instance As ITessellation
Dim FaceErrArray As Face2
Dim FacetErrArray As System.Integer
Dim VertexPointErrArray As System.Integer
Dim VertexNormalErrArray As System.Integer
Dim VertexParamsErrArray As System.Integer
 
instance.IGetErrorList2(FaceErrArray, FacetErrArray, VertexPointErrArray, VertexNormalErrArray, VertexParamsErrArray)
```

```

void IGetErrorList2( 
   out Face2 FaceErrArray,
   out System.int FacetErrArray,
   out System.int VertexPointErrArray,
   out System.int VertexNormalErrArray,
   out System.int VertexParamsErrArray
)
```

```

void IGetErrorList2( 
   [Out] Face2^ FaceErrArray,
   [Out] System.int FacetErrArray,
   [Out] System.int VertexPointErrArray,
   [Out] System.int VertexNormalErrArray,
   [Out] System.int VertexParamsErrArray
) 
```

#### Parameters

*FaceErrArray*
:   - in-process, unmanaged C++: Pointer to an array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) that have errors

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*FacetErrArray*
:   - in-process, unmanaged C++: Pointer to an array of longs or integers describing the facets with errors

    - VBA, VB.NET, C#, and C++/CLI: Not supported

*VertexPointErrArray*
:   - in-process, unmanaged C++: Pointer to an array of longs or integers of vertex point IDs from FacetErrArray

    - VBA, VB.NET, C#, and C++/CLI: Not supported

*VertexNormalErrArray*
:   - in-process, unmanaged C++: Pointer to an array of longs or integers of vertex normal IDs from FacetErrArray

    - VBA, VB.NET, C#, and C++/CLI: Not supported

*VertexParamsErrArray*
:   - in-process, unmanaged C++: Pointer to an array of longs or integers of vertex parameters IDs from facetErrArray

    - VBA, VB.NET, C#, and C++/CLI: Not supported

Remarks

Before using this method, make sure that you can retrieve the list for the tessellation data that you want to query error information from:

- [ITessellation::NeedVertexNormal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~NeedVertexNormal.md)
- [ITessellation::NeedVertexParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~NeedVertexParams.md)
- [ITessellation::NeedFaceFacetMap](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~NeedFaceFacetMap.md)
- [ITessellation::NeedEdgeFinMap](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~NeedEdgeFinMap.md)
- [ITessellation::NeedErrorList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~NeedErrorList.md)

After using an ITessellation function, you can return error information about any of the tessellation data.

The arrays returned by ITessellation::GetErrorList contains the tessellation entity IDs that have errors:

- Face error: The specified face could not be faceted.
- Facet error: The specified facet is disconnected from its neighboring facets.
- Vertex error: The specified vertex does not match any vertices on adjacent faces. There may be gaps between facets.
- Vertex normal error: The tessellate function could not calculate an accurate vertex normal.
- Vertex parameter error: The tessellate function could not calculate accurate vertex parameters.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)  
[ITessellation::GetErrorList Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetErrorList.md)  
[ITessellation::IGetErrorListCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetErrorListCount.md)  
[ITessellate::NeedErrorList Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~NeedErrorList.md)
