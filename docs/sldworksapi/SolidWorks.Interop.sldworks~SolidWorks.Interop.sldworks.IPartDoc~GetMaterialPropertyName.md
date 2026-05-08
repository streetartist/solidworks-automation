# GetMaterialPropertyName Method (IPartDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetMaterialPropertyName`

Obsolete. Superseded by IPartDoc::GetMaterialPropertyName2.
Obsolete. Superseded by [IPartDoc::GetMaterialPropertyName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetMaterialPropertyName2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMaterialPropertyName( _
   ByRef Database As System.String _
) As System.String
```

```

Dim instance As IPartDoc
Dim Database As System.String
Dim value As System.String
 
value = instance.GetMaterialPropertyName(Database)
```

```

System.string GetMaterialPropertyName( 
   out System.string Database
)
```

```

System.String^ GetMaterialPropertyName( 
   [Out] System.String^ Database
) 
```

#### Parameters

*Database*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)
