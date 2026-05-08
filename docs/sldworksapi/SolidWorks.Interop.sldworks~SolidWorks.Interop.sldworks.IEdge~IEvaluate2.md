# IEvaluate2 Method (IEdge)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IEvaluate2`

Evaluates the edge for the specified U parameter.
Evaluates the edge for the specified U parameter.

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

Dim instance As IEdge
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
:   Curve parameter U value (see **Remarks**)

*NumberOfDerivatives*
:   Number of derivatives (see **Remarks**)

#### Return Value

Array of doubles  (see Remarks)

Remarks

Use [IEdge::IGetCurveParams2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetCurveParams2.md) to determine the valid range of U parameter values for Parameter.

The returned array contains ((NumberOfDerivatives + 1) \* 3) + 1 doubles:

[evaluated\_point], [evaluated\_derivative\_1],...[evaluated\_derivative\_NumberOfDerivatives, **[***status\_code***]**

where *status\_code* is a packed double. After unpacking *status\_code* into two longs, the lower long value is 1 for success or 0 for error. See the Example in [IEdge::Evaluate2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Evaluate2.md).

|  |  |
| --- | --- |
| If curve type [ICurve::Identity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.md) is... | Then the maximum number of derivatives is... |
| Line/circle/ellipse | 2 |
| Intersection curve | 2 |
| Constant parameter line | Determined by underlying surface |
| SP-curve | 2 |
| B-curve | Any number |

For a curve of type swCurveTypes\_e::TRIMMED\_TYPE, the number of derivatives is determined by the base curve as obtained from [ICurve::GetBaseCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBaseCurve.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)  
[IEdge::GetCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams2.md)
