# IsCylinder Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsCylinder`

Gets whether the surface is a cylinder.
Gets whether the surface is a cylinder.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsCylinder() As System.Boolean
```

```

Dim instance As ISurface
Dim value As System.Boolean
 
value = instance.IsCylinder()
```

```

System.bool IsCylinder()
```

```

System.bool IsCylinder(); 
```

#### Return Value

True if surface is cylinder, false if not

Example

[Calculate Closest Distance Between Faces (VBA)](Calculate_Closest_Distance_Between_Faces_Example_VB.htm)  
[Get Angle of Hole Not Normal to a Face (VBA)](Get_Angle_of_Hole_Not_Normal_to_a_Face_Example_VB.htm)  
[Get Parameters of Cylindrical Surface (VBA)](Get_Parameters_of_Cylindrical_Surface_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[IModeler::CreateCylindricalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateCylindricalSurface2.md)  
[IModeler::ICreateCylindricalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateCylindricalSurface2.md)  
[ISurface::CylinderParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CylinderParams.md)  
[ISurface::ICylinderParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ICylinderParams.md)
