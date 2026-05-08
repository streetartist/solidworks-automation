# GetIntersectCurveCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetIntersectCurveCount`

Obsolete. Superseded by ISurface::GetIntersectCurveCount2.
Obsolete. Superseded by [ISurface::GetIntersectCurveCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetIntersectCurveCount2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetIntersectCurveCount( _
   ByVal OtherCurve As Curve, _
   ByRef CurveBound As System.Double _
) As System.Integer
```

```

Dim instance As ISurface
Dim OtherCurve As Curve
Dim CurveBound As System.Double
Dim value As System.Integer
 
value = instance.GetIntersectCurveCount(OtherCurve, CurveBound)
```

```

System.int GetIntersectCurveCount( 
   Curve OtherCurve,
   ref System.double CurveBound
)
```

```

System.int GetIntersectCurveCount( 
   Curve^ OtherCurve,
   System.double% CurveBound
) 
```

#### Parameters

*OtherCurve*

*CurveBound*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)
