# IntersectCurve2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IntersectCurve2`

Gets a surface-curve intersection.
Gets a surface-curve intersection.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IntersectCurve2( _
   ByVal OtherCurve As System.Object, _
   ByVal CurveBound As System.Object, _
   ByRef PointArray As System.Object, _
   ByRef TArray As System.Object, _
   ByRef UvArray As System.Object _
) As System.Boolean
```

```

Dim instance As ISurface
Dim OtherCurve As System.Object
Dim CurveBound As System.Object
Dim PointArray As System.Object
Dim TArray As System.Object
Dim UvArray As System.Object
Dim value As System.Boolean
 
value = instance.IntersectCurve2(OtherCurve, CurveBound, PointArray, TArray, UvArray)
```

```

System.bool IntersectCurve2( 
   System.object OtherCurve,
   System.object CurveBound,
   out System.object PointArray,
   out System.object TArray,
   out System.object UvArray
)
```

```

System.bool IntersectCurve2( 
   System.Object^ OtherCurve,
   System.Object^ CurveBound,
   [Out] System.Object^ PointArray,
   [Out] System.Object^ TArray,
   [Out] System.Object^ UvArray
) 
```

#### Parameters

*OtherCurve*
:   [Curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

*CurveBound*
:   Array of 6 doubles representing the start and end points of the curve

*PointArray*
:   Array of points

*TArray*
:   Array of parameters on curve

*UvArray*
:   Array of parameters on surface

#### Return Value

True if getting the intersection succeeded, false if not

Remarks

The curves must be bounded.

Visual Basic and C++ Dispatch applications should use this method instead of using [ISurface::GetIntersectCurveCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetIntersectCurveCount2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::IIntersectCurve2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IIntersectCurve2.md)
