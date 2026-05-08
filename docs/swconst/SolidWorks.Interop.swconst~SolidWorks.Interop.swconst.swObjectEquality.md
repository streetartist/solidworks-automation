# swObjectEquality Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swObjectEquality`

Object equality states.
Object equality states.

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

<System.Runtime.InteropServices.GuidAttribute("2E9AA9B9-A044-4156-9565-1FD8AF4F8288")>
Public Enum swObjectEquality 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swObjectEquality
```

```

[System.Runtime.InteropServices.Guid("2E9AA9B9-A044-4156-9565-1FD8AF4F8288")]
public enum swObjectEquality : System.Enum 
```

```

public enum swObjectEquality = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("2E9AA9B9-A044-4156-9565-1FD8AF4F8288")
public enum swObjectEquality extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("2E9AA9B9-A044-4156-9565-1FD8AF4F8288")]
__value public enum swObjectEquality : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("2E9AA9B9-A044-4156-9565-1FD8AF4F8288")]
public enum class swObjectEquality : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swObjectNotSame** | 0 = Specified objects are not the same object |
| **swObjectSame** | 1 = Specified objects are the same object |
| **swObjectUnsupported** | 2 = Unable to determine if the specified objects are the same object |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swObjectEquality**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
