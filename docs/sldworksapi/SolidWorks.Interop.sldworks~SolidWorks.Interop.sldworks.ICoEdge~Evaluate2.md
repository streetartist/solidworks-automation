# Evaluate2 Method (ICoEdge)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~Evaluate2`

Gets the (X,Y,Z) location and the tangency vector on the coedge at the specified position.
Gets the (X,Y,Z) location and the tangency vector on the coedge at the specified position.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Evaluate2( _
   ByVal Param As System.Double, _
   ByVal NumberOfDerivatives As System.Integer _
) As System.Object
```

```

Dim instance As ICoEdge
Dim Param As System.Double
Dim NumberOfDerivatives As System.Integer
Dim value As System.Object
 
value = instance.Evaluate2(Param, NumberOfDerivatives)
```

```

System.object Evaluate2( 
   System.double Param,
   System.int NumberOfDerivatives
)
```

```

System.Object^ Evaluate2( 
   System.double Param,
   System.int NumberOfDerivatives
) 
```

#### Parameters

*Param*
:   Curve parameter desired (U value desired for evaluation)

*NumberOfDerivatives*
:   Number of derivatives

#### Return Value

Array of doubles (see **Remarks**)

Remarks

The tangency vector is defined to be in the direction of the coedge.

The format of the return value is an array of (NumberOfDerivatives + 1) \* 3 doubles:

[evaluated point], [evaluated derivative 1],...[evaluated derivative NumberOfDerivatives]

In pseudo mathematical notation, this can be written as:

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

[ICoEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.md)  
[ICoEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge_members.md)  
[ICoEdge::IEvaluate2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IEvaluate2.md)  
[ICoEdge::GetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurveParams.md)  
[ICoEdge::IGetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetCurveParams.md)
