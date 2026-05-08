# PlaneParams Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~PlaneParams`

Gets the parameters of a planar surface.
Gets the parameters of a planar surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property PlaneParams As System.Object
```

```

Dim instance As ISurface
Dim value As System.Object
 
value = instance.PlaneParams
```

```

System.object PlaneParams {get;}
```

```

property System.Object^ PlaneParams {
   System.Object^ get();
}
```

#### Property Value

Array of doubles describing the parameters of a planar surface

Remarks

Returns an array of 6 double values:

normal.x

normal.y

normal.z

rootPoint.x

rootPoint.y

rootPoint.z

The rootPoint values are in meters.

Example

[Create Infinite Plane (VBA)](Create_Infinite_Plane_Example_VB.htm)  
[Get Angle of Hole Not Normal to a Face (VBA)](Get_Angle_of_Hole_Not_Normal_to_a_Face_Example_VB.htm)  
[Get Normal of Planar Surface (VBA)](Get_Normal_of_Planar_Surface_Example_VB.htm)  
[Get Parameters of Planar Surface (VBA)](Get_Parameters_of_Planar_Surface_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::IPlaneParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IPlaneParams.md)  
[ISurface::IsPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsPlane.md)
