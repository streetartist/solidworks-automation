# GetFacetFins Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFacetFins`

Gets all of the fin IDs of the fins that border this facet.
Gets all of the fin IDs of the fins that border this facet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFacetFins( _
   ByVal FacetId As System.Integer _
) As System.Object
```

```

Dim instance As ITessellation
Dim FacetId As System.Integer
Dim value As System.Object
 
value = instance.GetFacetFins(FacetId)
```

```

System.object GetFacetFins( 
   System.int FacetId
)
```

```

System.Object^ GetFacetFins( 
   System.int FacetId
) 
```

#### Parameters

*FacetId*
:   ID of the facet to use to return the fin IDs

#### Return Value

Array of long or integer values that describe the fin IDs

Example

[Tessellate a Body (C#)](Tessellate_a_Body_Example_CSharp.htm)  
[Tessellate a Body (VB.NET)](Tessellate_a_Body_Example_VBNET.htm)  
[Tessellate a Body (VBA)](Tessellate_a_Body_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)  
[ITessellation::IGetFacetFins Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFacetFins.md)  
[ITessellation::IGetFacetFinsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFacetFinsCount.md)
