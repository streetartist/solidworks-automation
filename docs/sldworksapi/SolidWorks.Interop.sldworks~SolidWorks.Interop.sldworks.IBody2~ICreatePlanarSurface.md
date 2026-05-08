# ICreatePlanarSurface Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreatePlanarSurface`

Creates a new infinite planar surface.
Creates a new infinite planar surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreatePlanarSurface( _
   ByVal VRootPoint As System.Object, _
   ByVal VNormal As System.Object _
) As Surface
```

```

Dim instance As IBody2
Dim VRootPoint As System.Object
Dim VNormal As System.Object
Dim value As Surface
 
value = instance.ICreatePlanarSurface(VRootPoint, VNormal)
```

```

Surface ICreatePlanarSurface( 
   System.object VRootPoint,
   System.object VNormal
)
```

```

Surface^ ICreatePlanarSurface( 
   System.Object^ VRootPoint,
   System.Object^ VNormal
) 
```

#### Parameters

*VRootPoint*
:   Array of 3 doubles (x,y,z)

*VNormal*
:   Array of 3 doubles (x,y,z)

#### Return Value

New planar [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)

Remarks

You can use this method with:

- A set of related functions that construct a body from trimmed surfaces.
- Trimming curve creation routines (for example, [ISurface::IAddTrimmingLoop2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IAddTrimmingLoop2.md)) to construct a trimmed surface.

To create a planar trimmed surface directly from the vertex points, see [IBody2::ICreatePlanarTrimSurfaceDLL](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreatePlanarTrimSurfaceDLL.md).

Any existing object created by this method is destroyed if you call this method again.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::CreatePlanarSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreatePlanarSurface.md)
