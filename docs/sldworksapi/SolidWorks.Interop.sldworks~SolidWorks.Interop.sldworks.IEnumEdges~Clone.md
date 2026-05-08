# Clone Method (IEnumEdges)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumEdges~Clone`

Clones the edges enumeration.
Clones the edges enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Clone( _
   ByRef Ppenum As EnumEdges _
) 
```

```

Dim instance As IEnumEdges
Dim Ppenum As EnumEdges
 
instance.Clone(Ppenum)
```

```

void Clone( 
   out EnumEdges Ppenum
)
```

```

void Clone( 
   [Out] EnumEdges^ Ppenum
) 
```

#### Parameters

*Ppenum*
:   Pointer to the clones [edges enumeration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumEdges.md)

Remarks

For use in in-process DLLs only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumEdges Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumEdges.md)  
[IEnumEdges Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumEdges_members.md)
