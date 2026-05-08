# swMoveCopyError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMoveCopyError_e`

Move/copy errors.
Move/copy errors.

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

<System.Runtime.InteropServices.GuidAttribute("A01B62E1-9F8F-4725-8B71-1AA4E70038FF")>
Public Enum swMoveCopyError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swMoveCopyError_e
```

```

[System.Runtime.InteropServices.Guid("A01B62E1-9F8F-4725-8B71-1AA4E70038FF")]
public enum swMoveCopyError_e : System.Enum 
```

```

public enum swMoveCopyError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("A01B62E1-9F8F-4725-8B71-1AA4E70038FF")
public enum swMoveCopyError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("A01B62E1-9F8F-4725-8B71-1AA4E70038FF")]
__value public enum swMoveCopyError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("A01B62E1-9F8F-4725-8B71-1AA4E70038FF")]
public enum class swMoveCopyError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swMoveCopyErrorFail** | 2 = Failed to create destination directories or copy operation failed possibly because you do not have proper permissions |
| **swMoveCopyErrorNone** | 0 = Successful |
| **swMoveCopyErrorSourceDoesNotExist** | 1 = Source file does not exist |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swMoveCopyError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
