# AddCustomInfo3 Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~AddCustomInfo3`

Obsolete. Superseded by IModelDoc2::AddCustomInfo3.
Obsolete. Superseded by [IModelDoc2::AddCustomInfo3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddCustomInfo3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddCustomInfo3( _
   ByVal Configuration As System.String, _
   ByVal FieldName As System.String, _
   ByVal FieldType As System.Integer, _
   ByVal FieldValue As System.String _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim Configuration As System.String
Dim FieldName As System.String
Dim FieldType As System.Integer
Dim FieldValue As System.String
Dim value As System.Boolean
 
value = instance.AddCustomInfo3(Configuration, FieldName, FieldType, FieldValue)
```

```

System.bool AddCustomInfo3( 
   System.string Configuration,
   System.string FieldName,
   System.int FieldType,
   System.string FieldValue
)
```

```

System.bool AddCustomInfo3( 
   System.String^ Configuration,
   System.String^ FieldName,
   System.int FieldType,
   System.String^ FieldValue
) 
```

#### Parameters

*Configuration*

*FieldName*

*FieldType*

*FieldValue*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
