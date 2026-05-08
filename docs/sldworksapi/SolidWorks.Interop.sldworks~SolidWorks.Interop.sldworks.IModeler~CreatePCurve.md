# CreatePCurve Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreatePCurve`

Creates a pcurve.
Creates a pcurve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreatePCurve( _
   ByVal Surface As System.Object, _
   ByVal Props As System.Object, _
   ByVal Knots As System.Object, _
   ByVal CtrlPtCoords As System.Object _
) As System.Object
```

```

Dim instance As IModeler
Dim Surface As System.Object
Dim Props As System.Object
Dim Knots As System.Object
Dim CtrlPtCoords As System.Object
Dim value As System.Object
 
value = instance.CreatePCurve(Surface, Props, Knots, CtrlPtCoords)
```

```

System.object CreatePCurve( 
   System.object Surface,
   System.object Props,
   System.object Knots,
   System.object CtrlPtCoords
)
```

```

System.Object^ CreatePCurve( 
   System.Object^ Surface,
   System.Object^ Props,
   System.Object^ Knots,
   System.Object^ CtrlPtCoords
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

#### Return Value

[Pcurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

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

Example

[Create Space Parameter Curve On Surface (VBA)](Create_Space_Parameter_Curve_on_Surface_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::ICreatePCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreatePCurve.md)  
[ICurve::GetPCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetPCurveParams.md)  
[ICurve::IGetPCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetPCurveParams.md)  
[ICurve::IGetPCurveParamsSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetPCurveParamsSize.md)  
[IModeler::CreateBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBsplineCurve.md)  
[IModeler::ICreateBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBsplineCurve.md)
