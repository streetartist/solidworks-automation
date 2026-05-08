# swEditPartCommandStatus_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEditPartCommandStatus_e`

Return values during the activation of a part.
Return values during the activation of a part.

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

<System.Runtime.InteropServices.GuidAttribute("BD625603-1B46-45AB-82F2-A8261EBC372C")>
Public Enum swEditPartCommandStatus_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swEditPartCommandStatus_e
```

```

[System.Runtime.InteropServices.Guid("BD625603-1B46-45AB-82F2-A8261EBC372C")]
public enum swEditPartCommandStatus_e : System.Enum 
```

```

public enum swEditPartCommandStatus_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("BD625603-1B46-45AB-82F2-A8261EBC372C")
public enum swEditPartCommandStatus_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("BD625603-1B46-45AB-82F2-A8261EBC372C")]
__value public enum swEditPartCommandStatus_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("BD625603-1B46-45AB-82F2-A8261EBC372C")]
public enum class swEditPartCommandStatus_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swEditPartAsmMustBeSaved** | -2 |
| **swEditPartCompMustBeResolved** | -4 |
| **swEditPartCompMustBeSelected** | -3 |
| **swEditPartCompMustHaveWriteAccess** | -5 |
| **swEditPartCompNotPositioned** | 1 or 0x1 |
| **swEditPartFailure** | -1 |
| **swEditPartSuccessful** | 0 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swEditPartCommandStatus\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
