# AddCustomInfo Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddCustomInfo`

Obsolete. Superseded by IModelDocExtension::CustomPropertyManager.
Obsolete. Superseded by [IModelDocExtension::CustomPropertyManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CustomPropertyManager.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddCustomInfo( _
   ByVal FieldName As System.String, _
   ByVal FieldType As System.String, _
   ByVal FieldValue As System.String _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim FieldName As System.String
Dim FieldType As System.String
Dim FieldValue As System.String
Dim value As System.Boolean
 
value = instance.AddCustomInfo(FieldName, FieldType, FieldValue)
```

```

System.bool AddCustomInfo( 
   System.string FieldName,
   System.string FieldType,
   System.string FieldValue
)
```

```

System.bool AddCustomInfo( 
   System.String^ FieldName,
   System.String^ FieldType,
   System.String^ FieldValue
) 
```

#### Parameters

*FieldName*

*FieldType*

*FieldValue*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
