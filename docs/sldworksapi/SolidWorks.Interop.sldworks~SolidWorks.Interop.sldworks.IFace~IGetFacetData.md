# IGetFacetData Method (IFace)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~IGetFacetData`

Obsolete. Superseded by IFace2::IGetTessNorms, IFace2::IGetTessTextures, IFace2::GetTessTriangleCount, IFace2::IGetTriangles, IFace2::IGetTessTriStripEdges, IFace2::IGetTessTriStrips, and IFace2::GetTessTriStripSize.
Obsolete. Superseded by [IFace2::IGetTessNorms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessNorms.md), [IFace2::IGetTessTextures](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTextures.md), [IFace2::GetTessTriangleCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriangleCount.md), [IFace2::IGetTriangles](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriangles.md), [IFace2::IGetTessTriStripEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStripEdges.md), [IFace2::IGetTessTriStrips](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStrips.md), and [IFace2::GetTessTriStripSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripSize.md).

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
   ByVal StripVertexNums As System.IntPtr, _
   ByVal VertexCoords As System.IntPtr, _
   ByVal NormalCoords As System.IntPtr _
) 
```

```

Dim instance As IFace
Dim FacetMesh As System.Integer
Dim NFacets As System.Integer
Dim NStrips As System.Integer
Dim StripVertexNums As System.IntPtr
Dim VertexCoords As System.IntPtr
Dim NormalCoords As System.IntPtr
 
instance.IGetFacetData(FacetMesh, NFacets, NStrips, StripVertexNums, VertexCoords, NormalCoords)
```

```

void IGetFacetData( 
   System.int FacetMesh,
   ref System.int NFacets,
   ref System.int NStrips,
   System.IntPtr StripVertexNums,
   System.IntPtr VertexCoords,
   System.IntPtr NormalCoords
)
```

```

void IGetFacetData( 
   System.int FacetMesh,
   System.int% NFacets,
   System.int% NStrips,
   System.IntPtr StripVertexNums,
   System.IntPtr VertexCoords,
   System.IntPtr NormalCoords
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

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.md)  
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.md)
