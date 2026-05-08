# Clone Method (IEnumDisplayDimensions)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDisplayDimensions~Clone`

Clones the display dimensions enumeration.
Clones the display dimensions enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Clone( _
   ByRef Ppenum As EnumDisplayDimensions _
) 
```

```

Dim instance As IEnumDisplayDimensions
Dim Ppenum As EnumDisplayDimensions
 
instance.Clone(Ppenum)
```

```

void Clone( 
   out EnumDisplayDimensions Ppenum
)
```

```

void Clone( 
   [Out] EnumDisplayDimensions^ Ppenum
) 
```

#### Parameters

*Ppenum*
:   Pointer to the cloned [display dimensions enumeration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDisplayDimensions.md)

Remarks

For use in in-process DLLs only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumDisplayDimensions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDisplayDimensions.md)  
[IEnumDisplayDimensions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDisplayDimensions_members.md)
