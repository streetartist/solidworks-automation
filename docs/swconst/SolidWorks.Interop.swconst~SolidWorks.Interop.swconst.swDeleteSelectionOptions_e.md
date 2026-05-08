# swDeleteSelectionOptions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDeleteSelectionOptions_e`

Options for deleting features. Bitmask.
Options for deleting features. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("8441E184-963E-4C64-B2F4-941BE77C8300")>
Public Enum swDeleteSelectionOptions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swDeleteSelectionOptions_e
```

```

[System.Runtime.InteropServices.Guid("8441E184-963E-4C64-B2F4-941BE77C8300")]
public enum swDeleteSelectionOptions_e : System.Enum 
```

```

public enum swDeleteSelectionOptions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("8441E184-963E-4C64-B2F4-941BE77C8300")
public enum swDeleteSelectionOptions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("8441E184-963E-4C64-B2F4-941BE77C8300")]
__value public enum swDeleteSelectionOptions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("8441E184-963E-4C64-B2F4-941BE77C8300")]
public enum class swDeleteSelectionOptions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swDelete\_Absorbed** | 2 or 0x2 |
| **swDelete\_Advanced** | 4 or 0x4 |
| **swDelete\_Children** | 1 or 0x1 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swDeleteSelectionOptions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
