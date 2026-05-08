# IImprintCurve Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IImprintCurve`

Imprints a curve on the selected face.
Imprints a curve on the selected face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IImprintCurve( _
   ByVal Curve As Curve, _
   ByVal NewEdgeCount As System.Integer, _
   ByRef NewEdges As Edge, _
   ByVal NewFaceCount As System.Integer, _
   ByRef NewFaces As Face2 _
) 
```

```

Dim instance As IFace2
Dim Curve As Curve
Dim NewEdgeCount As System.Integer
Dim NewEdges As Edge
Dim NewFaceCount As System.Integer
Dim NewFaces As Face2
 
instance.IImprintCurve(Curve, NewEdgeCount, NewEdges, NewFaceCount, NewFaces)
```

```

void IImprintCurve( 
   Curve Curve,
   System.int NewEdgeCount,
   out Edge NewEdges,
   System.int NewFaceCount,
   out Face2 NewFaces
)
```

```

void IImprintCurve( 
   Curve^ Curve,
   System.int NewEdgeCount,
   [Out] Edge^ NewEdges,
   System.int NewFaceCount,
   [Out] Face2^ NewFaces
) 
```

#### Parameters

*Curve*
:   Pointer to the [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) to imprint on the face

*NewEdgeCount*
:   Number of new edges to create

*NewEdges*
:   Array of new [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) created by the imprinted curve of size NewEdgeCount

*NewFaceCount*
:   Number of new faces to create

*NewFaces*
:   Array of new [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) created by the imprinted curve of size NewFaceCount

Remarks

Before calling this method, call [IFace2::ImprintCurveCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ImprintCurveCount.md) to get the size of the arrays.

The specified curve must lie on the face.

To imprint a curve on a new face of a temporary body, create a copy of the original curve and imprint the copy of the curve on the new face.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::ImprintCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ImprintCurve.md)
