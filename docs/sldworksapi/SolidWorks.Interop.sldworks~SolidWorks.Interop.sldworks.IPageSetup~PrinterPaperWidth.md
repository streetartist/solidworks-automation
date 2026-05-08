# PrinterPaperWidth Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperWidth`

Gets or sets the user-defined printer paper width for this document or sheet.
Gets or sets the user-defined printer paper width for this document or sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PrinterPaperWidth As System.Integer
```

```

Dim instance As IPageSetup
Dim value As System.Integer
 
instance.PrinterPaperWidth = value
 
value = instance.PrinterPaperWidth
```

```

System.int PrinterPaperWidth {get; set;}
```

```

property System.int PrinterPaperWidth {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Paper width (see **Remarks**)

Remarks

Use [IPageSetup::PrinterPaperSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperSize.md) to set the printer paper size. A value for IPageSetup::PrinterPaperSize is a user-defined paper size. In that case, this property indicates the width of that user-defined paper.

Width is in 0.1mm units. To define a paper that is 200mm wide, Width is 2000.

To get or set the printer paper length, use [IPageSetup:;PrinterPaperLength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperLength.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.md)  
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.md)  
[IPageSetup::PrinterPaperSource Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperSource.md)
