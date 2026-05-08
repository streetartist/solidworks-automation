# SelectByName Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SelectByName`

Obsolete. Superseded by IModelDoc2::SelectByName.
Obsolete. Superseded by [IModelDoc2::SelectByName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectByName.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SelectByName( _
   ByVal Flags As System.Integer, _
   ByVal IdStr As System.String _
) 
```

```

Dim instance As IModelDoc
Dim Flags As System.Integer
Dim IdStr As System.String
 
instance.SelectByName(Flags, IdStr)
```

```

void SelectByName( 
   System.int Flags,
   System.string IdStr
)
```

```

void SelectByName( 
   System.int Flags,
   System.String^ IdStr
) 
```

#### Parameters

*Flags*

*IdStr*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
