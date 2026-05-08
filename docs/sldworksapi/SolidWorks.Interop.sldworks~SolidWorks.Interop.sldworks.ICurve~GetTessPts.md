# GetTessPts Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetTessPts`

Gets a set of points that represent the tessellation of this curve.
Gets a set of points that represent the tessellation of this curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTessPts( _
   ByVal ChordTolerance As System.Double, _
   ByVal LengthTolerance As System.Double, _
   ByVal StartPoint As System.Object, _
   ByVal EndPoint As System.Object _
) As System.Object
```

```

Dim instance As ICurve
Dim ChordTolerance As System.Double
Dim LengthTolerance As System.Double
Dim StartPoint As System.Object
Dim EndPoint As System.Object
Dim value As System.Object
 
value = instance.GetTessPts(ChordTolerance, LengthTolerance, StartPoint, EndPoint)
```

```

System.object GetTessPts( 
   System.double ChordTolerance,
   System.double LengthTolerance,
   System.object StartPoint,
   System.object EndPoint
)
```

```

System.Object^ GetTessPts( 
   System.double ChordTolerance,
   System.double LengthTolerance,
   System.Object^ StartPoint,
   System.Object^ EndPoint
) 
```

#### Parameters

*ChordTolerance*
:   Chord tolerance to use in tessellation (meters); this is the maximum permitted distance from a cord to the curve between the cord endpoints; the smallest allowable value for this parameter is 1E-8; if 0.0 or a value smaller than 1E-8 is specified, then 1E-8 is used by default

*LengthTolerance*
:   Length tolerance to be used to filter out very short segments (meters); this method does not return tessellated segments shorter than this value

*StartPoint*
:   Array containing the start point of the curve

*EndPoint*
:   Array containing the end point of the curve

#### Return Value

Array of doubles containing the tessellation points (see **Remarks**)

Remarks

The array returned contains the x, y, z location of the tessellation points:

> **[** *x1, y1, z1, x2, y2, z2,* ... **]**

Example

[Create Space Parameter Curve on Surface (VBA)](Create_Space_Parameter_Curve_on_Surface_Example_VB.htm)  
[Find Outside Edges of Face (VBA)](Find_Outside_Edges_of_Face_Example_VB.htm)  
[Get Intersecting Faces (VBA)](Get_Intersecting_Faces_Example_VB.htm)  
[Get Length of Edge (VBA)](Get_Length_of_Edge_Example_VB.htm)  
[Get Reference Curve Information (VBA)](Get_Reference_Curve_Information_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::IGetTessPts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetTessPts.md)  
[ICurve::IGetTessPtsSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetTessPtsSize.md)
