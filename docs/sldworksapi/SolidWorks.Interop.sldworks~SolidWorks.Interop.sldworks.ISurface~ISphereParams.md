# ISphereParams Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ISphereParams`

Gets the parameters of a spherical surface.
Gets the parameters of a spherical surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ISphereParams As System.Double
```

```

Dim instance As ISurface
Dim value As System.Double
 
value = instance.ISphereParams
```

```

System.double ISphereParams {get;}
```

```

property System.double ISphereParams {
   System.double get();
}
```

#### Property Value

Array of doubles describing the parameters of a spherical surface

Remarks

Returns an array of 4 doubles:

center.x

center.y

center.z

radius

The center and radius values are in meters.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::SphereParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~SphereParams.md)  
[ISurface::IsSphere Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsSphere.md)
