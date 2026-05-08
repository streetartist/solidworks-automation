# Clone Method (IEnumFaces)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces~Clone`

Obsolete. Superseded by IEnumFaces2::Clone.
Obsolete. Superseded by [IEnumFaces2::Clone](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces2~Clone.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Clone( _
   ByRef Ppenum As EnumFaces _
) 
```

```

Dim instance As IEnumFaces
Dim Ppenum As EnumFaces
 
instance.Clone(Ppenum)
```

```

void Clone( 
   out EnumFaces Ppenum
)
```

```

void Clone( 
   [Out] EnumFaces^ Ppenum
) 
```

#### Parameters

*Ppenum*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumFaces Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces.md)  
[IEnumFaces Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces_members.md)
