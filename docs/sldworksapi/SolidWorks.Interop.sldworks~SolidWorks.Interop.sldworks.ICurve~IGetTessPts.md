# IGetTessPts Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetTessPts`

Gets a set of points that represent the tessellation of this curve.
Gets a set of points that represent the tessellation of this curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTessPts( _
   ByVal ChordTolerance As System.Double, _
   ByVal LengthTolerance As System.Double, _
   ByRef StartPoint As System.Double, _
   ByRef EndPoint As System.Double _
) As System.Double
```

```

Dim instance As ICurve
Dim ChordTolerance As System.Double
Dim LengthTolerance As System.Double
Dim StartPoint As System.Double
Dim EndPoint As System.Double
Dim value As System.Double
 
value = instance.IGetTessPts(ChordTolerance, LengthTolerance, StartPoint, EndPoint)
```

```

System.double IGetTessPts( 
   System.double ChordTolerance,
   System.double LengthTolerance,
   ref System.double StartPoint,
   ref System.double EndPoint
)
```

```

System.double IGetTessPts( 
   System.double ChordTolerance,
   System.double LengthTolerance,
   System.double% StartPoint,
   System.double% EndPoint
) 
```

#### Parameters

*ChordTolerance*
:   Chord tolerance to use in tessellation (meters); this is the maximum permitted distance from a cord to the curve between the cord endpoints; the smallest allowable value for this parameter is 1E-8; if 0.0 or a value smaller than 1E-8 is specified, then 1E-8 is used by default

*LengthTolerance*
:   Length tolerance to be used to filter out very short segments (meters); this method does not return tessellated segments shorter than this value

*StartPoint*
:   Pointer to an array containing the start point of the curve

*EndPoint*
:   Pointer to an array containing the end point of the curve

#### Return Value

- in-process, unmanaged C++: Pointer to an array containing the tessellation points (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The array returned contains the x, y, z location of the tessellation points:

> **[** *x1, y1, z1, x2, y2, z2,* ... **]**

Before calling this method, call [ICurve::IGetTessPtsSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetTessPtsSize.md) to determine the size of the array needed to contain the return values of this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::GetTessPts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetTessPts.md)
