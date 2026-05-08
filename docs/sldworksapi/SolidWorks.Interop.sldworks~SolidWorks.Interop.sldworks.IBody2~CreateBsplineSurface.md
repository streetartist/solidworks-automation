# CreateBsplineSurface Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBsplineSurface`

Creates a new B-spline surface.
Creates a new B-spline surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateBsplineSurface( _
   ByVal Props As System.Object, _
   ByVal UKnots As System.Object, _
   ByVal VKnots As System.Object, _
   ByVal CtrlPtCoords As System.Object _
) As System.Object
```

```

Dim instance As IBody2
Dim Props As System.Object
Dim UKnots As System.Object
Dim VKnots As System.Object
Dim CtrlPtCoords As System.Object
Dim value As System.Object
 
value = instance.CreateBsplineSurface(Props, UKnots, VKnots, CtrlPtCoords)
```

```

System.object CreateBsplineSurface( 
   System.object Props,
   System.object UKnots,
   System.object VKnots,
   System.object CtrlPtCoords
)
```

```

System.Object^ CreateBsplineSurface( 
   System.Object^ Props,
   System.Object^ UKnots,
   System.Object^ VKnots,
   System.Object^ CtrlPtCoords
) 
```

#### Parameters

*Props*
:   Array containing 8 integers packed as 4 double elements (see **Remarks**)

*UKnots*
:   Array of numUKnots (see Remarks)

*VKnots*
:   Array of numVKnots (see Remarks)

*CtrlPtCoords*
:   Array of numCtrlPtCoord (see Remarks)

#### Return Value

A new B-spline surface

Remarks

You can use this method with trimming curve creation routines (for example, [ISurface::AddTrimmingLoop2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~AddTrimmingLoop2.md)) to construct a trimmed surface.

The Props array contains the following elements. These are integers packed into a double array in the Dispatch version.

- Uorder, Vorder
- numV\_CtrlPoints, numU\_CtrlPoints
- Uperiodicity, Vperiodicity
- DimensionControlPoints, UNUSED ( set =0 )

The number of elements in the UKnots array is given by:

numUKnots = numU\_CtrlPoints + Uorder

The number of elements in the VKnots array is given by:

numVKnots = numV\_CtrlPoints + Vorder

The number of elements in the ctrlPtCoords array is given by:

> numCtrlPtCoord =( NumV\_CtrlPoints \* NumU\_CtrlPoints \* DimensionControlPoints )

**NOTE:** The order of the UV control points are reversed if you used [ISurface::GetBSurfParams3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetBSurfParams3.md) or [ISurface::IGetBSurfParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetBSurfParams.md) to get the data. You do not need to reverse the UV control points; instead, you can switch the UV knots and related parameters.

For periodics, the first knot must have multiplicity = 1 and all excess multiplicity must be imposed on the last knot. Therefore, a valid periodic knot vector would be { 0, 1, 2, 3, 3, 3 } for a cubic curve. The control point on the seam of the closed curve cannot be replicated at both ends; it should occur only at the beginning.

To convert from a clamped periodic curve (numKnots = numCtrlPts + Order, ctrlPts replicated, knot multiplicity = order at each end) to a SOLIDWORKS periodic curve, remove all but one of the knots at the beginning of the vector and remove one at the end. Also remove the last control point to avoid the point replication.

Any existing object created by this method is destroyed if you call this method again.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::ICreateBsplineSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBsplineSurface.md)
