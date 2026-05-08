# ImportFromExcel Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~ImportFromExcel`

Imports a table from the specified Microsoft Excel file for this variable pattern feature.
Imports a table from the specified Microsoft Excel file for this variable pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ImportFromExcel( _
   ByVal ExcelFile As System.String _
) As System.Integer
```

```

Dim instance As IDimPatternFeatureData
Dim ExcelFile As System.String
Dim value As System.Integer
 
value = instance.ImportFromExcel(ExcelFile)
```

```

System.int ImportFromExcel( 
   System.string ExcelFile
)
```

```

System.int ImportFromExcel( 
   System.String^ ExcelFile
) 
```

#### Parameters

*ExcelFile*
:   Path and Microsoft Excel file name from which to import a table; valid filename extensions are **.xls**, **.xlsx**, and **.xlsm**

#### Return Value

Status of importing a table from a Microsoft Excel file as defined in [swPatternFeatureImportExportError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternFeatureImportExportError_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.md)  
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.md)  
[IDimPatternFeatureData::ExportToExcel Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~ExportToExcel.md)
