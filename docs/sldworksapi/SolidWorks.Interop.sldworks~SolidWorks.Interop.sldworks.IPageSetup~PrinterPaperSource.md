# PrinterPaperSource Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperSource`

Gets or sets the printer paper source for this document or sheet.
Gets or sets the printer paper source for this document or sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PrinterPaperSource As System.Integer
```

```

Dim instance As IPageSetup
Dim value As System.Integer
 
instance.PrinterPaperSource = value
 
value = instance.PrinterPaperSource
```

```

System.int PrinterPaperSource {get; set;}
```

```

property System.int PrinterPaperSource {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Printer paper source (see **Remarks**)

Remarks

The property value is one of a set of standard constants defined by the operating system or by a specific printer device; there is no SOLIDWORKS enumeration for these values. See your operating system's and programming language's Help for the details on printers and paper sizes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.md)  
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.md)  
[IPageSetup::PrinterPaperLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperLength.md)  
[IPageSetup::PrinterPaperSize Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperSize.md)  
[IPageSetup::PrinterPaperWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperWidth.md)
