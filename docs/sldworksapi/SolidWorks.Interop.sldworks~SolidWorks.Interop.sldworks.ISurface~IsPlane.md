# IsPlane Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsPlane`

Gets whether the surface is a planar surface.
Gets whether the surface is a planar surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsPlane() As System.Boolean
```

```

Dim instance As ISurface
Dim value As System.Boolean
 
value = instance.IsPlane()
```

```

System.bool IsPlane()
```

```

System.bool IsPlane(); 
```

#### Return Value

True if surface is planar surface, false if not

Example

[Create Infinite Plane (VBA)](Create_Infinite_Plane_Example_VB.htm)  
[Get Angle of Hole Not Normal to a Face (VBA)](Get_Angle_of_Hole_Not_Normal_to_a_Face_Example_VB.htm)  
[Get Parameters of Planar Surface (VBA)](Get_Parameters_of_Planar_Surface_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::PlaneParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~PlaneParams.md)  
[ISurface::IPlaneParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IPlaneParams.md)  
[IModeler::CreatePlanarSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreatePlanarSurface2.md)  
[IModeler::ICreatePlanarSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreatePlanarSurface2.md)  
[ISurfacePlanarFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData.md)
