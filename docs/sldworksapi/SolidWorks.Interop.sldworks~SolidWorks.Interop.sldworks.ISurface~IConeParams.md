# IConeParams Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IConeParams`

Gets the parameters of a conical surface.
Gets the parameters of a conical surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property IConeParams As System.Double
```

```

Dim instance As ISurface
Dim value As System.Double
 
value = instance.IConeParams
```

```

System.double IConeParams {get;}
```

```

property System.double IConeParams {
   System.double get();
}
```

#### Property Value

Array of doubles describing the parameters of a conical surface

Remarks

Returns an array of 8 doubles:

- origin.x
- origin.y
- origin.z
- axis.x
- axis.y
- axis.z
- radius
- half angle

The half angle, origin, and radius parameters are in meters.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::ConeParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ConeParams.md)  
[ISurface::IsCone Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsCone.md)
