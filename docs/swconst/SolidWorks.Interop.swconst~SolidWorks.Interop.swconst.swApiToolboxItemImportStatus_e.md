# swApiToolboxItemImportStatus_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swApiToolboxItemImportStatus_e`

Return codes for toolbox item import.
Return codes for toolbox item import.

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

<System.Runtime.InteropServices.GuidAttribute("1FA231E8-A1EA-42F9-9E5C-A42A9ED2A267")>
Public Enum swApiToolboxItemImportStatus_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swApiToolboxItemImportStatus_e
```

```

[System.Runtime.InteropServices.Guid("1FA231E8-A1EA-42F9-9E5C-A42A9ED2A267")]
public enum swApiToolboxItemImportStatus_e : System.Enum 
```

```

public enum swApiToolboxItemImportStatus_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("1FA231E8-A1EA-42F9-9E5C-A42A9ED2A267")
public enum swApiToolboxItemImportStatus_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("1FA231E8-A1EA-42F9-9E5C-A42A9ED2A267")]
__value public enum swApiToolboxItemImportStatus_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("1FA231E8-A1EA-42F9-9E5C-A42A9ED2A267")]
public enum class swApiToolboxItemImportStatus_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swApiToolboxItemImportStatus\_ExcelCouldNotOpenFile** | 6 |
| **swApiToolboxItemImportStatus\_ExcelImportDidNotFindColumn** | 4 |
| **swApiToolboxItemImportStatus\_ExcelImportWrongFile** | 5 |
| **swApiToolboxItemImportStatus\_FailedToSaveFile** | 3 |
| **swApiToolboxItemImportStatus\_FailedUnspecifiedError** | 8 |
| **swApiToolboxItemImportStatus\_InvalidArgument** | 1 |
| **swApiToolboxItemImportStatus\_InvalidPartNumber** | 7 |
| **swApiToolboxItemImportStatus\_MicrosoftExcelNotInstalled** | 2 |
| **swApiToolboxItemImportStatus\_Success** | 0 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swApiToolboxItemImportStatus\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
