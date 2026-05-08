# Query Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~Query`

Gets or sets whether the options passed during a document's open, load, and save can be retrieved by this API.
Gets or sets whether the options passed during a document's open, load, and save can be retrieved by this API.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Query As System.Boolean
```

```

Dim instance As IDocumentSpecification
Dim value As System.Boolean
 
instance.Query = value
 
value = instance.Query
```

```

System.bool Query {get; set;}
```

```

property System.bool Query {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to retrieve options, false to not (default)

Remarks

Various options can be passed to document operation APIs such as [IModelDoc2::Save3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Save3.md), [IModelDocExtension::SaveAs4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SaveAs4.md), and [ISldWorks::LoadFile4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4.md). These options can be retrieved from the document, if Query is set to true. Only silent information can be retrieved.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.md)  
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.md)
