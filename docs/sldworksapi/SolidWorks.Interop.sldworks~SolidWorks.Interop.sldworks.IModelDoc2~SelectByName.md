# SelectByName Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectByName`

Obsolete. Superseded by IModelDocExtension::SelectByID2.
Obsolete. Superseded by [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md).

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

Dim instance As IModelDoc2
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

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
