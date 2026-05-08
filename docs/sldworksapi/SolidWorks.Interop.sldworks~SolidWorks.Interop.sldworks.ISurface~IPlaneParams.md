# IPlaneParams Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IPlaneParams`

Gets the parameters of a planar surface.
Gets the parameters of a planar surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property IPlaneParams As System.Double
```

```

Dim instance As ISurface
Dim value As System.Double
 
value = instance.IPlaneParams
```

```

System.double IPlaneParams {get;}
```

```

property System.double IPlaneParams {
   System.double get();
}
```

#### Property Value

Array of doubles describing the parameters of a planar surface

Remarks

Returns an array of 6 double values:

normal.x

normal.y

normal.z

rootPoint.x

rootPoint.y

rootPoint.z

The rootPoint values are in meters.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::PlaneParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~PlaneParams.md)  
[ISurface::IsPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsPlane.md)
