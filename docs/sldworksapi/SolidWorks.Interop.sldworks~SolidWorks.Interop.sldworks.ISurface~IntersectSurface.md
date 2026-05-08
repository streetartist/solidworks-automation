# IntersectSurface Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IntersectSurface`

Gets a surface-surface intersection.
Gets a surface-surface intersection.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IntersectSurface( _
   ByVal OtherSurf As System.Object, _
   ByRef CurveArray As System.Object, _
   ByRef BoundsArray As System.Object _
) As System.Boolean
```

```

Dim instance As ISurface
Dim OtherSurf As System.Object
Dim CurveArray As System.Object
Dim BoundsArray As System.Object
Dim value As System.Boolean
 
value = instance.IntersectSurface(OtherSurf, CurveArray, BoundsArray)
```

```

System.bool IntersectSurface( 
   System.object OtherSurf,
   out System.object CurveArray,
   out System.object BoundsArray
)
```

```

System.bool IntersectSurface( 
   System.Object^ OtherSurf,
   [Out] System.Object^ CurveArray,
   [Out] System.Object^ BoundsArray
) 
```

#### Parameters

*OtherSurf*
:   Intersecting [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)

*CurveArray*
:   Array of [curves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

*BoundsArray*
:   Array containing the curve bounds

#### Return Value

True if successful, false if not

Example

[Get Intersecting Faces (VBA)](Get_Intersecting_Faces_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::IIntersectSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IIntersectSurface.md)  
[ISurface::GetIntersectSurfaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetIntersectSurfaceCount.md)
