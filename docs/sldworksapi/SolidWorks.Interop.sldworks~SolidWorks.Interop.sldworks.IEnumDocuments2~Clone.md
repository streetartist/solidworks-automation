# Clone Method (IEnumDocuments2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments2~Clone`

Clones the documents enumeration.
Clones the documents enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Clone( _
   ByRef Ppenum As EnumDocuments2 _
) 
```

```

Dim instance As IEnumDocuments2
Dim Ppenum As EnumDocuments2
 
instance.Clone(Ppenum)
```

```

void Clone( 
   out EnumDocuments2 Ppenum
)
```

```

void Clone( 
   [Out] EnumDocuments2^ Ppenum
) 
```

#### Parameters

*Ppenum*
:   Pointer to the cloned [documents enumeration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments2.md)

Remarks

For use in in-process DLLs only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumDocuments2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments2.md)  
[IEnumDocuments2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments2_members.md)
