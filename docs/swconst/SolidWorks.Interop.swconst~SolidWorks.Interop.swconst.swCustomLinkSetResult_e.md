# swCustomLinkSetResult_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCustomLinkSetResult_e`

Error codes when linking and unlinking custom properties.
Error codes when linking and unlinking custom properties.

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

<System.Runtime.InteropServices.GuidAttribute("CAF24A33-EB6A-49FA-9068-C048C8125A28")>
Public Enum swCustomLinkSetResult_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCustomLinkSetResult_e
```

```

[System.Runtime.InteropServices.Guid("CAF24A33-EB6A-49FA-9068-C048C8125A28")]
public enum swCustomLinkSetResult_e : System.Enum 
```

```

public enum swCustomLinkSetResult_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("CAF24A33-EB6A-49FA-9068-C048C8125A28")
public enum swCustomLinkSetResult_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("CAF24A33-EB6A-49FA-9068-C048C8125A28")]
__value public enum swCustomLinkSetResult_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("CAF24A33-EB6A-49FA-9068-C048C8125A28")]
public enum class swCustomLinkSetResult_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCustomLinkSetResult\_Legacy** | 2 = Legacy custom properties cannot be linked or unlinked |
| **swCustomLinkSetResult\_NotPresent** | 1 = Custom property does not exist |
| **swCustomLinkSetResult\_OK** | 0 = Success |
| **swCustomLinkSetResult\_UserProp** | 3 = User-defined custom properties cannot be linked or unlinked |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCustomLinkSetResult\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
