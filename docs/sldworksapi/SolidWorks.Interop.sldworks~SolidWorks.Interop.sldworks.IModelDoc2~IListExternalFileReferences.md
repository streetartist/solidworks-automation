# IListExternalFileReferences Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IListExternalFileReferences`

Obsolete. Superseded by IModelDocExtension::ListExternalReferences.
Obsolete. Superseded by [IModelDocExtension::ListExternalReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ListExternalFileReferences.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IListExternalFileReferences( _
   ByVal UseSearchRules As System.Boolean, _
   ByVal NumRefs As System.Integer _
) As System.String
```

```

Dim instance As IModelDoc2
Dim UseSearchRules As System.Boolean
Dim NumRefs As System.Integer
Dim value As System.String
 
value = instance.IListExternalFileReferences(UseSearchRules, NumRefs)
```

```

System.string IListExternalFileReferences( 
   System.bool UseSearchRules,
   System.int NumRefs
)
```

```

System.String^ IListExternalFileReferences( 
   System.bool UseSearchRules,
   System.int NumRefs
) 
```

#### Parameters

*UseSearchRules*

*NumRefs*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
