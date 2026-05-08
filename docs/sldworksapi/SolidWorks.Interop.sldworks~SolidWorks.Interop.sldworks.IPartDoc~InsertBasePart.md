# InsertBasePart Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertBasePart`

Obsolete. Superseded by IPartDoc::InsertPart.
Obsolete. Superseded by [IPartDoc::InsertPart](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertPart.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertBasePart( _
   ByVal FileName As System.String _
) As System.Boolean
```

```

Dim instance As IPartDoc
Dim FileName As System.String
Dim value As System.Boolean
 
value = instance.InsertBasePart(FileName)
```

```

System.bool InsertBasePart( 
   System.string FileName
)
```

```

System.bool InsertBasePart( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)
