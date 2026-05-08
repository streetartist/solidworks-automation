# IEvaluate Method (ICoEdge)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IEvaluate`

Obsolete. Superseded by ICoEdge::IEvaluate2.
Obsolete. Superseded by [ICoEdge::IEvaluate2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IEvaluate2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IEvaluate( _
   ByVal Param As System.Double _
) As System.Double
```

```

Dim instance As ICoEdge
Dim Param As System.Double
Dim value As System.Double
 
value = instance.IEvaluate(Param)
```

```

System.double IEvaluate( 
   System.double Param
)
```

```

System.double IEvaluate( 
   System.double Param
) 
```

#### Parameters

*Param*
:   Curve parameter desired (U value desired for evaluation)

#### Return Value

Pointer to an array of doubles (see **Remarks**)

Remarks

The tangency vector is defined to be in the direction of the coedge.

The format of the return value is an array of 6 doubles:

- retval[0] x location on the curve
- retval[1] y location on the curve
- retval[2] z location on the curve
- retval[3] x vector describing the tangency at the parameter location on the coedge
- retval[4] y vector describing the tangency at the parameter location on the coedge
- retval[5] z vector describing the tangency at the parameter location on the coedge

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICoEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.md)  
[ICoEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge_members.md)  
[ICoEdge::Evaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~Evaluate.md)  
[ICoEdge::GetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurveParams.md)  
[ICoEdge::IGetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetCurveParams.md)
