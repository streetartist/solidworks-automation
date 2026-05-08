# IGetFacetFinsCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFacetFinsCount`

Gets the number of fins corresponding to a facet.
Gets the number of fins corresponding to a facet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFacetFinsCount( _
   ByVal FacetId As System.Integer _
) As System.Integer
```

```

Dim instance As ITessellation
Dim FacetId As System.Integer
Dim value As System.Integer
 
value = instance.IGetFacetFinsCount(FacetId)
```

```

System.int IGetFacetFinsCount( 
   System.int FacetId
)
```

```

System.int IGetFacetFinsCount( 
   System.int FacetId
) 
```

#### Parameters

*FacetId*
:   Facet for which to count fins

#### Return Value

Number of fins corresponding to FacetId

Remarks

A cache is created when you use this method. This cache is released when you use [ITessellation::IGetFacetFins](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFacetFins.md). If you use ITessellation::IGetFacetFinsCount again, then the cache is refilled. Alternatively, you can use ITessellation::IGetFacetFins repeatedly.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)  
[ITessellation::GetFacetFins Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFacetFins.md)
