# AddProfileBspline Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddProfileBspline`

Creates an B-spline profile curve and returns a pointer to that curve.
Creates an B-spline profile curve and returns a pointer to that curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddProfileBspline( _
   ByVal Props As System.Object, _
   ByVal Knots As System.Object, _
   ByVal CtrlPtCoords As System.Object _
) As System.Object
```

```

Dim instance As IBody2
Dim Props As System.Object
Dim Knots As System.Object
Dim CtrlPtCoords As System.Object
Dim value As System.Object
 
value = instance.AddProfileBspline(Props, Knots, CtrlPtCoords)
```

```

System.object AddProfileBspline( 
   System.object Props,
   System.object Knots,
   System.object CtrlPtCoords
)
```

```

System.Object^ AddProfileBspline( 
   System.Object^ Props,
   System.Object^ Knots,
   System.Object^ CtrlPtCoords
) 
```

#### Parameters

*Props*
:   Contains 4 integers packed into 2 double elements (see **Remarks**)

*Knots*
:   Array of numKnots (see Remarks)

*CtrlPtCoords*
:   Array of numCtrlPtCoord (see Remarks)

#### Return Value

[Curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

Remarks

You can use this method with [IBody2::CreateRevolutionSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateRevolutionSurface.md) to generate any surface of revolution or with [IBody2::CreateExtrusionSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateExtrusionSurface.md) to generate a tabulated cylinder.

The Props argument contains the following values:

- DimensionControlPoints
- Order
- NumCtrlPoints
- Periodicity

The length of the knots array is given by:

> numKnots = NumCtrlPoints + Order

The length of the CtrlPtCoords is given by:

> NumCtrlPtCoord = NumCtrlPoints + DimensionControlPoints

Example

[Create Reference Curve (C#)](Create_Reference_Curve_Example_CSharp.htm)  
[Create Reference Curve (VB.NET)](Create_Reference_Curve_Example_VBNET.htm)  
[Create Reference Curve (VBA)](Create_Reference_Curve_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::IAddProfileBspline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileBspline.md)
