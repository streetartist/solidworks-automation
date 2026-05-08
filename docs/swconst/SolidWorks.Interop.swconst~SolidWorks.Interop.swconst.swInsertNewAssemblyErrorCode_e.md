# swInsertNewAssemblyErrorCode_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInsertNewAssemblyErrorCode_e`

Error codes when assembly inserted.
Error codes when assembly inserted.

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

<System.Runtime.InteropServices.GuidAttribute("B30B7FC8-9029-4819-B6EF-BFAC86E95D2F")>
Public Enum swInsertNewAssemblyErrorCode_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swInsertNewAssemblyErrorCode_e
```

```

[System.Runtime.InteropServices.Guid("B30B7FC8-9029-4819-B6EF-BFAC86E95D2F")]
public enum swInsertNewAssemblyErrorCode_e : System.Enum 
```

```

public enum swInsertNewAssemblyErrorCode_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("B30B7FC8-9029-4819-B6EF-BFAC86E95D2F")
public enum swInsertNewAssemblyErrorCode_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("B30B7FC8-9029-4819-B6EF-BFAC86E95D2F")]
__value public enum swInsertNewAssemblyErrorCode_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("B30B7FC8-9029-4819-B6EF-BFAC86E95D2F")]
public enum class swInsertNewAssemblyErrorCode_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swInsertNewAssemblyError\_ErrorUknown** | 0 |
| **swInsertNewAssemblyError\_ExtensionNotSldAsm** | 5 |
| **swInsertNewAssemblyError\_FileAlreadyExists** | 3 |
| **swInsertNewAssemblyError\_FilePathEmpty** | 2 |
| **swInsertNewAssemblyError\_FolderDoesNotExist** | 4 |
| **swInsertNewAssemblyError\_NoError** | 1 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swInsertNewAssemblyErrorCode\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
