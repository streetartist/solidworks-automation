# swCloseReopenError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCloseReopenError_e`

Close and reopen errors.
Close and reopen errors.

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

<System.Runtime.InteropServices.GuidAttribute("0D640A0C-CFB6-4B77-9EAC-37248CEE399C")>
Public Enum swCloseReopenError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCloseReopenError_e
```

```

[System.Runtime.InteropServices.Guid("0D640A0C-CFB6-4B77-9EAC-37248CEE399C")]
public enum swCloseReopenError_e : System.Enum 
```

```

public enum swCloseReopenError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("0D640A0C-CFB6-4B77-9EAC-37248CEE399C")
public enum swCloseReopenError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("0D640A0C-CFB6-4B77-9EAC-37248CEE399C")]
__value public enum swCloseReopenError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("0D640A0C-CFB6-4B77-9EAC-37248CEE399C")]
public enum class swCloseReopenError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCloseReopenCloseDocError** | 5; error occurred during close |
| **swCloseReopenInvalidDocError** | 4; document is not a drawing |
| **swCloseReopenLoadFileNotFoundError** | 7; file path specified for document to reopen does not exist |
| **swCloseReopenLoadFilePathEmptyError** | 13; file path of document to reopen is empty |
| **swCloseReopenLoadFilePathNonDrawingError** | 14; file to reopen is not a drawing |
| **swCloseReopenLoadFutureVersionError** | 9; file to reopen is a future version |
| **swCloseReopenLoadGenericError** | 6; error occurred during reopen |
| **swCloseReopenLoadInvalidFileTypeError** | 8; file type is not valid |
| **swCloseReopenLoadLiquidMachineDocError** | 11; LiquidMachine document error |
| **swCloseReopenLoadSameTitleAlreadyOpenError** | 10; file with the same title is already open |
| **swCloseReopenModifiedError** | 12; unable to close the document because changes were made to the document, and [swCloseReopenOption\_e.swCloseReopenOption\_DiscardChanges](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCloseReopenOption_e.md) was not set |
| **swCloseReopenNoError** | 0; no error |
| **swCloseReopenNoInputDocError** | 2; input document is null |
| **swCloseReopenOutputDocPointerError** | 3; output document is null |
| **swCloseReopenUnknownError** | 1; unknown error |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCloseReopenError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
