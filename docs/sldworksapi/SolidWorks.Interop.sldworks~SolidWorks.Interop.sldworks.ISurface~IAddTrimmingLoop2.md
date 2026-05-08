# IAddTrimmingLoop2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IAddTrimmingLoop2`

Creates a trimming loop out of specified surface parametric (UV-curves) and adds it to a list of such loops.
Creates a trimming loop out of specified surface parametric (UV-curves) and adds it to a list of such loops.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IAddTrimmingLoop2( _
   ByVal CurveCount As System.Integer, _
   ByRef Order As System.Integer, _
   ByRef Dim As System.Integer, _
   ByRef Periodic As System.Integer, _
   ByRef NumKnots As System.Integer, _
   ByRef NumCtrlPoints As System.Integer, _
   ByRef Knots As System.Double, _
   ByRef CtrlPointDbls As System.Double, _
   ByRef UvRange As System.Double _
) 
```

```

Dim instance As ISurface
Dim CurveCount As System.Integer
Dim Order As System.Integer
Dim Dim As System.Integer
Dim Periodic As System.Integer
Dim NumKnots As System.Integer
Dim NumCtrlPoints As System.Integer
Dim Knots As System.Double
Dim CtrlPointDbls As System.Double
Dim UvRange As System.Double
 
instance.IAddTrimmingLoop2(CurveCount, Order, Dim, Periodic, NumKnots, NumCtrlPoints, Knots, CtrlPointDbls, UvRange)
```

```

void IAddTrimmingLoop2( 
   System.int CurveCount,
   ref System.int Order,
   ref System.int Dim,
   ref System.int Periodic,
   ref System.int NumKnots,
   ref System.int NumCtrlPoints,
   ref System.double Knots,
   ref System.double CtrlPointDbls,
   ref System.double UvRange
)
```

```

void IAddTrimmingLoop2( 
   System.int CurveCount,
   System.int% Order,
   System.int% Dim,
   System.int% Periodic,
   System.int% NumKnots,
   System.int% NumCtrlPoints,
   System.double% Knots,
   System.double% CtrlPointDbls,
   System.double% UvRange
) 
```

#### Parameters

*CurveCount*
:   Number of surface parametric (UV) curves constituting the loop; the size of Order, Dim, Periodic, NumKnots, and NumControlPnts arrays

*Order*
:   Orders of the curves; array of CurveCount longs (VBA), Integers (VB.NET), or ints (C#, C++)

*Dim*
:   Dimensions of the curves' control points; array of CurveCount longs (VBA), Integers (VB.NET), or ints (C#, C++); if you set the first value in this array to negative of its absolute value, then 3D trim curves are expected

*Periodic*
:   0 for non-periodic or 1 for periodic; array of CurveCount longs (VBA), Integers (VB.NET), or ints (C#, C++)

*NumKnots*
:   Number of knots in the curves; array of CurveCount longs (VBA), Integers (VB.NET), or ints (C#, C++)

*NumCtrlPoints*
:   Number of control points in the curves; array of CurveCount longs (VBA), Integers (VB.NET), or ints (C#, C++)

*Knots*
:   Knot vectors of the curves; array of <TotalNumKnots> doubles, where TotalNumKnots = (TotalNumKnots + NumKnots[i]) for i = 1 to CurveCount

*CtrlPointDbls*
:   Control point coordinates of the curves; array of <TotalNumCPCoords> doubles, where TotalNumCPCoords = (TotalNumCPCoords + (Dim[i] \* NumCtrlPoints[i])) for i = 1 to CurveCount

*UvRange*
:   Array of four doubles defining U Low U High V Low V High

Remarks

The list of trimming loops is created by a previous call to one of the base surface creation functions, [IBody2::CreateRevolutionSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateRevolutionSurface.md) or [IBody2::CreatePlanarSurface.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreatePlanarSurface.md)

The information on each UV-curve is in b-spline form (knots and control point coordinates) and is compacted into two arrays, VKnots and VCtrlPointDbls.

Order of each curve in Order is, at a minimum, 2. A second order curve is a linear curve.

For each curve in NumCtrlPoints, Order, and NumKnots, (NumCtrlPoints >= Order) and (NumKnots = NumCtrlPoints + Order).

Dim for each curve in Dim specifies the dimension of each CtrlPointDbl set in CtrlPointDbls. This method expects 2D-polynomial (X,Y) or 2D-rational (X,Y,Weight) curves to be passed as trimming curves. However, you can set a flag so that this method accepts 3D-polynomial (X,Y,Z) or 3D-rational (X,Y,Z,Weight) trim curves. To do this, negate the absolute value of the first value in the VDim array. For example, if the first VDim value is 3, set it to -3. When you do this, 3D trim curves are expected.

If Dim is:

- 2, specify (X,Y) control points in each CtrlPointDbl sub-array.
- -2, specify (X,Y,Z) control points in each CtrlPointDbl sub-array.
- 3, specify (X,Y,Weight) control points in each CtrlPointDbl sub-array.
- -3, specify (X,Y,Z,Weight) control points in each CtrlPointDbl sub-array.

Multiplicity of a knot is the number of times it is repeated in the knot vector. There are specific rules around number of knots, knot multiplicity, and curve order. For example, if a curve's Periodic value is:

- 0 (non-periodic), there must be (NumCtrlPoints + Order) knots and the maximum multiplicity of any knot is Order.
- 1 (periodic), there must be (NumCtrlPoints + 1) knots and the maximum multiplicity of any knot is Order. If a knot has multiplicity greater than 1, repetitions must occur at the end of the knot vector.

If you do not want to specify a UV range, use null or Nothing in the UvRange array elements.

After calling this method to add a trimming loop, you can generate a trimmed surface by calling [IBody2::CreateTrimmedSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateTrimmedSurface.md). You can create a body from trimmed surfaces using [IBody2::CreateBodyFromSurfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBodyFromSurfaces.md).

NOTE: It is highly recommended that you consult other resources for the mathematics behind b-splines, knots, knot multiplicity, and control points before attempting to use this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::AddTrimmingLoop2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~AddTrimmingLoop2.md)
