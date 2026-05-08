# ConeParams Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ConeParams`

Obsolete. Superseded by ISurface::ConeParams2.
Obsolete. Superseded by [ISurface::ConeParams2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ConeParams2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ConeParams As System.Object
```

```

Dim instance As ISurface
Dim value As System.Object
 
value = instance.ConeParams
```

```

System.object ConeParams {get;}
```

```

property System.Object^ ConeParams {
   System.Object^ get();
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
[ISurface::IConeParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IConeParams.md)  
[ISurface::IsCone Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsCone.md)
