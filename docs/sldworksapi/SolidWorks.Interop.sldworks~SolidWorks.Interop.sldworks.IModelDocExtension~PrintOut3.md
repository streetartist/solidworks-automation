# PrintOut3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PrintOut3`

Obsolete. Superseded by IModelDocExtension::PrintOut4.
Obsolete. Superseded by [IModelDocExtension::PrintOut4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PrintOut4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub PrintOut3( _
   ByVal PageArray As System.Object, _
   ByVal Copies As System.Integer, _
   ByVal Collate As System.Boolean, _
   ByVal Printer As System.String, _
   ByVal PrintFileName As System.String, _
   ByVal ConvertToHighQuality As System.Boolean _
) 
```

```

Dim instance As IModelDocExtension
Dim PageArray As System.Object
Dim Copies As System.Integer
Dim Collate As System.Boolean
Dim Printer As System.String
Dim PrintFileName As System.String
Dim ConvertToHighQuality As System.Boolean
 
instance.PrintOut3(PageArray, Copies, Collate, Printer, PrintFileName, ConvertToHighQuality)
```

```

void PrintOut3( 
   System.object PageArray,
   System.int Copies,
   System.bool Collate,
   System.string Printer,
   System.string PrintFileName,
   System.bool ConvertToHighQuality
)
```

```

void PrintOut3( 
   System.Object^ PageArray,
   System.int Copies,
   System.bool Collate,
   System.String^ Printer,
   System.String^ PrintFileName,
   System.bool ConvertToHighQuality
) 
```

#### Parameters

*PageArray*
:   :   Range of pages to print (see **Remarks)**

*Copies*
:   Number of copies to print

*Collate*
:   True to collate copies, false to not

*Printer*
:   Name of the printer queue (see **Remarks** )

*PrintFileName*
:   Name of file to print to instead of Printer

*ConvertToHighQuality*
:   True to convert to high quality, false to leave as draft quality

Remarks

This method supports printing parts, assemblies, and both single and multisheet drawings.

PageArray

For a part or assembly, the PageArray argument is ignored. No dialogs or message boxes are displayed.

PageArray contains any number of pairs of values, each pair indicating the start page and end page of a range of pages to print. For example, to print sheets 1, 2, 3, 6, and 7 of a drawing, the array should contain 4 elements; 1, 3, 6, 7. This means to print pages 1-3 and 6-7.  A range can be 5, 5, which means to print just page 5. If the array contains only one value, only that page is printed. If that one element is 0, then all sheets are printed.

If PageArray is an empty array, then all sheets are printed. Also, the array can contain just one value, rather than an array, in which case only that page is printed.

PrintFileName

To print to a file instead to a printer, set PrintFileName to a non-empty name.

If the PrintFileName is empty, then the document is printed to the printer specified in Printer. If that string is empty, then the document is printed to the default printer for this document. Use [IModelDoc2::Printer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Printer.md) to get or set this value.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::IPrintOut3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IPrintOut3.md)  
[IModelDoc2::PrintDirect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PrintDirect.md)  
[IModelDoc2::PrintPreview Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PrintPreview.md)  
[IModelDoc2::ClosePrintPreview Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClosePrintPreview.md)  
[IModelDocExtension::SaveAs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs.md)
