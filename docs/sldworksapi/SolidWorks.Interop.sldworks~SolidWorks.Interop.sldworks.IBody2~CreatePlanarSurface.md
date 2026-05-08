# CreatePlanarSurface Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreatePlanarSurface`

Creates a new infinite planar surface.
Creates a new infinite planar surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreatePlanarSurface( _
   ByVal VRootPoint As System.Object, _
   ByVal VNormal As System.Object _
) As System.Object
```

```

Dim instance As IBody2
Dim VRootPoint As System.Object
Dim VNormal As System.Object
Dim value As System.Object
 
value = instance.CreatePlanarSurface(VRootPoint, VNormal)
```

```

System.object CreatePlanarSurface( 
   System.object VRootPoint,
   System.object VNormal
)
```

```

System.Object^ CreatePlanarSurface( 
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

New planar surface

Remarks

You can use this method with:

- A set of related functions that construct a body from trimmed surfaces.
- Trimming curve creation routines (for example, [ISurface::AddTrimmingLoop2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~AddTrimmingLoop2.md)) to construct a trimmed surface.

To create a planar trimmed surface directly from the vertex points, see [IBody2::CreatePlanarTrimSurfaceDLL](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreatePlanarTrimSurfaceDLL.md).

Any existing object created by this method is destroyed if you call this method again.

Example

[Create Body Using Trimmed Surfaces (VBA)](Create_Body_using_Trimmed_Surfaces_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::ICreatePlanarSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreatePlanarSurface.md)
