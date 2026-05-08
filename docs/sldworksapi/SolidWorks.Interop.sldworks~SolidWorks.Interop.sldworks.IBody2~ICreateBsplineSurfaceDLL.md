# ICreateBsplineSurfaceDLL Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBsplineSurfaceDLL`

Creates a B-spline surface in this body.
Creates a B-spline surface in this body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateBsplineSurfaceDLL( _
   ByRef Properties As System.Integer, _
   ByRef UKnotArray As System.Double, _
   ByRef VKnotArray As System.Double, _
   ByRef ControlPointCoordArray As System.Double _
) As Surface
```

```

Dim instance As IBody2
Dim Properties As System.Integer
Dim UKnotArray As System.Double
Dim VKnotArray As System.Double
Dim ControlPointCoordArray As System.Double
Dim value As Surface
 
value = instance.ICreateBsplineSurfaceDLL(Properties, UKnotArray, VKnotArray, ControlPointCoordArray)
```

```

Surface ICreateBsplineSurfaceDLL( 
   ref System.int Properties,
   ref System.double UKnotArray,
   ref System.double VKnotArray,
   ref System.double ControlPointCoordArray
)
```

```

Surface^ ICreateBsplineSurfaceDLL( 
   System.int% Properties,
   System.double% UKnotArray,
   System.double% VKnotArray,
   System.double% ControlPointCoordArray
) 
```

#### Parameters

*Properties*
:   Contains 8 longs (see **Remarks**)

*UKnotArray*
:   Array of numUKnots doubles (see Remarks)

*VKnotArray*
:   Array of numVKnots doubles (see Remarks)

*ControlPointCoordArray*
:   Array of numCtrlPtCoord doubles (see Remarks)

#### Return Value

New B-spline [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)

Remarks

You can use this method with trimming curve creation routines (for example, [ISurface::AddTrimmingLoop2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~AddTrimmingLoop2.md)) to construct a trimmed surface.

The Properties argument contains the following elements. These are integers packed into a double array in the Dispatch version.

- Uorder, Vorder
- numV\_CtrlPoints, numU\_CtrlPoints
- Uperiodicity, Vperiodicity
- DimensionControlPoints, UNUSED ( set = 0 )

The number of elements in UKnotArray is:

> numUKnots = numU\_CtrlPoints + Uorder

The number of elements in VKnotArray is:

> numVKnots = numV\_CtrlPoints + Vorder

The number of elements in ControlPointCoordArray is :

> numCtrlPtCoord =( NumV\_CtrlPoints \* NumU\_CtrlPoints \* DimensionControlPoints )

**NOTE:** The order of the UV control points are reversed if you used [ISurface::GetBSurfParams3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetBSurfParams3.md) or [ISurface::IGetBSurfParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetBSurfParams.md) to get the data. You do not need to reverse the UV control points; instead, you can switch the UV knots and related parameters.

For periodics, the first knot must have multiplicity = 1 and all excess multiplicity must be imposed on the last knot. Therefore, a valid periodic knot vector would be { 0, 1, 2, 3, 3, 3 } for a cubic curve. The control point on the seam of the closed curve cannot be replicated at both ends; it should occur only at the beginning.

To convert a clamped periodic curve (numKnots = numCtrlPts + Order, ctrlPts replicated, knot multiplicity = order at each end) to a SOLIDWORKS periodic curve, remove all but one of the knots at the beginning of the vector and remove one at the end. Also, remove the last control point to avoid the point replication.

Any existing object created by this method is destroyed if you call this method again.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
