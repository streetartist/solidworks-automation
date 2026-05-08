# IGetFaceFacetsCount2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFaceFacetsCount2`

Gets the number of facets corresponding to a face.
Gets the number of facets corresponding to a face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFaceFacetsCount2( _
   ByVal FaceObj As Face2 _
) As System.Integer
```

```

Dim instance As ITessellation
Dim FaceObj As Face2
Dim value As System.Integer
 
value = instance.IGetFaceFacetsCount2(FaceObj)
```

```

System.int IGetFaceFacetsCount2( 
   Face2 FaceObj
)
```

```

System.int IGetFaceFacetsCount2( 
   Face2^ FaceObj
) 
```

#### Parameters

*FaceObj*
:   Face on which to count the facets

#### Return Value

Number of facets

Remarks

This method caches the raw facet data after determining the number of facets. A subsequent call to [ITessellation::IGetFaceFacets2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFaceFacets2.md) does not have to fetch the facet data again.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)  
[ITessellation::GetFaceFacets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFaceFacets.md)
