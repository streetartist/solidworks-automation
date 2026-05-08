# ITorusParams Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ITorusParams`

Gets the parameters of a toroidal surface.
Gets the parameters of a toroidal surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ITorusParams As System.Double
```

```

Dim instance As ISurface
Dim value As System.Double
 
value = instance.ITorusParams
```

```

System.double ITorusParams {get;}
```

```

property System.double ITorusParams {
   System.double get();
}
```

#### Property Value

Array of doubles describing the parameters of a toroidal surface

Remarks

Returns an array of 8 double values:

center.x

center.y

center.z

axis.x

axis.y

axis.z

major radius - the distance between the center of torus and the center of revolved circle

minor radius - the radius of the revolved circle

NOTES:

- The real major radius (the outer radius) of the torus is major radius + minor radius.
- The center, major radius, and minor radius are in meters.
- Possible values that indicate a type of self-intersecting torus:

  - Apple - when the major radius is positive and less than or equal to the minor radius.
  - Lemon - when the major radius is negative and the sum of the radii is positive.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::TorusParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~TorusParams.md)  
[ISurface::IsTorus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsTorus.md)
