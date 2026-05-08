# GetCustomInfoType3 Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetCustomInfoType3`

Obsolete. Superseded by IModelDoc2::GetCustomInfoType3.
Obsolete. Superseded by [IModelDoc2::GetCustomInfoType3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetCustomInfoType3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCustomInfoType3( _
   ByVal Configuration As System.String, _
   ByVal FieldName As System.String _
) As System.Integer
```

```

Dim instance As IModelDoc
Dim Configuration As System.String
Dim FieldName As System.String
Dim value As System.Integer
 
value = instance.GetCustomInfoType3(Configuration, FieldName)
```

```

System.int GetCustomInfoType3( 
   System.string Configuration,
   System.string FieldName
)
```

```

System.int GetCustomInfoType3( 
   System.String^ Configuration,
   System.String^ FieldName
) 
```

#### Parameters

*Configuration*

*FieldName*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
