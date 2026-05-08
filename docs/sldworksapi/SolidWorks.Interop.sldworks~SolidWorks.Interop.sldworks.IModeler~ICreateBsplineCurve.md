# ICreateBsplineCurve Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBsplineCurve`

Creates a b-spline curve.
Creates a b-spline curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateBsplineCurve( _
   ByRef Properties As System.Integer, _
   ByRef KnotArray As System.Double, _
   ByRef ControlPointCoordArray As System.Double _
) As Curve
```

```

Dim instance As IModeler
Dim Properties As System.Integer
Dim KnotArray As System.Double
Dim ControlPointCoordArray As System.Double
Dim value As Curve
 
value = instance.ICreateBsplineCurve(Properties, KnotArray, ControlPointCoordArray)
```

```

Curve ICreateBsplineCurve( 
   ref System.int Properties,
   ref System.double KnotArray,
   ref System.double ControlPointCoordArray
)
```

```

Curve^ ICreateBsplineCurve( 
   System.int% Properties,
   System.double% KnotArray,
   System.double% ControlPointCoordArray
) 
```

#### Parameters

*Properties*
:   Array containing 4 integers packed into 2 double elements (see **Remarks**)

*KnotArray*
:   Array of numKnots doubles (see Remarks)

*ControlPointCoordArray*
:   Array of NumCtrlPtCoord doubles (see Remarks)

#### Return Value

B-spline [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

Remarks

The Properties argument contains the following values:

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
[IModeler::CreateBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBsplineCurve.md)  
[IModeler::CreateBsplineSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBsplineSurface.md)  
[IModeler::ICreateBsplineSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBsplineSurface.md)
