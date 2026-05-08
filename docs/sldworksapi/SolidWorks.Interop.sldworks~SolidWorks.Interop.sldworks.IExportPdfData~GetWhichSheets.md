# GetWhichSheets Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~GetWhichSheets`

Gets the drawing sheets to export to PDF.
Gets the drawing [sheets](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md) to export to PDF.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetWhichSheets() As System.Integer
```

```

Dim instance As IExportPdfData
Dim value As System.Integer
 
value = instance.GetWhichSheets()
```

```

System.int GetWhichSheets()
```

```

System.int GetWhichSheets(); 
```

#### Return Value

Drawing sheets to export to PDF as defined in [swExportDataSheetsToExport\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swExportDataSheetsToExport_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExportPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData.md)  
[IExportPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData_members.md)  
[IExportPdfData::GetSheets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~GetSheets.md)  
[IExportPdfData::SetSheets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~SetSheets.md)
