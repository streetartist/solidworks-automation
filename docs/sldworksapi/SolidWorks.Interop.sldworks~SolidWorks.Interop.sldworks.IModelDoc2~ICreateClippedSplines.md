# ICreateClippedSplines Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateClippedSplines`

Creates one or more sketch spline segments that are clipped against a given (x1, y1), (x2, y2) rectangle. This rectangle lies in the space of the active 2D sketch.
Creates one or more sketch spline segments that are clipped against a given (x1, y1), (x2, y2) rectangle. This rectangle lies in the space of the active 2D sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateClippedSplines( _
   ByRef PropArray As System.Integer, _
   ByRef KnotsArray As System.Double, _
   ByRef CntrlPntCoordArray As System.Double, _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double _
) As EnumSketchSegments
```

```

Dim instance As IModelDoc2
Dim PropArray As System.Integer
Dim KnotsArray As System.Double
Dim CntrlPntCoordArray As System.Double
Dim X1 As System.Double
Dim Y1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim value As EnumSketchSegments
 
value = instance.ICreateClippedSplines(PropArray, KnotsArray, CntrlPntCoordArray, X1, Y1, X2, Y2)
```

```

EnumSketchSegments ICreateClippedSplines( 
   ref System.int PropArray,
   ref System.double KnotsArray,
   ref System.double CntrlPntCoordArray,
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2
)
```

```

EnumSketchSegments^ ICreateClippedSplines( 
   System.int% PropArray,
   System.double% KnotsArray,
   System.double% CntrlPntCoordArray,
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2
) 
```

#### Parameters

*PropArray*
:   See Remarks

*KnotsArray*
:   See Remarks

*CntrlPntCoordArray*
:   See Remarks

*X1*
:   x component of the lower corner of the clipping rectangle

*Y1*
:   y component of the lower corner of the clipping rectangle

*X2*
:   x component of the upper corner of the clipping rectang

*Y2*
:   y component of the upper corner of the clipping rectang

#### Return Value

Newly created [sketch segments enumeration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchSegments.md)

Remarks

The rectangle lies in the space of the active 2D sketch. The results are undefined for calls made in an active 3D sketch.

The arrays are as follows:

- PropArray = [ Dimension, Order, NumControlPoints, Periodicity ]
- KnotsArray = [ NumControlPoints + Order ]
- CntrlPntCoordArray = [ NumControlPoints \* Dimension ]

If Dimension = 3, then CntrlPntCoordArray is an array of 3 doubles ( x, y, z ).

If Dimension = 4, then CntrlPntCoordArray is an array of 4 doubles ( x, y, z, w ) where w = weight.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::CreateClippedSplines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateClippedSplines.md)
