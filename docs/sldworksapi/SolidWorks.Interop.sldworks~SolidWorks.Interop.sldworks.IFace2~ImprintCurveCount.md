# ImprintCurveCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ImprintCurveCount`

Gets the number of new edges and faces to create when imprinting a curve.
Gets the number of new edges and faces to create when imprinting a curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ImprintCurveCount( _
   ByVal Curve As Curve, _
   ByRef NewEdgeCount As System.Integer, _
   ByRef NewFaceCount As System.Integer _
) 
```

```

Dim instance As IFace2
Dim Curve As Curve
Dim NewEdgeCount As System.Integer
Dim NewFaceCount As System.Integer
 
instance.ImprintCurveCount(Curve, NewEdgeCount, NewFaceCount)
```

```

void ImprintCurveCount( 
   Curve Curve,
   out System.int NewEdgeCount,
   out System.int NewFaceCount
)
```

```

void ImprintCurveCount( 
   Curve^ Curve,
   [Out] System.int NewEdgeCount,
   [Out] System.int NewFaceCount
) 
```

#### Parameters

*Curve*
:   Pointer to the [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

*NewEdgeCount*
:   Number of new edges to create when imprinting this curve

*NewFaceCount*
:   Number of new faces to create when imprinting this curve

Remarks

Call this method before calling [IFace2::IImprintCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IImprintCurve.md) to get the size of the edges and faces arrays.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::ImprintCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ImprintCurve.md)
