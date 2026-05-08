# Clone Method (IEnumLoops2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops2~Clone`

Clones the loops enumeration.
Clones the loops enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Clone( _
   ByRef Ppenum As EnumLoops2 _
) 
```

```

Dim instance As IEnumLoops2
Dim Ppenum As EnumLoops2
 
instance.Clone(Ppenum)
```

```

void Clone( 
   out EnumLoops2 Ppenum
)
```

```

void Clone( 
   [Out] EnumLoops2^ Ppenum
) 
```

#### Parameters

*Ppenum*
:   Pointer to the clones [loops enumeration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops2.md)

Remarks

For use in in-process DLLs only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumLoops2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops2.md)  
[IEnumLoops2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops2_members.md)
