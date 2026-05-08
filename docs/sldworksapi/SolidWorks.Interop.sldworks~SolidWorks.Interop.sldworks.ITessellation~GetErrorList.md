# GetErrorList Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetErrorList`

Gets the tessellation error list.
Gets the tessellation error list.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetErrorList( _
   ByRef FaceErrArray As System.Object, _
   ByRef FacetErrArray As System.Object, _
   ByRef VertexPointErrArray As System.Object, _
   ByRef VertexNormalErrArray As System.Object, _
   ByRef VertexParamsErrArray As System.Object _
) 
```

```

Dim instance As ITessellation
Dim FaceErrArray As System.Object
Dim FacetErrArray As System.Object
Dim VertexPointErrArray As System.Object
Dim VertexNormalErrArray As System.Object
Dim VertexParamsErrArray As System.Object
 
instance.GetErrorList(FaceErrArray, FacetErrArray, VertexPointErrArray, VertexNormalErrArray, VertexParamsErrArray)
```

```

void GetErrorList( 
   out System.object FaceErrArray,
   out System.object FacetErrArray,
   out System.object VertexPointErrArray,
   out System.object VertexNormalErrArray,
   out System.object VertexParamsErrArray
)
```

```

void GetErrorList( 
   [Out] System.Object^ FaceErrArray,
   [Out] System.Object^ FacetErrArray,
   [Out] System.Object^ VertexPointErrArray,
   [Out] System.Object^ VertexNormalErrArray,
   [Out] System.Object^ VertexParamsErrArray
) 
```

#### Parameters

*FaceErrArray*
:   Array of tessellation faces that have errors

*FacetErrArray*
:   Array of tessellation facets that have errors

*VertexPointErrArray*
:   Array of tessellation vertex points that have errors

*VertexNormalErrArray*
:   Array of tessellation vertex normals that have errors

*VertexParamsErrArray*
:   Array of tessellation vertex parameters that have errors

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
[ITessellation::IGetErrorList2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetErrorList2.md)  
[ITessellation::IGetErrorListCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetErrorListCount.md)  
[ITessellate::NeedErrorList Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~NeedErrorList.md)
