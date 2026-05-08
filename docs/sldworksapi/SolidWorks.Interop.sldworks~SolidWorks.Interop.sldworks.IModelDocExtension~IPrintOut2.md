# IPrintOut2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IPrintOut2`

Obsolete. Superseded by IModelDocExtension::IPrintOut3.
Obsolete. Superseded by [IModelDocExtension::IPrintOut3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IPrintOut3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IPrintOut2( _
   ByVal ArraySize As System.Integer, _
   ByRef PageArray As System.Integer, _
   ByVal Copies As System.Integer, _
   ByVal Collate As System.Boolean, _
   ByVal Printer As System.String, _
   ByVal PrintFileName As System.String _
) 
```

```

Dim instance As IModelDocExtension
Dim ArraySize As System.Integer
Dim PageArray As System.Integer
Dim Copies As System.Integer
Dim Collate As System.Boolean
Dim Printer As System.String
Dim PrintFileName As System.String
 
instance.IPrintOut2(ArraySize, PageArray, Copies, Collate, Printer, PrintFileName)
```

```

void IPrintOut2( 
   System.int ArraySize,
   ref System.int PageArray,
   System.int Copies,
   System.bool Collate,
   System.string Printer,
   System.string PrintFileName
)
```

```

void IPrintOut2( 
   System.int ArraySize,
   System.int% PageArray,
   System.int Copies,
   System.bool Collate,
   System.String^ Printer,
   System.String^ PrintFileName
) 
```

#### Parameters

*ArraySize*
:   Number of pages to print (see **Remarks**)

*PageArray*
:   - in-process, unmanaged C++: Pointer to an array of range of pages to print (see **Remarks**)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

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

PageArray and ArraySize

For a part or assembly, the ArraySize and PageArray arguments are ignored.  No dialogs or message boxes are displayed.

PageArray contains any number of pairs of values, each pair indicating the start page and end page of a range of pages to print. For example, to print sheets 1, 2, 3, 6, and 7 of a drawing, the array should contain 4 elements; 1, 3, 6, 7. This means to print pages 1-3 and 6-7.  A range can be 5, 5, which means to print just page 5. If the array contains only one value, only that page is printed. If that one element is 0, then all sheets are printed.

If ArraySize = 0 or PageArray argument is NULL, the all sheets are printed.

PrintFileName

To print to a file instead to a printer, set PrintFileName to a non-empty name.

If the PrintFileName is empty, then the document is printed to the printer specified in Printer.  If that string is empty, then the document is printed to the default printer for this document. Use [IModelDoc2::Printer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Printer.md) to get or set this value.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDoc2::PrintDirect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PrintDirect.md)  
[IModelDoc2::ClosePrintPreview Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClosePrintPreview.md)  
[IModelDoc2::PrintPreview Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PrintPreview.md)  
[IModelDocExtension::PrintOut2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PrintOut2.md)
