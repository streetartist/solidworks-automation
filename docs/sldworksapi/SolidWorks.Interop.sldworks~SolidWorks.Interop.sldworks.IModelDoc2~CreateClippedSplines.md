# CreateClippedSplines Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateClippedSplines`

Creates one or more sketch spline segments that are clipped against a given (x1, y1), (x2, y2) rectangle. This rectangle lies in the space of the active 2D sketch.
Creates one or more sketch spline segments that are clipped against a given (x1, y1), (x2, y2) rectangle. This rectangle lies in the space of the active 2D sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateClippedSplines( _
   ByVal ParamsIn As System.Object, _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double _
) As System.Object
```

```

Dim instance As IModelDoc2
Dim ParamsIn As System.Object
Dim X1 As System.Double
Dim Y1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim value As System.Object
 
value = instance.CreateClippedSplines(ParamsIn, X1, Y1, X2, Y2)
```

```

System.object CreateClippedSplines( 
   System.object ParamsIn,
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2
)
```

```

System.Object^ CreateClippedSplines( 
   System.Object^ ParamsIn,
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2
) 
```

#### Parameters

*ParamsIn*
:   See Remarks

*X1*
:   x component of the lower corner of the clipping rectangle

*Y1*
:   y component of the lower corner of the clipping rectangle

*X2*
:   x component of the upper corner of the clipping rectangle

*Y2*
:   y component of the upper corner of the clipping rectangle

#### Return Value

Array of newly created sketch segments

Remarks

The rectangle lies in the space of the active 2D sketch. The results are undefined for calls made in an active 3D sketch.

The ParamsIn argument in Visual Basic for Applications (VBA) is a SafeArray of size (4 + numKnots + numControlPointDoubles) as follows:

[ Dimension, Order, NumControlPoints, Periodicity, knot1, knot2,..., ControlPoint1[Dimension], ControlPoint2[Dimension],... ]

where:

Dimension, Order, NumControlPoints, and Periodicity are integer values.

The size of the knot array is determined by ( NumControlPoints + Order ).

The size of the control point array is based upon the curve dimension:

- If Dimension = 3, then ControlPoint is an array of 3 doubles ( x, y, z ).
- If Dimension = 4, then ControlPoint is an array of 4 doubles ( x, y, z, w ) where w = weight.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::ICreateClippedSplines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateClippedSplines.md)
