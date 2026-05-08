# ViewPdfAfterSaving Property (IExportPdfData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~ViewPdfAfterSaving`

Gets or sets whether to view the PDF file to which a part or drawing is saved.
Gets or sets whether to view the PDF file to which a part or drawing is saved.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ViewPdfAfterSaving As System.Boolean
```

```

Dim instance As IExportPdfData
Dim value As System.Boolean
 
instance.ViewPdfAfterSaving = value
 
value = instance.ViewPdfAfterSaving
```

```

System.bool ViewPdfAfterSaving {get; set;}
```

```

property System.bool ViewPdfAfterSaving {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to view the PDF file, false to not

Example

See [IExportPdfData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExportPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData.md)  
[IExportPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData_members.md)
