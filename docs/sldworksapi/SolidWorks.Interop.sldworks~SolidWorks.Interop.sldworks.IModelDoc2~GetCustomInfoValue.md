# GetCustomInfoValue Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetCustomInfoValue`

Obsolete. Superseded by IModelDocExtension::CustomPropertyManager.
Obsolete. Superseded by [IModelDocExtension::CustomPropertyManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CustomPropertyManager.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCustomInfoValue( _
   ByVal Configuration As System.String, _
   ByVal FieldName As System.String _
) As System.String
```

```

Dim instance As IModelDoc2
Dim Configuration As System.String
Dim FieldName As System.String
Dim value As System.String
 
value = instance.GetCustomInfoValue(Configuration, FieldName)
```

```

System.string GetCustomInfoValue( 
   System.string Configuration,
   System.string FieldName
)
```

```

System.String^ GetCustomInfoValue( 
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

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
