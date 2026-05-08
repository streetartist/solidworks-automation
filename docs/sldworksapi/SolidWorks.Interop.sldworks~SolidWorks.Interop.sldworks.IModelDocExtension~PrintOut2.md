# PrintOut2 Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PrintOut2`

Obsolete. Superseded by IModelDocExtension::PrintOut3.
Obsolete. Superseded by [IModelDocExtension::PrintOut3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PrintOut3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub PrintOut2( _
   ByVal PageArray As System.Object, _
   ByVal Copies As System.Integer, _
   ByVal Collate As System.Boolean, _
   ByVal Printer As System.String, _
   ByVal PrintFileName As System.String _
) 
```

```

Dim instance As IModelDocExtension
Dim PageArray As System.Object
Dim Copies As System.Integer
Dim Collate As System.Boolean
Dim Printer As System.String
Dim PrintFileName As System.String
 
instance.PrintOut2(PageArray, Copies, Collate, Printer, PrintFileName)
```

```

void PrintOut2( 
   System.object PageArray,
   System.int Copies,
   System.bool Collate,
   System.string Printer,
   System.string PrintFileName
)
```

```

void PrintOut2( 
   System.Object^ PageArray,
   System.int Copies,
   System.bool Collate,
   System.String^ Printer,
   System.String^ PrintFileName
) 
```

#### Parameters

*PageArray*
:   Range of pages to print (see **Remarks**)

*Copies*
:   Number of copies to print

*Collate*
:   True to collate copies, false to not

*Printer*
:   Name of the printer queue (see **Remarks** )

*PrintFileName*
:   Name of file to print to instead of Printer

Remarks

This method supports printing parts, assemblies, and both single and multisheet drawings.

PageArray

For a part or assembly, the PageArray argument is ignored.  No dialogs or message boxes are displayed.

PageArray contains any number of pairs of values, each pair indicating the start page and end page of a range of pages to print. For example, to print sheets 1, 2, 3, 6, and 7 of a drawing, the array should contain 4 elements; 1, 3, 6, 7. This means to print pages 1-3 and 6-7.  A range can be 5, 5, which means to print just page 5. If the array contains only one value, only that page is printed. If that one element is 0, then all sheets are printed.

If PageArray is an empty array, then all sheets are printed. Also, the array can contain just a one value, rather than an array, in which case only that page is printed, just like passing in an array containing only one value.

PrintFileName

To print to a file instead to a printer, set PrintFileName to a non-empty name.

If the PrintFileName is empty, then the document is printed to the printer specified in Printer.  If that string is empty, then the document is printed to the default printer for this document. Use [IModelDoc2::Printer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Printer.md) to get or set this value.

Example

[Print Drawing and Save As PDF (VBA)](Print_Drawing_and_Save_as_PDF_Example_VB.htm)  
[Print Drawing Document to File (VBA)](Print_Drawing_Document_to_File_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDoc2::PrintDirect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PrintDirect.md)  
[IModelDoc2::PrintPreview Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PrintPreview.md)  
[IModelDoc2::ClosePrintPreview Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClosePrintPreview.md)  
[IModelDocExtension::IPrintOut2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IPrintOut2.md)
