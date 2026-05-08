# AddTrimmingLoop2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~AddTrimmingLoop2`

Creates a trimming loop out of specified surface parametric UV-curves and adds it to a list of such loops.
Creates a trimming loop out of specified surface parametric UV-curves and adds it to a list of such loops.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddTrimmingLoop2( _
   ByVal NCrvs As System.Integer, _
   ByVal VOrder As System.Object, _
   ByVal VDim As System.Object, _
   ByVal VPeriodic As System.Object, _
   ByVal VNumKnots As System.Object, _
   ByVal VNumCtrlPoints As System.Object, _
   ByVal VKnots As System.Object, _
   ByVal VCtrlPointDbls As System.Object, _
   ByVal UvRange As System.Object _
) As System.Boolean
```

```

Dim instance As ISurface
Dim NCrvs As System.Integer
Dim VOrder As System.Object
Dim VDim As System.Object
Dim VPeriodic As System.Object
Dim VNumKnots As System.Object
Dim VNumCtrlPoints As System.Object
Dim VKnots As System.Object
Dim VCtrlPointDbls As System.Object
Dim UvRange As System.Object
Dim value As System.Boolean
 
value = instance.AddTrimmingLoop2(NCrvs, VOrder, VDim, VPeriodic, VNumKnots, VNumCtrlPoints, VKnots, VCtrlPointDbls, UvRange)
```

```

System.bool AddTrimmingLoop2( 
   System.int NCrvs,
   System.object VOrder,
   System.object VDim,
   System.object VPeriodic,
   System.object VNumKnots,
   System.object VNumCtrlPoints,
   System.object VKnots,
   System.object VCtrlPointDbls,
   System.object UvRange
)
```

```

System.bool AddTrimmingLoop2( 
   System.int NCrvs,
   System.Object^ VOrder,
   System.Object^ VDim,
   System.Object^ VPeriodic,
   System.Object^ VNumKnots,
   System.Object^ VNumCtrlPoints,
   System.Object^ VKnots,
   System.Object^ VCtrlPointDbls,
   System.Object^ UvRange
) 
```

#### Parameters

*NCrvs*
:   Number of surface parametric (UV) curves constituting the loop and the size of each of the VOrder, VDim, VPeriodic, VNumKnots, VNumControlPnts arrays

*VOrder*
:   Array containing NCrvs longs (VBA), Integers (VB.NET), or ints (C#, C++) representing orders of the curves (see **Remarks**)

*VDim*
:   Array containing NCrvs longs (VBA), Integers (VB.NET), or ints (C#, C++) representing dimensions (2, 3, or 4) of the control points of the curves (see **Remarks**)

*VPeriodic*
:   Array containing NCrvs longs (VBA), Integers (VB.NET), or ints (C#, C++) representing whether the curve is periodic (1) or non-periodic (0) (see **Remarks**)

*VNumKnots*
:   Array containing NCrvs longs (VBA), Integers (VB.NET), or ints (C#, C++) representing number of knots on the curves (see **Remarks**)

*VNumCtrlPoints*
:   Array containing NCrvs longs (VBA), Integers (VB.NET), or ints (C#, C++) representing number of control points on the curves (see **Remarks**)

*VKnots*
:   Knot vector array of <TotalNumKnots> doubles, where TotalNumKnots = (TotalNumKnots + VNumKnots[i]) for i = 1 to NCrvs (see **Remarks**)

*VCtrlPointDbls*
:   Control point coordinate array of <TotalNumCPCoords> doubles, where TotalNumCPCoords = (TotalNumCPCoords + (VDim[i] \* VNumCtrlPoints[i])) for i = 1 to NCrvs (see **Remarks**)

*UvRange*
:   Array of four doubles representing U Low, U High, V Low, and V High (see **Remarks**)

#### Return Value

True if successful in adding a trimming loop to the surface, false if not

Remarks

The list of trimming loops is created by a previous call to one of the base surface creation functions, [IBody2::CreateRevolutionSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateRevolutionSurface.md) or [IBody2::CreatePlanarSurface.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreatePlanarSurface.md)

The information on each UV-curve is in b-spline form (knots and control point coordinates) and is compacted into two arrays, VKnots and VCtrlPointDbls.

Order of each curve in VOrder is, at a minimum, 2. A second order curve is a linear curve.

For each curve in VNumCtrlPoints, VOrder, and VNumKnots, (NumCtrlPoints >= Order) and (NumKnots = NumCtrlPoints + Order).

Dim for each curve in VDim specifies the dimension of each CtrlPointDbl set in VCtrlPointDbls. This method expects 2D-polynomial (X,Y) or 2D-rational (X,Y,Weight) curves to be passed as trimming curves. However, you can set a flag so that this method accepts 3D-polynomial (X,Y,Z) or 3D-rational (X,Y,Z,Weight) trim curves. To do this, negate the absolute value of the first value in the VDim array. For example, if the first VDim value is 3, set it to -3. When you do this, 3D trim curves are expected.

If Dim is:

- 2, specify (X,Y) control points in each CtrlPointDbl set.
- -2, specify (X,Y,Z) control points in each CtrlPointDbl set.
- 3, specify (X,Y,Weight) control points in each CtrlPointDbl.
- -3, specify (X,Y,Z,Weight) control points in each CtrlPointDbl.

Multiplicity of a knot is the number of times it is repeated in the knot vector. There are specific rules around number of knots, knot multiplicity, and curve order. For example, if a curve's Periodic value is:

- 0 (non-periodic), there must be (NumCtrlPoints + Order) knots and the maximum multiplicity of any knot is Order.
- 1 (periodic), there must be (NumCtrlPoints + 1) knots and the maximum multiplicity of any knot is Order. If a knot has multiplicity greater than 1, repetitions must occur at the end of the knot vector.

If you do not want to specify a UV range, use null or Nothing in the UvRange array elements.

After calling this method to add a trimming loop, you can generate the trimmed surface by calling [IBody2::CreateTrimmedSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateTrimmedSurface.md). You can create a body from trimmed surfaces using [IBody2::CreateBodyFromSurfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBodyFromSurfaces.md).

NOTE: It is highly recommended that you consult other resources for the mathematics behind b-splines, knots, knot multiplicity, and control points before attempting to use this method.

Example

[Create Body Using Trimmed Surfaces (VBA)](Create_Body_using_Trimmed_Surfaces_Example_VB.htm)  
[Create Body Using Trimmed Surfaces (VB.NET)](Create_Body_using_Trimmed_Surfaces_Example_VBNET.htm)  
[Create Body Using Trimmed Surfaces (C#)](Create_Body_using_Trimmed_Surfaces_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::IAddTrimmingLoop2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IAddTrimmingLoop2.md)
