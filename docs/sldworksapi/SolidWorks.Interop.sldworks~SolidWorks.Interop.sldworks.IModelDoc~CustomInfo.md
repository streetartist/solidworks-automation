# CustomInfo Property (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CustomInfo`

Obsolete. Superseded by IModelDoc2::CustomInfo.
Obsolete. Superseded by [IModelDoc2::CustomInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CustomInfo.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CustomInfo( _
   ByVal FieldName As System.String _
) As System.String
```

```

Dim instance As IModelDoc
Dim FieldName As System.String
Dim value As System.String
 
instance.CustomInfo(FieldName) = value
 
value = instance.CustomInfo(FieldName)
```

```

System.string CustomInfo( 
   System.string FieldName
) {get; set;}
```

```

property System.String^ CustomInfo {
   System.String^ get(System.String^ FieldName);
   void set (System.String^ FieldName, System.String^ value);
}
```

#### Parameters

*FieldName*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
