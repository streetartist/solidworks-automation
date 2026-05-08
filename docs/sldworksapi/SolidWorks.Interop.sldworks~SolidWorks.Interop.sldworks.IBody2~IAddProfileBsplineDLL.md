# IAddProfileBsplineDLL Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileBsplineDLL`

Adds a profile B-spline.
Adds a profile B-spline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddProfileBsplineDLL( _
   ByRef Properties As System.Integer, _
   ByRef KnotArray As System.Double, _
   ByRef ControlPointCoordArray As System.Double _
) As Curve
```

```

Dim instance As IBody2
Dim Properties As System.Integer
Dim KnotArray As System.Double
Dim ControlPointCoordArray As System.Double
Dim value As Curve
 
value = instance.IAddProfileBsplineDLL(Properties, KnotArray, ControlPointCoordArray)
```

```

Curve IAddProfileBsplineDLL( 
   ref System.int Properties,
   ref System.double KnotArray,
   ref System.double ControlPointCoordArray
)
```

```

Curve^ IAddProfileBsplineDLL( 
   System.int% Properties,
   System.double% KnotArray,
   System.double% ControlPointCoordArray
) 
```

#### Parameters

*Properties*
:   Contains 4 longs (see **Remarks**)

*KnotArray*
:   Pointer to an array of numKnots doubles (see **Remarks**)

*ControlPointCoordArray*
:   Pointer to an array of numCtrlPtCoord doubles (see **Remarks**)

#### Return Value

Pointer to the profile B-spline [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

Remarks

You can use this method with [IBody2::ICreateRevolutionSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateRevolutionSurface.md) to generate any surface  
of revolution or with [IBody2::ICreateExtrusionSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateExtrusionSurface.md) to generate a tabulated cylinder.

The Properties argument contains the following values:

- DimensionControlPoints
- Order
- NumCtrlPoints
- Periodicity

The length of the KnotArray argument is:

> numKnots = NumCtrlPoints + Order

The length of the ControlPointCoordArray is:

> numCtrlPtCoord = NumCtrlPoints \* DimensionControlPoints

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
