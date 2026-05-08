# IEvaluate2 Method (ICurve)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IEvaluate2`

Evaluates the curve at the specified parameter of the curve.
Evaluates the curve at the specified parameter of the curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IEvaluate2( _
   ByVal Parameter As System.Double, _
   ByVal NumberOfDerivatives As System.Integer _
) As System.Double
```

```

Dim instance As ICurve
Dim Parameter As System.Double
Dim NumberOfDerivatives As System.Integer
Dim value As System.Double
 
value = instance.IEvaluate2(Parameter, NumberOfDerivatives)
```

```

System.double IEvaluate2( 
   System.double Parameter,
   System.int NumberOfDerivatives
)
```

```

System.double IEvaluate2( 
   System.double Parameter,
   System.int NumberOfDerivatives
) 
```

#### Parameters

*Parameter*
:   Curve parameter

*NumberOfDerivatives*
:   Number of derivatives

#### Return Value

Array of doubles (see Remarks)

Remarks

To determine a valid parameter range, use [ICurve::GetEndParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetEndParams.md) or [IEdge::GetCurveParams2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams2.md).

The format of the return value is an array of (NumberOfDerivatives + 1) \* 3 doubles:

[evaluated point], [evaluated derivative 1],...[evaluated derivative NumberOfDerivatives]

In pseudo mathematical notation, this could be written as:

    P(t)  P(t)/dt  P(t)/dtdt ..........

 In terms of the number of derivatives that can be returned for a curve type, you could write:

 

|  |  |
| --- | --- |
| Curve type | Maximum number of derivatives |
| Line/circle/ellipse | 2 |
| Intersection curve | 2 |
| Constant parameter line | Determined by underlying surface |
| SP-curve | 2 |
| B-curve | Any number |

where the curve type is from [ICurve::Identity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.md).

For a curve of type swCurveTypes\_e::TRIMMED\_TYPE, the number of derivatives is determined by the base curve as obtained from [ICurve::GetBaseCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBaseCurve.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::Evaluate2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Evaluate2.md)
