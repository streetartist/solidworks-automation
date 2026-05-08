# GetClosestPointOn Method (ISurface)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetClosestPointOn`

Uses the X,Y,Z input point to determine the closest point on the surface.
Uses the X,Y,Z input point to determine the closest point on the surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetClosestPointOn( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Object
```

```

Dim instance As ISurface
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Object
 
value = instance.GetClosestPointOn(X, Y, Z)
```

```

System.object GetClosestPointOn( 
   System.double X,
   System.double Y,
   System.double Z
)
```

```

System.Object^ GetClosestPointOn( 
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

Array of 5 doubles containing the (x,y,z) coordinates and the (u,v) parameters of the point on the surface

Example

[Create Imported Surface Body from Sketch (C#)](Create_Imported_Surface_Body_from_Sketch_Example_CSharp.htm)  
[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)  
[Evaluate Points on Surface (VBA)](Evaluate_Points_on_Surface_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetClosestPointOn.md)  
[ISurface::GetProjectedPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetProjectedPointOn.md)
