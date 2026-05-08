# IGetFacetFace2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFacetFace2`

Gets a face that corresponds to a facet.
Gets a face that corresponds to a facet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFacetFace2( _
   ByVal FacetId As System.Integer _
) As Face2
```

```

Dim instance As ITessellation
Dim FacetId As System.Integer
Dim value As Face2
 
value = instance.IGetFacetFace2(FacetId)
```

```

Face2 IGetFacetFace2( 
   System.int FacetId
)
```

```

Face2^ IGetFacetFace2( 
   System.int FacetId
) 
```

#### Parameters

*FacetId*
:   Facet ID of the facet from which you want to return the face pointer

#### Return Value

[Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) to which this facet belongs

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)  
[ITessellation::GetFacetFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFacetFace.md)
