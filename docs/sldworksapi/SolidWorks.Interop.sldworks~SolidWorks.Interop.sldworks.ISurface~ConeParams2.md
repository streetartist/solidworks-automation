# ConeParams2 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ConeParams2`

Gets the parameters of a conical surface.
Gets the parameters of a conical surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ConeParams2 As System.Object
```

```

Dim instance As ISurface
Dim value As System.Object
 
value = instance.ConeParams2
```

```

System.object ConeParams2 {get;}
```

```

property System.Object^ ConeParams2 {
   System.Object^ get();
}
```

#### Property Value

Array of doubles describing the parameters of a conical surface

Remarks

Returns an array of 11 doubles:

- origin.x
- origin.y
- origin.z
- axis.x
- axis.y
- axis.z
- radius
- half angle
- reference\_direction.x
- reference\_direction.y
- reference\_direction.z

Half angle element is in radians. Origin, radius, and reference direction elements are in meters.

Example

[Get Parameters of Conical Surface (VBA)](Get_Parameters_of_Conical_Surface_Example_VB.htm)  
[Get Parameters of Conical Surface (VB.NET)](Get_Parameters_of_Conical_Surface_Example_VBNET.htm)  
[Get Parameters of Conical Surface (C#)](Get_Parameters_of_Conical_Surface_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::IsCone Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsCone.md)
