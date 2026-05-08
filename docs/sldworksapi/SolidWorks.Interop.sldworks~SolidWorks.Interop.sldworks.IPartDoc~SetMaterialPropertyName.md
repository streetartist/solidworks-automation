# SetMaterialPropertyName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetMaterialPropertyName`

Obsolete. Superseded by IPartDoc::SetMaterialPropertyName2.
Obsolete. Superseded by [IPartDoc::SetMaterialPropertyName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetMaterialPropertyName2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetMaterialPropertyName( _
   ByVal Database As System.String, _
   ByVal Name As System.String _
) 
```

```

Dim instance As IPartDoc
Dim Database As System.String
Dim Name As System.String
 
instance.SetMaterialPropertyName(Database, Name)
```

```

void SetMaterialPropertyName( 
   System.string Database,
   System.string Name
)
```

```

void SetMaterialPropertyName( 
   System.String^ Database,
   System.String^ Name
) 
```

#### Parameters

*Database*

*Name*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)
