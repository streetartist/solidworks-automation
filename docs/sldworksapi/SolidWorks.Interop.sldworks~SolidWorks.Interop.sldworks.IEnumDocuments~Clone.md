# Clone Method (IEnumDocuments)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments~Clone`

Obsolete. Superseded by IEnumDocuments2::Clone.
Obsolete. Superseded by [IEnumDocuments2::Clone](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments2~Clone.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Clone( _
   ByRef Ppenum As EnumDocuments _
) 
```

```

Dim instance As IEnumDocuments
Dim Ppenum As EnumDocuments
 
instance.Clone(Ppenum)
```

```

void Clone( 
   out EnumDocuments Ppenum
)
```

```

void Clone( 
   [Out] EnumDocuments^ Ppenum
) 
```

#### Parameters

*Ppenum*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumDocuments Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments.md)  
[IEnumDocuments Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments_members.md)
