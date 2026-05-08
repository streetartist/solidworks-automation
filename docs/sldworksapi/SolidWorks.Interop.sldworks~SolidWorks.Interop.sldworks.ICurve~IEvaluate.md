# IEvaluate Method (ICurve)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IEvaluate`

Obsolete. Superseded by ICurve::Evaluate2.
Obsolete. Superseded by [ICurve::Evaluate2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Evaluate2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IEvaluate( _
   ByVal Parameter As System.Double _
) As System.Double
```

```

Dim instance As ICurve
Dim Parameter As System.Double
Dim value As System.Double
 
value = instance.IEvaluate(Parameter)
```

```

System.double IEvaluate( 
   System.double Parameter
)
```

```

System.double IEvaluate( 
   System.double Parameter
) 
```

#### Parameters

*Parameter*
:   Curve parameter

#### Return Value

Pointer to an array of doubles (see **Remarks**)

Remarks

To determine a valid parameter range, use [ICurve::GetEndParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetEndParams.md) or [IEdge::GetCurveParams2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams2.md) or [IEdge::IGetCurveParams2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetCurveParams2.md).

The OLE Automation return value is an array of doubles with the following format:

[ PointX, PointY, PointZ, TangentX, TangentY, TangentZ, Success ]

where:

- PointX, PointY, and PointZ represent the 3D point in space for the given parameter
- TangentX, TangentY, and TangentZ represent the tangent vector at the point
- True if the operation is successful

The COM return value is an array of 6 doubles representing the point and tangent. The success value is determined from the HRESULT return.

This method returns values in meters.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)
