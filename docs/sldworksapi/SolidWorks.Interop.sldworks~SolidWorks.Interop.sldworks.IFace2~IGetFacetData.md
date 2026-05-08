# IGetFacetData Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetFacetData`

Obsolete. Superseded by IFace2::GetTessNorms, IFace2::IGetTessNorms, IFace2::GetTessTextures, IFace2::IGetTessTextures, IFace2::GetTessTriangleCount, IFace2::GetTessTriangles, IFace2::IGetTessTriangles, IFace2::GetTessTriStripEdges, IFace2::IGetTessT
Obsolete. Superseded by [IFace2::GetTessNorms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessNorms.md), [IFace2::IGetTessNorms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessNorms.md), [IFace2::GetTessTextures](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTextures.md)[, IFace2::IGetTessTextures, IFace2::GetTessTriangleCount, IFace2::GetTessTriangles,](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriangles.md) [IFace2::IGetTessTriangles](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriangles.md), [IFace2::GetTessTriStripEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripEdges.md), [IFace2::IGetTessTriStripEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStripEdges.md), [IFace::GetTessTriStripNorms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripNorms.md), [IFace2::IGetTessTriStripNorms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStripNorms.md), [IFace2::GetTessTriStrips](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStrips.md), and [IFace2::IGetTessTriStrips](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStrips.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IGetFacetData( _
   ByVal FacetMesh As System.Integer, _
   ByRef NFacets As System.Integer, _
   ByRef NStrips As System.Integer, _
   ByRef StripVertexNums As System.Integer, _
   ByRef VertexCoords As System.Single, _
   ByRef NormalCoords As System.Single _
) 
```

```

Dim instance As IFace2
Dim FacetMesh As System.Integer
Dim NFacets As System.Integer
Dim NStrips As System.Integer
Dim StripVertexNums As System.Integer
Dim VertexCoords As System.Single
Dim NormalCoords As System.Single
 
instance.IGetFacetData(FacetMesh, NFacets, NStrips, StripVertexNums, VertexCoords, NormalCoords)
```

```

void IGetFacetData( 
   System.int FacetMesh,
   ref System.int NFacets,
   ref System.int NStrips,
   ref System.int StripVertexNums,
   ref System.float VertexCoords,
   ref System.float NormalCoords
)
```

```

void IGetFacetData( 
   System.int FacetMesh,
   System.int% NFacets,
   System.int% NStrips,
   System.int% StripVertexNums,
   System.float% VertexCoords,
   System.float% NormalCoords
) 
```

#### Parameters

*FacetMesh*

*NFacets*

*NStrips*

*StripVertexNums*

*VertexCoords*

*NormalCoords*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)
