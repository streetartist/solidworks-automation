# IAddProfileBspline Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileBspline`

Creates an B-spline profile curve and returns a pointer to that curve.
Creates an B-spline profile curve and returns a pointer to that curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddProfileBspline( _
   ByVal Props As System.Object, _
   ByVal Knots As System.Object, _
   ByVal CtrlPtCoords As System.Object _
) As Curve
```

```

Dim instance As IBody2
Dim Props As System.Object
Dim Knots As System.Object
Dim CtrlPtCoords As System.Object
Dim value As Curve
 
value = instance.IAddProfileBspline(Props, Knots, CtrlPtCoords)
```

```

Curve IAddProfileBspline( 
   System.object Props,
   System.object Knots,
   System.object CtrlPtCoords
)
```

```

Curve^ IAddProfileBspline( 
   System.Object^ Props,
   System.Object^ Knots,
   System.Object^ CtrlPtCoords
) 
```

#### Parameters

*Props*
:   Contains four integers packed into two double elements (see **Remarks**)

*Knots*
:   Array of numKnots (see **Remarks**)

*CtrlPtCoords*
:   Array of numCtrlPtCoord (see **Remarks**)

#### Return Value

[ICurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

Remarks

You can use this method with [IBody2::ICreateRevolutionSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateRevolutionSurface.md) to generate any surface of revolution or with [IBody2::ICreateExtrusionSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateExtrusionSurface.md) to generate a tabulated cylinder.

The Props argument contains the following values:

- DimensionControlPoints
- Order
- NumCtrlPoints
- Periodicity

The length of the knots array is given by:

> numKnots = NumCtrlPoints + Order

The length of the CtrlPtCoords is given by:

> numCtrlPtCoord = NumCtrlPoints + DimensionControlPoints

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::AddProfileBspline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddProfileBspline.md)
