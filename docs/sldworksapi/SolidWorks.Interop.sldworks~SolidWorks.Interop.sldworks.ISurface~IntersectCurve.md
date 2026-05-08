# IntersectCurve Method (ISurface)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IntersectCurve`

Obsolete. Superseded by ISurface::IntersectCurve2.
Obsolete. Superseded by [ISurface::IntersectCurve2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IIntersectCurve2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IntersectCurve( _
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
 
value = instance.IntersectCurve(OtherCurve, CurveBound, PointArray, TArray, UvArray)
```

```

System.bool IntersectCurve( 
   System.object OtherCurve,
   System.object CurveBound,
   out System.object PointArray,
   out System.object TArray,
   out System.object UvArray
)
```

```

System.bool IntersectCurve( 
   System.Object^ OtherCurve,
   System.Object^ CurveBound,
   [Out] System.Object^ PointArray,
   [Out] System.Object^ TArray,
   [Out] System.Object^ UvArray
) 
```

#### Parameters

*OtherCurve*

*CurveBound*

*PointArray*

*TArray*

*UvArray*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)
