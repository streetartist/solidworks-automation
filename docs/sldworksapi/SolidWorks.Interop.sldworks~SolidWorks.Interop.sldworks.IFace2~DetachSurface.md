# DetachSurface Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~DetachSurface`

Detaches a surface from this face.
Detaches a surface from this face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DetachSurface() As System.Boolean
```

```

Dim instance As IFace2
Dim value As System.Boolean
 
value = instance.DetachSurface()
```

```

System.bool DetachSurface()
```

```

System.bool DetachSurface(); 
```

#### Return Value

True if the surface is detached from this face, false if not

Example

Use[IFace2::AttachSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~AttachSurface.md) to attach surfaces to faces. Neither IFace2::DetachFace nor IFace2::AttachFace affect body topology.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::IGetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetSurface.md)  
[IFace2::GetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetSurface.md)
