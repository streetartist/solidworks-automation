# SaveAs3 Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SaveAs3`

Obsolete. Superseded by IModelDoc2::SaveAs3.
Obsolete. Superseded by [IModelDoc2::SaveAs3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SaveAs3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveAs3( _
   ByVal NewName As System.String, _
   ByVal SaveAsVersion As System.Integer, _
   ByVal Options As System.Integer _
) As System.Integer
```

```

Dim instance As IModelDoc
Dim NewName As System.String
Dim SaveAsVersion As System.Integer
Dim Options As System.Integer
Dim value As System.Integer
 
value = instance.SaveAs3(NewName, SaveAsVersion, Options)
```

```

System.int SaveAs3( 
   System.string NewName,
   System.int SaveAsVersion,
   System.int Options
)
```

```

System.int SaveAs3( 
   System.String^ NewName,
   System.int SaveAsVersion,
   System.int Options
) 
```

#### Parameters

*NewName*

*SaveAsVersion*

*Options*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
