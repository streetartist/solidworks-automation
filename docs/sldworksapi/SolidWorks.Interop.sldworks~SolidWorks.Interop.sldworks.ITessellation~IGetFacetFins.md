# IGetFacetFins Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFacetFins`

Gets all of the fin IDs of the fins that border this facet.
Gets all of the fin IDs of the fins that border this facet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFacetFins( _
   ByVal FacetId As System.Integer _
) As System.Integer
```

```

Dim instance As ITessellation
Dim FacetId As System.Integer
Dim value As System.Integer
 
value = instance.IGetFacetFins(FacetId)
```

```

System.int IGetFacetFins( 
   System.int FacetId
)
```

```

System.int IGetFacetFins( 
   System.int FacetId
) 
```

#### Parameters

*FacetId*
:   ID of the facet to use to return the fin IDs

#### Return Value

- in-process, unmanaged C++: Pointer to an array of long or integer values that describe the fin IDs

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

A cache is created when you use [ITessellation::IGetFacetFinsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFacetFinsCount.md). This cache is released when you use ITessellation::IGetFacetFins. If you use ITessellation::IGetFacetFinsCount again, then the cache is refilled. Alternatively, you can use ITessellation::IGetFacetFins repeatedly.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)  
[ITessellate::GetFacetFins Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFacetFins.md)
