# swRebuildOnActivation_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRebuildOnActivation_e`

Rebuild options during document activation.
Rebuild options during document activation.

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

<System.Runtime.InteropServices.GuidAttribute("2D8787D0-3B21-4417-967F-DA00D3CD03A5")>
Public Enum swRebuildOnActivation_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swRebuildOnActivation_e
```

```

[System.Runtime.InteropServices.Guid("2D8787D0-3B21-4417-967F-DA00D3CD03A5")]
public enum swRebuildOnActivation_e : System.Enum 
```

```

public enum swRebuildOnActivation_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("2D8787D0-3B21-4417-967F-DA00D3CD03A5")
public enum swRebuildOnActivation_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("2D8787D0-3B21-4417-967F-DA00D3CD03A5")]
__value public enum swRebuildOnActivation_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("2D8787D0-3B21-4417-967F-DA00D3CD03A5")]
public enum class swRebuildOnActivation_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swDontRebuildActiveDoc** | 1 = do not rebuild the activated document |
| **swRebuildActiveDoc** | 2 = rebuild the activated document |
| **swUserDecision** | 0 = prompt the user whether to rebuild the activated document |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swRebuildOnActivation\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
