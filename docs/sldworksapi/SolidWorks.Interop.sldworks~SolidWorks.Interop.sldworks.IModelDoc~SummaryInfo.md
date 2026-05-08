# SummaryInfo Property (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SummaryInfo`

Obsolete. Superseded by IModelDoc2::SummaryInfo.
Obsolete. Superseded by [IModelDoc2::SummaryInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SummaryInfo.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SummaryInfo( _
   ByVal FieldId As System.Integer _
) As System.String
```

```

Dim instance As IModelDoc
Dim FieldId As System.Integer
Dim value As System.String
 
instance.SummaryInfo(FieldId) = value
 
value = instance.SummaryInfo(FieldId)
```

```

System.string SummaryInfo( 
   System.int FieldId
) {get; set;}
```

```

property System.String^ SummaryInfo {
   System.String^ get(System.int FieldId);
   void set (System.int FieldId, System.String^ value);
}
```

#### Parameters

*FieldId*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
