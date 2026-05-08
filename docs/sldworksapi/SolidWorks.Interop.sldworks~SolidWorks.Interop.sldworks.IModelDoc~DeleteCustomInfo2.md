# DeleteCustomInfo2 Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~DeleteCustomInfo2`

Obsolete. Superseded by IModelDoc2::DeleteCustomInfo2.
Obsolete. Superseded by [IModelDoc2::DeleteCustomInfo2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteCustomInfo2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteCustomInfo2( _
   ByVal Configuration As System.String, _
   ByVal FieldName As System.String _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim Configuration As System.String
Dim FieldName As System.String
Dim value As System.Boolean
 
value = instance.DeleteCustomInfo2(Configuration, FieldName)
```

```

System.bool DeleteCustomInfo2( 
   System.string Configuration,
   System.string FieldName
)
```

```

System.bool DeleteCustomInfo2( 
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
