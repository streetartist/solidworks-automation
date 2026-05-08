# SaveAs2 Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SaveAs2`

Obsolete. Superseded by IModelDoc2::SaveAs2.
Obsolete. Superseded by [IModelDoc2::SaveAs2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SaveAs2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveAs2( _
   ByVal NewName As System.String, _
   ByVal SaveAsVersion As System.Integer, _
   ByVal SaveAsCopy As System.Boolean, _
   ByVal Silent As System.Boolean _
) As System.Integer
```

```

Dim instance As IModelDoc
Dim NewName As System.String
Dim SaveAsVersion As System.Integer
Dim SaveAsCopy As System.Boolean
Dim Silent As System.Boolean
Dim value As System.Integer
 
value = instance.SaveAs2(NewName, SaveAsVersion, SaveAsCopy, Silent)
```

```

System.int SaveAs2( 
   System.string NewName,
   System.int SaveAsVersion,
   System.bool SaveAsCopy,
   System.bool Silent
)
```

```

System.int SaveAs2( 
   System.String^ NewName,
   System.int SaveAsVersion,
   System.bool SaveAsCopy,
   System.bool Silent
) 
```

#### Parameters

*NewName*

*SaveAsVersion*

*SaveAsCopy*

*Silent*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
