# CylinderParams Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CylinderParams`

Gets the parameters of a cylindrical surface.
Gets the parameters of a cylindrical surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property CylinderParams As System.Object
```

```

Dim instance As ISurface
Dim value As System.Object
 
value = instance.CylinderParams
```

```

System.object CylinderParams {get;}
```

```

property System.Object^ CylinderParams {
   System.Object^ get();
}
```

#### Property Value

Array of doubles describing the parameters of a cylindrical surface

Remarks

Returns an array of 7 doubles:

- origin.x
- origin.y
- origin.z
- axis.x
- axis.y
- axis.z
- radius

The origin and radius parameters are in meters.

Example

[Get Angle of Hole Not Normal to a Face (VBA)](Get_Angle_of_Hole_Not_Normal_to_a_Face_Example_VB.htm)  
[Get Entities Attached to Cosmetic Thread (VBA)](Get_Entities_Attached_To_Cosmetic_Thread_Example_VB.htm)  
[Get Parameters of Cylindrical Surface (VBA)](Get_Parameters_of_Cylindrical_Surface_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::ICylinderParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ICylinderParams.md)  
[ISurface::IsCylinder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsCylinder.md)
