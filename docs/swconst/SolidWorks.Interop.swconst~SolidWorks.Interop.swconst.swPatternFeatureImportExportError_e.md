# swPatternFeatureImportExportError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternFeatureImportExportError_e`

Variable pattern feature errors when importing or exporting Microsoft Excel data.
Variable pattern feature errors when importing or exporting Microsoft Excel data.

Syntax

- [Visual Basic](#Syntax-VBAll)
- [C#](#Syntax-CS)
- [Delphi](#Syntax-Delphi)
- [JScript](#Syntax-JScript)
- [Managed Extensions for C++](#Syntax-CPP)
- [C++/CLI](#Syntax-CPP2005)

```

'Declaration
 
```

```

<System.Runtime.InteropServices.GuidAttribute("4FFCEF1C-5603-4153-B6B0-C54BD1E4BA62")>
Public Enum swPatternFeatureImportExportError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swPatternFeatureImportExportError_e
```

```

[System.Runtime.InteropServices.Guid("4FFCEF1C-5603-4153-B6B0-C54BD1E4BA62")]
public enum swPatternFeatureImportExportError_e : System.Enum 
```

```

public enum swPatternFeatureImportExportError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("4FFCEF1C-5603-4153-B6B0-C54BD1E4BA62")
public enum swPatternFeatureImportExportError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("4FFCEF1C-5603-4153-B6B0-C54BD1E4BA62")]
__value public enum swPatternFeatureImportExportError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("4FFCEF1C-5603-4153-B6B0-C54BD1E4BA62")]
public enum class swPatternFeatureImportExportError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swPatternFeatureImportExportError\_AccessDeniedOrInvalidPath** | 19 = Access denied or invalid path |
| **swPatternFeatureImportExportError\_ColumnARows1And2Error** | 5 = Column A, Rows 1 and 2 must be merged and named Instance |
| **swPatternFeatureImportExportError\_ColumnBRows1And2Error** | 7 = Column B, Rows 1 and 2 must be merged and named Instances to Skip |
| **swPatternFeatureImportExportError\_DimensionNameDoesNotExist** | 12 = Dimension name does not exist in the parent feature |
| **swPatternFeatureImportExportError\_DimValueFormatIncorrect** | 15 = Dimension is incorrectly formatted |
| **swPatternFeatureImportExportError\_DuplicateDimensions** | 10 = Duplicate dimensions are not allowed in the import file |
| **swPatternFeatureImportExportError\_EmptyRowsOrColumns** | 4 = Empty rows or columns are not allowed |
| **swPatternFeatureImportExportError\_Failed** | 1 = Failed |
| **swPatternFeatureImportExportError\_FailedToRetrieveExcelApp** | 20 = Failed to find Microsoft Excel application |
| **swPatternFeatureImportExportError\_FailedToRetrieveModelDocument** | 16 = Failed to retrieve model document |
| **swPatternFeatureImportExportError\_FeatureDoesNotExist** | 9 = Feature does not exist in the selected features or references to pattern |
| **swPatternFeatureImportExportError\_FeatureOrDimDoesNotExist** | 13 = Feature does not exist in the selected features or references to pattern, or the dimension name does not exist in the parent feature |
| **swPatternFeatureImportExportError\_FileExistsAndOverwriteIsFalse** | 17 = Microsoft Excel file exists, but the file cannot be overwritten |
| **swPatternFeatureImportExportError\_ImproperValuesForColumnB** | 8 = Invalid value; valid values are 0 (not skipped) or 1 (skipped) |
| **swPatternFeatureImportExportError\_InstNumStartsFromNonZero** | 6 = Instances in the Microsoft Excel table must start at 0 |
| **swPatternFeatureImportExportError\_NoValidDimensionToImport** | 14 = No valid dimensions to import from this Microsoft Excel file |
| **swPatternFeatureImportExportError\_OutOfRangeDimensionValue** | 11 = Dimension in this cell in is not in the range of dimensions |
| **swPatternFeatureImportExportError\_ReadOnlyFile** | 18 = Microsoft Excel file is read only |
| **swPatternFeatureImportExportError\_Succeed** | 0 = Succeeded |
| **swPatternFeatureImportExportError\_UnequalNumOfCellsInColumn** | 2 = All columns containing dimensions in this imported table must have the same number of cells; these columns cannot be empty or merged |
| **swPatternFeatureImportExportError\_UnequalNumOfCellsInRow** | 3 = All rows containing dimensions in this imported table must have the same number of cells; these rows cannot be empty or merged |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swPatternFeatureImportExportError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
