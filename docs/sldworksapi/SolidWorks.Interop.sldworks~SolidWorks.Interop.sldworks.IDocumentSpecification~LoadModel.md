# LoadModel Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~LoadModel`

Gets or sets whether to load the model if the document is a detached drawing.
Gets or sets whether to load the model if the document is a detached drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LoadModel As System.Boolean
```

```

Dim instance As IDocumentSpecification
Dim value As System.Boolean
 
instance.LoadModel = value
 
value = instance.LoadModel
```

```

System.bool LoadModel {get; set;}
```

```

property System.bool LoadModel {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to load the model, false to not

Remarks

To avoid a warning when opening shaded modes in views, set this property to TRUE so that the view is automatically loaded in shaded.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.md)  
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.md)
