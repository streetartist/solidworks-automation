# IGetFaceFacets2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFaceFacets2`

Gets the facets IDs that correspond to a face.
Gets the facets IDs that correspond to a face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFaceFacets2( _
   ByVal FaceObj As Face2 _
) As System.Integer
```

```

Dim instance As ITessellation
Dim FaceObj As Face2
Dim value As System.Integer
 
value = instance.IGetFaceFacets2(FaceObj)
```

```

System.int IGetFaceFacets2( 
   Face2 FaceObj
)
```

```

System.int IGetFaceFacets2( 
   Face2^ FaceObj
) 
```

#### Parameters

*FaceObj*
:   [Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) from which you want to return the corresponding facet IDs

#### Return Value

- in-process, unmanaged C++: Pointer to an array of longs or integers that describe the facet IDs that correspond to the face

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

[ITessellation::NeedFaceFacetMap](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~NeedFaceFacetMap.md) must be set to true to return results.

Before calling this method, call [ITessellation::IGetFaceFacetsCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFaceFacetsCount2.md) to fetch the raw facet data. ITessellation::IGetFaceFacets2 clears the cache of raw facet data.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)  
[ITessellation::GetFaceFacets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFaceFacets.md)
