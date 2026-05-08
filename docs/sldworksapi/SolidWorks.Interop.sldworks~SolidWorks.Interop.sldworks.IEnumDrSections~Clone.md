# Clone Method (IEnumDrSections)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDrSections~Clone`

Clones the section views enumeration.
Clones the section views enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Clone( _
   ByRef Ppenum As EnumDrSections _
) 
```

```

Dim instance As IEnumDrSections
Dim Ppenum As EnumDrSections
 
instance.Clone(Ppenum)
```

```

void Clone( 
   out EnumDrSections Ppenum
)
```

```

void Clone( 
   [Out] EnumDrSections^ Ppenum
) 
```

#### Parameters

*Ppenum*
:   Pointer to the cloned [section views enumeration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDrSections.md)

Remarks

For use in in-process DLLs only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumDrSections Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDrSections.md)  
[IEnumDrSections Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDrSections_members.md)
