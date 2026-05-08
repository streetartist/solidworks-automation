# GetExportFileData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetExportFileData`

Gets the data interface for the specified file type to which to export one or more drawing sheets.
Gets the data interface for the specified file type to which to export one or more drawing sheets.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetExportFileData( _
   ByVal FileType As System.Integer _
) As System.Object
```

```

Dim instance As ISldWorks
Dim FileType As System.Integer
Dim value As System.Object
 
value = instance.GetExportFileData(FileType)
```

```

System.object GetExportFileData( 
   System.int FileType
)
```

```

System.Object^ GetExportFileData( 
   System.int FileType
) 
```

#### Parameters

*FileType*
:   File type as defined in [swExportDataFileType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swExportDataFileType_e.html)

#### Return Value

[Data interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData.md) for the specified file type to which to export one or more drawing sheets

Example

[Save File As PDF (VBA)](Save_File_as_PDF_Example_VB.htm)  
[Save File as PDF (C#)](Save_File_as_PDF_Example_CSharp.htm)  
[Save File as PDF (VB.NET)](Save_File_as_PDF_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
