# IsCone Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsCone`

Gets whether the surface is a cone.
Gets whether the surface is a cone.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsCone() As System.Boolean
```

```

Dim instance As ISurface
Dim value As System.Boolean
 
value = instance.IsCone()
```

```

System.bool IsCone()
```

```

System.bool IsCone(); 
```

#### Return Value

True if surface is a cone, false if not

Remarks

Closed cone faces that have an apex point do not have an edge or coedge at the apex.

Example

[Locate Apex of Conical Face (VBA)](Locate_Apex_of_Conical_Face_Example_VB.htm)  
[Get Parameters of Conical Surface (VBA)](Get_Parameters_of_Conical_Surface_Example_VB.htm)  
[Get Parameters of Conical Surface (VB.NET)](Get_Parameters_of_Conical_Surface_Example_VBNET.htm)  
[Get Parameters of Conical Surface (C#)](Get_Parameters_of_Conical_Surface_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::IConeParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IConeParams.md)  
[ISurface::ConeParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ConeParams.md)  
[IModeler::CreateConicalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateConicalSurface2.md)  
[IModeler::ICreateConicalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateConicalSurface2.md)
