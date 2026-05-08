# PrintOut4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PrintOut4`

Prints this document without displaying any dialogs or message boxes.
Prints this document without displaying any dialogs or message boxes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub PrintOut4( _
   ByVal Printer As System.String, _
   ByVal PrintFileName As System.String, _
   ByVal PrintSpecification As System.Object _
) 
```

```

Dim instance As IModelDocExtension
Dim Printer As System.String
Dim PrintFileName As System.String
Dim PrintSpecification As System.Object
 
instance.PrintOut4(Printer, PrintFileName, PrintSpecification)
```

```

void PrintOut4( 
   System.string Printer,
   System.string PrintFileName,
   System.object PrintSpecification
)
```

```

void PrintOut4( 
   System.String^ Printer,
   System.String^ PrintFileName,
   System.Object^ PrintSpecification
) 
```

#### Parameters

*Printer*
:   Name of the printer to which to print (see **Remarks**)

*PrintFileName*
:   Name of file to which to print (see **Remarks**)

*PrintSpecification*
:   [IPrintSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.md) (see **Remarks**)

Remarks

This method supports printing parts, assemblies, and both single and multisheet drawings.

Before calling this method:

1. Call [IModelDocExtension::GetPrintSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPrintSpecification.md) to get the IPrintSpecification object for this document.
2. Set [IPrintSpecification::PrintToFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~PrintToFile.md) to:  
   - true to print to PrintFileName.
   - false to print to Printer.
3. Set other properties on the IPrintSpecification object.
4. Use the IPrintSpecification object to specify PrintSpecification.

If Printer, PrintFileName, and PrintSpecification are not specified, then this method prints to the default printer specified by [IModelDoc2::Printer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Printer.md).

Example

[Print Drawing (VBA)](Print_Drawing_as_High_Quality_Example_VB.htm)  
[Print Drawing (VB.NET)](Print_Drawing_as_High_Quality_Example_VBNET.htm)  
[Print Drawing (C#)](Print_Drawing_as_High_Quality_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDoc2::PrintDirect Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PrintDirect.md)  
[IModelDoc2::PrintPreview Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PrintPreview.md)  
[IModelDoc2::ClosePrintPreview Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClosePrintPreview.md)  
[IModelDocExtension::SaveAs Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs.md)
