# InsertBendTableNew Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertBendTableNew`

Obsolete. Superseded by IModelDoc2::InsertBendTableNew.
Obsolete. Superseded by [IModelDoc2::InsertBendTableNew](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertBendTableNew.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertBendTableNew( _
   ByVal FileName As System.String, _
   ByVal Units As System.String, _
   ByVal Type As System.String _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim FileName As System.String
Dim Units As System.String
Dim Type As System.String
Dim value As System.Boolean
 
value = instance.InsertBendTableNew(FileName, Units, Type)
```

```

System.bool InsertBendTableNew( 
   System.string FileName,
   System.string Units,
   System.string Type
)
```

```

System.bool InsertBendTableNew( 
   System.String^ FileName,
   System.String^ Units,
   System.String^ Type
) 
```

#### Parameters

*FileName*

*Units*

*Type*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
