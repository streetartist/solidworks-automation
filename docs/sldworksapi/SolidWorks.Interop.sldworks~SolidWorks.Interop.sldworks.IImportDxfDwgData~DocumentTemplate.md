# DocumentTemplate Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~DocumentTemplate`

Gets or sets the filename of the document template.
Gets or sets the filename of the document template.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DocumentTemplate As System.String
```

```

Dim instance As IImportDxfDwgData
Dim value As System.String
 
instance.DocumentTemplate = value
 
value = instance.DocumentTemplate
```

```

System.string DocumentTemplate {get; set;}
```

```

property System.String^ DocumentTemplate {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Filename of document template

Remarks

This method only supports importing to a drawing; it does not support importing to a part sketch.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.md)  
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.md)
