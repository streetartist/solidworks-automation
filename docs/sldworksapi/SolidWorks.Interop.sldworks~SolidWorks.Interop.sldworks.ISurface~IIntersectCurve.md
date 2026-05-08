# IIntersectCurve Method (ISurface)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IIntersectCurve`

Obsolete. Superseded by ISurface::IIntersectCurve2.
Obsolete. Superseded by [ISurface::IIntersectCurve2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IIntersectCurve2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IIntersectCurve( _
   ByVal OtherCurve As Curve, _
   ByRef CurveBound As System.Double, _
   ByVal PointCount As System.Integer, _
   ByRef PointArray As System.Double, _
   ByRef TArray As System.Double, _
   ByRef UvArray As System.Double _
) As System.Boolean
```

```

Dim instance As ISurface
Dim OtherCurve As Curve
Dim CurveBound As System.Double
Dim PointCount As System.Integer
Dim PointArray As System.Double
Dim TArray As System.Double
Dim UvArray As System.Double
Dim value As System.Boolean
 
value = instance.IIntersectCurve(OtherCurve, CurveBound, PointCount, PointArray, TArray, UvArray)
```

```

System.bool IIntersectCurve( 
   Curve OtherCurve,
   ref System.double CurveBound,
   System.int PointCount,
   out System.double PointArray,
   out System.double TArray,
   out System.double UvArray
)
```

```

System.bool IIntersectCurve( 
   Curve^ OtherCurve,
   System.double% CurveBound,
   System.int PointCount,
   [Out] System.double PointArray,
   [Out] System.double TArray,
   [Out] System.double UvArray
) 
```

#### Parameters

*OtherCurve*

*CurveBound*

*PointCount*

*PointArray*

*TArray*

*UvArray*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)
