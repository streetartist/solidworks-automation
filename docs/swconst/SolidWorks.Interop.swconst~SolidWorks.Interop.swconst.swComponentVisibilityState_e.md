# swComponentVisibilityState_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swComponentVisibilityState_e`

States for component visibility.
States for component visibility.

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

<System.Runtime.InteropServices.GuidAttribute("A274A28B-0B8A-435C-8861-809BB73A8BE3")>
Public Enum swComponentVisibilityState_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swComponentVisibilityState_e
```

```

[System.Runtime.InteropServices.Guid("A274A28B-0B8A-435C-8861-809BB73A8BE3")]
public enum swComponentVisibilityState_e : System.Enum 
```

```

public enum swComponentVisibilityState_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("A274A28B-0B8A-435C-8861-809BB73A8BE3")
public enum swComponentVisibilityState_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("A274A28B-0B8A-435C-8861-809BB73A8BE3")]
__value public enum swComponentVisibilityState_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("A274A28B-0B8A-435C-8861-809BB73A8BE3")]
public enum class swComponentVisibilityState_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swComponentHidden** | 0 = Component is hidden in the assembly |
| **swComponentUnknown** | -1 = Component is unknown |
| **swComponentVisible** | 1 = Component is visible in the assembly |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swComponentVisibilityState\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
