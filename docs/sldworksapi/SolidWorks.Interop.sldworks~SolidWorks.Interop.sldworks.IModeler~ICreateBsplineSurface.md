# ICreateBsplineSurface Method (IModeler)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBsplineSurface`

Creates a b-spline surface.
Creates a b-spline surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateBsplineSurface( _
   ByRef Properties As System.Integer, _
   ByRef UKnotArray As System.Double, _
   ByRef VKnotArray As System.Double, _
   ByRef ControlPointCoordArray As System.Double _
) As Surface
```

```

Dim instance As IModeler
Dim Properties As System.Integer
Dim UKnotArray As System.Double
Dim VKnotArray As System.Double
Dim ControlPointCoordArray As System.Double
Dim value As Surface
 
value = instance.ICreateBsplineSurface(Properties, UKnotArray, VKnotArray, ControlPointCoordArray)
```

```

Surface ICreateBsplineSurface( 
   ref System.int Properties,
   ref System.double UKnotArray,
   ref System.double VKnotArray,
   ref System.double ControlPointCoordArray
)
```

```

Surface^ ICreateBsplineSurface( 
   System.int% Properties,
   System.double% UKnotArray,
   System.double% VKnotArray,
   System.double% ControlPointCoordArray
) 
```

#### Parameters

*Properties*
:   Array of 8 integers (see **Remarks**)

*UKnotArray*
:   Array of numUKnots (see Remarks)

*VKnotArray*
:   Array of numVKnots (see Remarks)

*ControlPointCoordArray*
:   Array of numCtrlPtCoord (see Remarks)

#### Return Value

[Surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)

Remarks

|  |  |
| --- | --- |
| **Number of elements in this array...** | **Given by...** |
| UKnots | numUKnots = numU\_CtrlPoints + Uorder |
| VKnots | numVKnots = numV\_CtrlPoints + Vorder |
| CtrlPtCoords | numCtrlPtCoord =( NumV\_CtrlPoints \* NumU\_CtrlPoints \* DimensionControlPoints ) |

**NOTE:** The order of the UV control points are reversed if you used [ISurface::GetBSurfParams3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetBSurfParams3.md) or [ISurface::IGetBSurfParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetBSurfParams.md) to get the data. You do not need to reverse the UV control points; instead, you can switch the UV knots and related parameters.

For periodics, the first knot must have multiplicity = 1 and all excess multiplicity must be imposed on the last knot. Therefore, a valid periodic knot vector would be { 0, 1, 2, 3, 3, 3 } for a cubic curve. The control point on the seam of the closed curve cannot be replicated at both ends; it should occur only at the beginning.

To convert from a clamped periodic curve (numKnots = numCtrlPts + Order, ctrlPts replicated, knot multiplicity = order at each end) to a SOLIDWORKS periodic curve, remove all but one of the knots at the beginning of the vector and remove one at the end. Also remove the last control point to avoid the point replication.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::CreateBsplineSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBsplineSurface.md)  
[IBody2::CreateBsplineSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBsplineSurface.md)  
[IBody2::ICreateBsplineSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBsplineSurface.md)  
[IModeler::CreateBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBsplineCurve.md)  
[IModeler::ICreateBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBsplineCurve.md)  
[IModeler::CreateConicalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateConicalSurface2.md)  
[IModeler::CreateCoonsBSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateCoonsBSurface.md)  
[IModeler::CreateCylindricalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateCylindricalSurface2.md)  
[IModeler::CreateExtrusionSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrusionSurface.md)  
[IModeler::CreateLoftSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLoftSurface.md)  
[IModeler::CreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateOffsetSurface.md)  
[IModeler::CreatePlanarSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreatePlanarSurface2.md)  
[IModeler::CreateRuledSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateRuledSurface.md)  
[IModeler::CreateSweptSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSweptSurface.md)  
[IModeler::CreateToroidalSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateToroidalSurface.md)  
[IModeler::ICreateConicalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateConicalSurface2.md)  
[IModeler::ICreateCylindricalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateCylindricalSurface2.md)  
[IModeler::ICreateExtrusionSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateExtrusionSurface.md)  
[IModeler::ICreateLoftSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateLoftSurface.md)  
[IModeler::ICreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateOffsetSurface.md)  
[IModeler::ICreatePlanarSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreatePlanarSurface2.md)  
[IModeler::ICreateRuledSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateRuledSurface.md)  
[IModeler::ICreateSweptSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSweptSurface.md)  
[IModeler::ICreateToroidalSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateToroidalSurface.md)
