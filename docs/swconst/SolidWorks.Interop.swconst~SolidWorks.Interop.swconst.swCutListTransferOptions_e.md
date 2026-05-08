# swCutListTransferOptions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCutListTransferOptions_e`

Options for transferring the cut list when saving a weldment member, surface body, or solid body to another part.
Options for transferring the cut list when saving a weldment member, surface body, or solid body to another part.

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

<System.Runtime.InteropServices.GuidAttribute("2F9231E7-7614-44D7-899A-67FA8A90BF4D")>
Public Enum swCutListTransferOptions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCutListTransferOptions_e
```

```

[System.Runtime.InteropServices.Guid("2F9231E7-7614-44D7-899A-67FA8A90BF4D")]
public enum swCutListTransferOptions_e : System.Enum 
```

```

public enum swCutListTransferOptions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("2F9231E7-7614-44D7-899A-67FA8A90BF4D")
public enum swCutListTransferOptions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("2F9231E7-7614-44D7-899A-67FA8A90BF4D")]
__value public enum swCutListTransferOptions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("2F9231E7-7614-44D7-899A-67FA8A90BF4D")]
public enum class swCutListTransferOptions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCutListTransferOptions\_CutListProperties** | 2 = Transfer to a cut list in the new part |
| **swCutListTransferOptions\_FileProperties** | 1 = Transfer to file properties of the new part |
| **swCutListTransferOptions\_None** | 0 = No transfer |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCutListTransferOptions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
