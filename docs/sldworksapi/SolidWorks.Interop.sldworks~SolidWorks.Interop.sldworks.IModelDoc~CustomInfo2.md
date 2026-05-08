# CustomInfo2 Property (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CustomInfo2`

Obsolete. Superseded by IModelDoc2::CustomInfo2.
Obsolete. Superseded by [IModelDoc2::CustomInfo2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CustomInfo2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CustomInfo2( _
   ByVal Configuration As System.String, _
   ByVal FieldName As System.String _
) As System.String
```

```

Dim instance As IModelDoc
Dim Configuration As System.String
Dim FieldName As System.String
Dim value As System.String
 
instance.CustomInfo2(Configuration, FieldName) = value
 
value = instance.CustomInfo2(Configuration, FieldName)
```

```

System.string CustomInfo2( 
   System.string Configuration,
   System.string FieldName
) {get; set;}
```

```

property System.String^ CustomInfo2 {
   System.String^ get(System.String^ Configuration, System.String^ FieldName);
   void set (System.String^ Configuration, System.String^ FieldName, System.String^ value);
}
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
