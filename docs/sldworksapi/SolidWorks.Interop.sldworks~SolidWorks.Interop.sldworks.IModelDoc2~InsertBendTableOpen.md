# InsertBendTableOpen Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertBendTableOpen`

Inserts an existing bend table from a file into this model document.
Inserts an existing bend table from a file into this model document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertBendTableOpen( _
   ByVal FileName As System.String _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim FileName As System.String
Dim value As System.Boolean
 
value = instance.InsertBendTableOpen(FileName)
```

```

System.bool InsertBendTableOpen( 
   System.string FileName
)
```

```

System.bool InsertBendTableOpen( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   File name of the bend table to insert into this model document

#### Return Value

True if the table is successfully inserted, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::InsertBendTableEdit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertBendTableEdit.md)  
[IModelDoc2::InsertBendTableNew Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertBendTableNew.md)  
[IModelDoc2::DeleteBendTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteBendTable.md)
