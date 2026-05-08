# ICreatePCurve Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreatePCurve`

Creates a pcurve.
Creates a pcurve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreatePCurve( _
   ByVal Surface As Surface, _
   ByRef Props As System.Integer, _
   ByRef Knots As System.Double, _
   ByRef CtrlPtCoords As System.Double _
) As Curve
```

```

Dim instance As IModeler
Dim Surface As Surface
Dim Props As System.Integer
Dim Knots As System.Double
Dim CtrlPtCoords As System.Double
Dim value As Curve
 
value = instance.ICreatePCurve(Surface, Props, Knots, CtrlPtCoords)
```

```

Curve ICreatePCurve( 
   Surface Surface,
   ref System.int Props,
   ref System.double Knots,
   ref System.double CtrlPtCoords
)
```

```

Curve^ ICreatePCurve( 
   Surface^ Surface,
   System.int% Props,
   System.double% Knots,
   System.double% CtrlPtCoords
) 
```

#### Parameters

*Surface*
:   [Surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md) associated with the pcurve

*Props*
:   Array containing 4 integers packed into 2 double elements (see **Remarks**)

*Knots*
:   Array of numKnots (see **Remarks**)

*CtrlPtCoords*
:   Array of numCtrlPtCoord (see **Remarks**)

Remarks

The Props argument contains the following values:

- DimensionControlPoints
- Order
- NumCtrlPoints
- Periodicity

|  |  |
| --- | --- |
| **Length of this array...** | **Given by...** |
| Knots | numKnots = NumCtrlPoints + Order |
| CtrlPtCoords | NumCtrlPtCoord = NumCtrlPoints \* DimensionControlPoints |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::CreatePCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreatePCurve.md)  
[ICurve::GetPCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetPCurveParams.md)  
[ICurve::IGetPCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetPCurveParams.md)  
[ICurve::IGetPCurveParamsSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetPCurveParamsSize.md)  
[IModeler::CreateBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBsplineCurve.md)  
[IModeler::ICreateBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBsplineCurve.md)
