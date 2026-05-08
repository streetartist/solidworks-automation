# IExportPdfData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData`

Allows access to the PDF export data interface, which allows you to save:
Allows access to the PDF export data interface, which allows you to save:

- one or more drawing sheets to PDF.
- parts and assemblies to 3D PDF.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IExportPdfData 
```

```

Dim instance As IExportPdfData
```

```

public interface IExportPdfData 
```

```

public interface class IExportPdfData 
```

Remarks

**To export one or more drawing sheets to PDF:**

1. Get the IExportPdfData object using [ISldWorks::GetExportFileData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetExportFileData.md).
2. Set the sheets to export to PDF using [IExportPdfData::SetSheets](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~SetSheets.md).
3. Set whether to view the PDF after saving using [IExportPdfData::ViewPdfAfterSaving](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~ViewPdfAfterSaving.md).
4. Save the sheets using [IModelDocExtension::SaveAs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs.md).

**To export a part or assembly to 3D PDF:**

1. Get the IExportPdfData object using [ISldWorks::GetExportFileData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetExportFileData.md).
2. Set [IExportPdfData::ExportAs3D](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~ExportAs3D.md) to true.
3. Set whether to view the PDF after saving using [IExportPdfData::ViewPdfAfterSaving](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~ViewPdfAfterSaving.md).
4. Save the part or assembly using [IModelDocExtension::SaveAs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs.md).

Example

[Save File as PDF (VBA)](Save_File_as_PDF_Example_VB.htm)  
[Save File as PDF (C#)](Save_File_as_PDF_Example_CSharp.htm)  
[Save File as PDF (VB.NET)](Save_File_as_PDF_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExportPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
