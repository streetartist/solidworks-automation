# IInsertNote Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IInsertNote`

Obsolete. Superseded by IModelDoc2::IInsertNote.
Obsolete. Superseded by [IModelDoc2::IInsertNote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IInsertNote.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IInsertNote( _
   ByVal Text As System.String _
) As Note
```

```

Dim instance As IModelDoc
Dim Text As System.String
Dim value As Note
 
value = instance.IInsertNote(Text)
```

```

Note IInsertNote( 
   System.string Text
)
```

```

Note^ IInsertNote( 
   System.String^ Text
) 
```

#### Parameters

*Text*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
