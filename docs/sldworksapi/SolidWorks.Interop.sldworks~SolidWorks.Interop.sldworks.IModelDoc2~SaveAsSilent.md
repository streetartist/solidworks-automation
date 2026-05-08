# SaveAsSilent Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SaveAsSilent`

Obsolete. Superseded by IModelDocExtension::SaveAs.
Obsolete. Superseded by [IModelDocExtension::SaveAs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveAsSilent( _
   ByVal NewName As System.String, _
   ByVal SaveAsCopy As System.Boolean _
) As System.Integer
```

```

Dim instance As IModelDoc2
Dim NewName As System.String
Dim SaveAsCopy As System.Boolean
Dim value As System.Integer
 
value = instance.SaveAsSilent(NewName, SaveAsCopy)
```

```

System.int SaveAsSilent( 
   System.string NewName,
   System.bool SaveAsCopy
)
```

```

System.int SaveAsSilent( 
   System.String^ NewName,
   System.bool SaveAsCopy
) 
```

#### Parameters

*NewName*

*SaveAsCopy*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
