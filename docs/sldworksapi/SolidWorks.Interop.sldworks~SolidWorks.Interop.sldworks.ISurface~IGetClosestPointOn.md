# IGetClosestPointOn Method (ISurface)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetClosestPointOn`

Uses the X,Y,Z input point to determine the closest point on the surface.
Uses the X,Y,Z input point to determine the closest point on the surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetClosestPointOn( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Double
```

```

Dim instance As ISurface
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Double
 
value = instance.IGetClosestPointOn(X, Y, Z)
```

```

System.double IGetClosestPointOn( 
   System.double X,
   System.double Y,
   System.double Z
)
```

```

System.double IGetClosestPointOn( 
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*X*
:   x coordinate of the approximate position on the surface

*Y*
:   y coordinate of the approximate position on the surface

*Z*
:   z coordinate of the approximate position on the surface

#### Return Value

- in-process, unmanaged C++: Pointer to an array of 5 doubles containing the (x,y,z) coordinates and the (u,v) parameters of the point on the surface

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetClosestPointOn.md)  
[ISurface::GetProjectedPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetProjectedPointOn.md)
