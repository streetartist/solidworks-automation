# GetShellType Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetShellType`

Gets the shell type for this face.
Gets the shell type for this face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetShellType() As System.Integer
```

```

Dim instance As IFace2
Dim value As System.Integer
 
value = instance.GetShellType()
```

```

System.int GetShellType()
```

```

System.int GetShellType(); 
```

#### Return Value

Shell type:

- 0 = Open shell. For example, a face that belongs to a sheet (surface) body or reference surface.
- 1 = Internal shell. For example, a face that belongs to a cavity. Face helps define an internal volume.
- 2 = External shell. For example, a typical face on a solid body (helps "hold in" the body mass). This includes all external faces (faces belonging to bosses, pockets, holes, and so on).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)
