# SetSheets Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~SetSheets`

Sets the drawing sheets to export.
Sets the drawing [sheets](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md) to export.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetSheets( _
   ByVal Which As System.Integer, _
   ByVal Sheets As System.Object _
) As System.Boolean
```

```

Dim instance As IExportPdfData
Dim Which As System.Integer
Dim Sheets As System.Object
Dim value As System.Boolean
 
value = instance.SetSheets(Which, Sheets)
```

```

System.bool SetSheets( 
   System.int Which,
   System.object Sheets
)
```

```

System.bool SetSheets( 
   System.int Which,
   System.Object^ Sheets
) 
```

#### Parameters

*Which*
:   Drawing sheets to export to PDF as defined in [swExportDataSheetsToExport\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swExportDataSheetsToExport_e.html)

*Sheets*
:   Array of the names of the drawing sheets to export

#### Return Value

True if the drawings sheets are set to export to PDF, false if not

Example

[Save File as PDF (VBA)](Save_File_as_PDF_Example_VB.htm)  
[Save File as PDF (C#)](Save_File_as_PDF_Example_CSharp.htm)  
[Save File as PDF (VB.NET)](Save_File_as_PDF_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExportPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData.md)  
[IExportPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData_members.md)  
[IExportPdfData::GetSheets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~GetSheets.md)  
[IExportPdfData::GetWhichSheets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~GetWhichSheets.md)
