# ReplaceReference Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ReplaceReference`

Obsolete. Superseded by AssemblyDoc::ReplaceComponents.
Obsolete. Superseded by [AssemblyDoc::ReplaceComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReplaceComponents.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ReplaceReference( _
   ByVal FileName As System.String _
) As System.Integer
```

```

Dim instance As IComponent2
Dim FileName As System.String
Dim value As System.Integer
 
value = instance.ReplaceReference(FileName)
```

```

System.int ReplaceReference( 
   System.string FileName
)
```

```

System.int ReplaceReference( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)
