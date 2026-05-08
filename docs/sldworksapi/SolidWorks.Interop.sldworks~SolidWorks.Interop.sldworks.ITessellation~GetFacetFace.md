# GetFacetFace Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFacetFace`

Gets a face that corresponds to a facet.
Gets a face that corresponds to a facet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFacetFace( _
   ByVal FacetId As System.Integer _
) As System.Object
```

```

Dim instance As ITessellation
Dim FacetId As System.Integer
Dim value As System.Object
 
value = instance.GetFacetFace(FacetId)
```

```

System.object GetFacetFace( 
   System.int FacetId
)
```

```

System.Object^ GetFacetFace( 
   System.int FacetId
) 
```

#### Parameters

*FacetId*
:   Facet ID of the facet from which to return the face

#### Return Value

[Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) to which that this facet belongs

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)  
[ITessellation::IGetFacetFace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFacetFace2.md)
