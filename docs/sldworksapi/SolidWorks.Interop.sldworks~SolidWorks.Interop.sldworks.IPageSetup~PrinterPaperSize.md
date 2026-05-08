# PrinterPaperSize Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperSize`

Gets or sets the printer paper size for this document or sheet.
Gets or sets the printer paper size for this document or sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PrinterPaperSize As System.Integer
```

```

Dim instance As IPageSetup
Dim value As System.Integer
 
instance.PrinterPaperSize = value
 
value = instance.PrinterPaperSize
```

```

System.int PrinterPaperSize {get; set;}
```

```

property System.int PrinterPaperSize {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Paper size (see **Remarks**)

Remarks

This property is one of a set of standard constants defined by the operating system or by a specific printer device; there is no SOLIDWORKS enumeration for these values. See your operating system's and programming language's Help for the details on printers and paper sizes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.md)  
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.md)  
[IPageSetup::PrinterPaperLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperLength.md)  
[IPageSetup::PrinterPaperSource Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperSource.md)  
[IPageSetup::PrinterPaperWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperWidth.md)
