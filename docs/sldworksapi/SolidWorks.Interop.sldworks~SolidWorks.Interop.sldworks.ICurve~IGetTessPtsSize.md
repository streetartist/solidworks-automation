# IGetTessPtsSize Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetTessPtsSize`

Gets the size of the array required by ICurve::IGetTessPts.
Gets the size of the array required by [ICurve::IGetTessPts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetTessPts.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTessPtsSize( _
   ByVal ChordTolerance As System.Double, _
   ByVal LengthTolerance As System.Double, _
   ByRef StartPoint As System.Double, _
   ByRef EndPoint As System.Double _
) As System.Integer
```

```

Dim instance As ICurve
Dim ChordTolerance As System.Double
Dim LengthTolerance As System.Double
Dim StartPoint As System.Double
Dim EndPoint As System.Double
Dim value As System.Integer
 
value = instance.IGetTessPtsSize(ChordTolerance, LengthTolerance, StartPoint, EndPoint)
```

```

System.int IGetTessPtsSize( 
   System.double ChordTolerance,
   System.double LengthTolerance,
   ref System.double StartPoint,
   ref System.double EndPoint
)
```

```

System.int IGetTessPtsSize( 
   System.double ChordTolerance,
   System.double LengthTolerance,
   System.double% StartPoint,
   System.double% EndPoint
) 
```

#### Parameters

*ChordTolerance*
:   Chord tolerance to be used in tessellation (meters); this is the maximum permitted  
    distance from a cord to the curve between the cord endpoints

*LengthTolerance*
:   Length tolerance to be used to filter out very short segments (meters);  tessellated  
    segments shorter than this value are not returned

*StartPoint*
:   Pointer to an array containing the start point of the curve

*EndPoint*
:   Pointer to an array containing the end point of the curve

#### Return Value

Number of doubles returned when [ICurve::IGetTessPts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetTessPts.md) is called

Remarks

To get the actual tessellation points, use [ICurve::IGetTessPts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetTessPts.md). Arguments passed to ICurve::IGetTessPts must match the arguments passed to this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::GetTessPts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetTessPts.md)
