# CreateBsplineCurve Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBsplineCurve`

Creates a b-spline curve.
Creates a b-spline curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateBsplineCurve( _
   ByVal Props As System.Object, _
   ByVal Knots As System.Object, _
   ByVal CtrlPtCoords As System.Object _
) As System.Object
```

```

Dim instance As IModeler
Dim Props As System.Object
Dim Knots As System.Object
Dim CtrlPtCoords As System.Object
Dim value As System.Object
 
value = instance.CreateBsplineCurve(Props, Knots, CtrlPtCoords)
```

```

System.object CreateBsplineCurve( 
   System.object Props,
   System.object Knots,
   System.object CtrlPtCoords
)
```

```

System.Object^ CreateBsplineCurve( 
   System.Object^ Props,
   System.Object^ Knots,
   System.Object^ CtrlPtCoords
) 
```

#### Parameters

*Props*
:   Array containing 4 integers packed into 2 double elements (see **Remarks**)

*Knots*
:   Array of numKnots doubles (see Remarks)

*CtrlPtCoords*
:   Array of NumCtrlPtCoord doubles (see Remarks)

#### Return Value

B-spline [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

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
| CtrlPtCoords | NumCtrlPtCoord = NumCtrlPoints + DimensionControlPoints |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::ICreateBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBsplineCurve.md)  
[IBody2::AddProfileBspline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddProfileBspline.md)  
[IBody2::IAddProfileBspline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileBspline.md)
