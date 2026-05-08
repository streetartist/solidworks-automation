# ExportToExcel Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~ExportToExcel`

Exports the pattern table to the specified Microsoft Excel file for this variable pattern feature.
Exports the pattern table to the specified Microsoft Excel file for this variable pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ExportToExcel( _
   ByVal ExcelFile As System.String, _
   ByVal Overwrite As System.Boolean _
) As System.Integer
```

```

Dim instance As IDimPatternFeatureData
Dim ExcelFile As System.String
Dim Overwrite As System.Boolean
Dim value As System.Integer
 
value = instance.ExportToExcel(ExcelFile, Overwrite)
```

```

System.int ExportToExcel( 
   System.string ExcelFile,
   System.bool Overwrite
)
```

```

System.int ExportToExcel( 
   System.String^ ExcelFile,
   System.bool Overwrite
) 
```

#### Parameters

*ExcelFile*
:   Path and Microsoft Excel file name to which to export the pattern table; valid filename extensions are **.xls**, **.xlsx**, and **.xlsm**

*Overwrite*
:   True to overwrite a file in the specified path with the same file name, false to not

#### Return Value

Status of exporting the pattern table to a Microsoft Excel file as defined in [swPatternFeatureImportExportError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternFeatureImportExportError_e.html)

Example

[Insert Variable Pattern Feature (C#)](Insert_Advanced_Variable_Pattern_Feature_Example_CSharp.htm)  
[Insert Variable Pattern Feature (VB.NET)](Insert_Advanced_Variable_Pattern_Feature_Example_VBNET.htm)  
[Insert Variable Pattern Feature (VBA)](Insert_Advanced_Variable_Pattern_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.md)  
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.md)  
[IDimPatternFeatureData::ImportFromExcel Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~ImportFromExcel.md)
