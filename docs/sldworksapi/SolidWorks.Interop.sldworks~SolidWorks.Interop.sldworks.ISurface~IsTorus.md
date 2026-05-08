# IsTorus Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsTorus`

Gets whether the surface is a torus.
Gets whether the surface is a torus.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsTorus() As System.Boolean
```

```

Dim instance As ISurface
Dim value As System.Boolean
 
value = instance.IsTorus()
```

```

System.bool IsTorus()
```

```

System.bool IsTorus(); 
```

#### Return Value

True if the surface is a torus, false if not

Example

[Get Parameters of Toroidal Surface (VBA)](Get_Parameters_of_Toroidal_Surface_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[IModeler::ICreateToroidalSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateToroidalSurface.md)  
[IModeler::CreateToroidalSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateToroidalSurface.md)  
[ISurface::ITorusParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ITorusParams.md)  
[ISurface::TorusParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~TorusParams.md)
