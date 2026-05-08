# PrinterPaperLength Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperLength`

Gets or sets the user-defined printer paper length for this document or sheet.
Gets or sets the user-defined printer paper length for this document or sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PrinterPaperLength As System.Integer
```

```

Dim instance As IPageSetup
Dim value As System.Integer
 
instance.PrinterPaperLength = value
 
value = instance.PrinterPaperLength
```

```

System.int PrinterPaperLength {get; set;}
```

```

property System.int PrinterPaperLength {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Paper length (see **Remarks**)

Remarks

Use [IPageSetup::PrinterPaperSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperSize.md) to set the printer's paper size. A possible value for IPageSetup::PrinterPaperSize is to have a user-defined paper size. In that case, this property indicates the length of that user-defined paper.

Length is in 0.1mm units. To define a paper that is 250mm long, set Length to 2500.

To get or set the printer paper width, use [IPageSetup::PrinterPaperWidth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperWidth.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.md)  
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.md)  
[IPageSetup::PrinterPaperSource Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperSource.md)
