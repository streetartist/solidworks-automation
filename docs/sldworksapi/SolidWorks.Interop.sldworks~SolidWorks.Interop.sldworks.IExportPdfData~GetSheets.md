# GetSheets Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~GetSheets`

Gets the drawing sheets to export.
Gets the drawing [sheets](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md) to export.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSheets() As System.Object
```

```

Dim instance As IExportPdfData
Dim value As System.Object
 
value = instance.GetSheets()
```

```

System.object GetSheets()
```

```

System.Object^ GetSheets(); 
```

#### Return Value

Array of the names of the sheets to export

Remarks

Call [IModelDocExtension::SaveAs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs.md) after calling this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExportPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData.md)  
[IExportPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData_members.md)  
[IExportPdfData::GetWhichSheets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~GetWhichSheets.md)  
[IExportPdfData::SetSheets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~SetSheets.md)
