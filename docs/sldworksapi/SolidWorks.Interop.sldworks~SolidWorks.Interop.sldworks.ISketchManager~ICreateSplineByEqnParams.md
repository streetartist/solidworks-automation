# ICreateSplineByEqnParams Method (ISketchManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSplineByEqnParams`

Creates a B-curve from B-spline data; that is, a set of B-spline vertices (control points) and a knot vector.
Creates a B-curve from B-spline data; that is, a set of B-spline vertices (control points) and a knot vector.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateSplineByEqnParams( _
   ByRef Properties As System.Integer, _
   ByVal KnotArrayCount As System.Integer, _
   ByRef Knots As System.Double, _
   ByVal ControlPointArrayCount As System.Integer, _
   ByRef ControlPoints As System.Double _
) As SketchSegment
```

```

Dim instance As ISketchManager
Dim Properties As System.Integer
Dim KnotArrayCount As System.Integer
Dim Knots As System.Double
Dim ControlPointArrayCount As System.Integer
Dim ControlPoints As System.Double
Dim value As SketchSegment
 
value = instance.ICreateSplineByEqnParams(Properties, KnotArrayCount, Knots, ControlPointArrayCount, ControlPoints)
```

```

SketchSegment ICreateSplineByEqnParams( 
   ref System.int Properties,
   System.int KnotArrayCount,
   ref System.double Knots,
   System.int ControlPointArrayCount,
   ref System.double ControlPoints
)
```

```

SketchSegment^ ICreateSplineByEqnParams( 
   System.int% Properties,
   System.int KnotArrayCount,
   System.double% Knots,
   System.int ControlPointArrayCount,
   System.double% ControlPoints
) 
```

#### Parameters

*Properties*
:   - in-process, unmanaged C++: Pointer to an array of properties including dimension, order, number of control points, periodicity (see Remarks)

    VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*KnotArrayCount*
:   Number of knots

*Knots*
:   - in-process, unmanaged C++: Pointer to an array of knots (e.g., knot1, knot2, and so on)
    - VBA, VB.NET, C#, and C++/CLI: Not supported

*ControlPointArrayCount*
:   Number of control points

*ControlPoints*
:   - in-process, unmanaged C++: Pointer to an array of control points (e.g., controlpoint1[dimension], controlpoint2[dimension], and so on)

    VBA, VB.NET, C#, and C++/CLI: Not supported

#### Return Value

[Sketch segment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) for the spline

Remarks

The Properties array contains four longs (placed in the first four doubles in the array):

- Dimension
- Order
- Number of Control Points
- Periodicity ( true or false)

The Knots array contains doubles with (Number of Control Points + Order) elements.

The size of the ControlPoints array is based upon the curve dimension.

- Dimension = 2 then each Control Point is an array of 2 doubles ( x, y )
- Dimension = 3 then each Control Point is an array of 3 doubles ( x, y, z)
- Dimension = 4 then each Control Point is an array of 4 doubles ( x, y, z, w ) where w = weight

The parameters are provided as three arrays.

Pass the control point coordinates to this routine in sketch space. The Z value is  interpreted as 0. In certain situations, you must transform your B-curve parameters to sketch space using [ISketch::ModelToSketchTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~ModelToSketchTransform.md).

NOTE: The curve can be either periodic or non-periodic. If the generated spline is a closed spline, then it must be flagged as periodic. Additionally, splines generated in sketches must be G1 continuous. If the data passed to this method does not generate a G1 continuous spline, then it is rejected and a spline is not created. If your data is not G1 continuous, then you must split the spline into multiple G1 segments and call this method for each segment.

This method does not work with [ISketchManager::AddToDB](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddToDB.md) or [ISketchManager::DisplayWhenAdded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~DisplayWhenAdded.md). It always adds the spline directly to the database (as if ISketchManager::AddToDB(True) is in effect), and you must redraw your document window to see the entities that you added (as if ISketchManager::DisplayWhenAdded(False) is in effect).

To create 3D splines, see [IModelDoc2::InsertCurveFilePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFilePoint.md) and related functions.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::CreateSpline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSpline.md)  
[ISketchManager::CreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplineByEqnParams.md)  
[ISketchManager::CreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplinesByEqnParams.md)  
[ISketchManager::ICreateSpline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSpline.md)  
[ISketchManager::ICreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSplinesByEqnParams.md)
