# GetFaceFacets Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFaceFacets`

Gets the facets IDs that correspond to a SOLIDWORKS face.
Gets the facets IDs that correspond to a SOLIDWORKS face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFaceFacets( _
   ByVal Facedisp As System.Object _
) As System.Object
```

```

Dim instance As ITessellation
Dim Facedisp As System.Object
Dim value As System.Object
 
value = instance.GetFaceFacets(Facedisp)
```

```

System.object GetFaceFacets( 
   System.object Facedisp
)
```

```

System.Object^ GetFaceFacets( 
   System.Object^ Facedisp
) 
```

#### Parameters

*Facedisp*
:   [Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) from which to return the corresponding facet IDs

#### Return Value

Array of longs or integers (see [Long vs. Integer](sldworksapiprogguide.chm::/overview/Long_vs_Integer.htm)) that describe the facet IDs that correspond to the face

Remarks

[ITessellation::NeedFaceFacetMap](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~NeedFaceFacetMap.md) must be set to true to return results.

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
[ITessellation::IGetFaceFacets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFaceFacets2.md)  
[ITessellation::IGetFaceFacetsCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFaceFacetsCount2.md)
