# ImprintCurve Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ImprintCurve`

Imprints a curve on the selected face.
Imprints a curve on the selected face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ImprintCurve( _
   ByVal Curve As System.Object, _
   ByRef NewEdges As System.Object, _
   ByRef NewFaces As System.Object _
) 
```

```

Dim instance As IFace2
Dim Curve As System.Object
Dim NewEdges As System.Object
Dim NewFaces As System.Object
 
instance.ImprintCurve(Curve, NewEdges, NewFaces)
```

```

void ImprintCurve( 
   System.object Curve,
   out System.object NewEdges,
   out System.object NewFaces
)
```

```

void ImprintCurve( 
   System.Object^ Curve,
   [Out] System.Object^ NewEdges,
   [Out] System.Object^ NewFaces
) 
```

#### Parameters

*Curve*
:   [Curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) to imprint on the face

*NewEdges*
:   Array of new [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) created by the imprinted curve

*NewFaces*
:   Array of new [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) created by the imprinted curve

Remarks

The specified curve must lie on the face.

To imprint a curve on a new face of a temporary body, create a copy of the original curve and imprint the copy of the curve on the new face.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::IImprintCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IImprintCurve.md)  
[IFace2::ImprintCurveCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ImprintCurveCount.md)
