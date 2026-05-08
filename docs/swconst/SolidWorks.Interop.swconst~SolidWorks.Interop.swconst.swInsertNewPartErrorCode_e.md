# swInsertNewPartErrorCode_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInsertNewPartErrorCode_e`

Error codes when part inserted.
Error codes when part inserted.

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

<System.Runtime.InteropServices.GuidAttribute("3B832244-512B-4207-895C-983CBA6D37EC")>
Public Enum swInsertNewPartErrorCode_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swInsertNewPartErrorCode_e
```

```

[System.Runtime.InteropServices.Guid("3B832244-512B-4207-895C-983CBA6D37EC")]
public enum swInsertNewPartErrorCode_e : System.Enum 
```

```

public enum swInsertNewPartErrorCode_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("3B832244-512B-4207-895C-983CBA6D37EC")
public enum swInsertNewPartErrorCode_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("3B832244-512B-4207-895C-983CBA6D37EC")]
__value public enum swInsertNewPartErrorCode_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("3B832244-512B-4207-895C-983CBA6D37EC")]
public enum class swInsertNewPartErrorCode_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swInsertNewPartError\_CannotSelectFaceOrPlane** | 7 |
| **swInsertNewPartError\_ErrorUknown** | 0 |
| **swInsertNewPartError\_ExtensionNotSldPrt** | 5 |
| **swInsertNewPartError\_FileAlreadyExists** | 3 |
| **swInsertNewPartError\_FilePathEmpty** | 2 |
| **swInsertNewPartError\_FolderDoesNotExist** | 4 |
| **swInsertNewPartError\_NoError** | 1 |
| **swInsertNewPartError\_NotAFaceOrPlane** | 6 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swInsertNewPartErrorCode\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
