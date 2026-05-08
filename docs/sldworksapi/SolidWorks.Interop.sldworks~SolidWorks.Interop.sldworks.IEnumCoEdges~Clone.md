# Clone Method (IEnumCoEdges)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumCoEdges~Clone`

Clones the a coedges enumeration.
Clones the a coedges enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Clone( _
   ByRef Ppenum As EnumCoEdges _
) 
```

```

Dim instance As IEnumCoEdges
Dim Ppenum As EnumCoEdges
 
instance.Clone(Ppenum)
```

```

void Clone( 
   out EnumCoEdges Ppenum
)
```

```

void Clone( 
   [Out] EnumCoEdges^ Ppenum
) 
```

#### Parameters

*Ppenum*
:   Pointer to the cloned [coedges enumeration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumCoEdges.md)

Remarks

For use in in-process DLLs only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumCoEdges Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumCoEdges.md)  
[IEnumCoEdges Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumCoEdges_members.md)
