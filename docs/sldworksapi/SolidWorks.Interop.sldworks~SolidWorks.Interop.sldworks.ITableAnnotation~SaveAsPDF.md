# SaveAsPDF Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SaveAsPDF`

Saves this table to a PDF file.
Saves this table to a PDF file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveAsPDF( _
   ByVal FileName As System.String _
) As System.Boolean
```

```

Dim instance As ITableAnnotation
Dim FileName As System.String
Dim value As System.Boolean
 
value = instance.SaveAsPDF(FileName)
```

```

System.bool SaveAsPDF( 
   System.string FileName
)
```

```

System.bool SaveAsPDF( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Full path and filename of the PDF File (see **Remarks**)

#### Return Value

True if the table is saved to a PDF file, false if not

Remarks

You must specify a filename. It should include the path, filename, and the PDF filename extension to which to save the table.

|  |  |
| --- | --- |
| **If a file of the specified name in the specified path...** | **Then it is...** |
| Exists | Overwritten |
| Does not exist | Created |

Example

[Save Table to PDF (C#)](Save_Table_Annotation_to_PDF_Example_CSharp.htm)  
[Save Table to PDF (VB.NET)](Save_Table_Annotation_to_PDF_Example_VBNET.htm)  
[Save Table to PDF (VBA)](Save_Table_Annotation_to_PDF_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::SaveAsTemplate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SaveAsTemplate.md)  
[ITableAnnotation::SaveAsText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SaveAsText.md)
