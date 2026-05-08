# swComponentSuppressionState_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swComponentSuppressionState_e`

States for component suppression.
States for component suppression.

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

<System.Runtime.InteropServices.GuidAttribute("C7044F4E-27E1-4095-B6A5-35682477B8C8")>
Public Enum swComponentSuppressionState_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swComponentSuppressionState_e
```

```

[System.Runtime.InteropServices.Guid("C7044F4E-27E1-4095-B6A5-35682477B8C8")]
public enum swComponentSuppressionState_e : System.Enum 
```

```

public enum swComponentSuppressionState_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("C7044F4E-27E1-4095-B6A5-35682477B8C8")
public enum swComponentSuppressionState_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("C7044F4E-27E1-4095-B6A5-35682477B8C8")]
__value public enum swComponentSuppressionState_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("C7044F4E-27E1-4095-B6A5-35682477B8C8")]
public enum class swComponentSuppressionState_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swComponentFullyLightweight** | 4 = Fully lightweight - recursively makes the component and any child components lightweight |
| **swComponentFullyResolved** | 2 = Fully resolved - recursively resolves the component and any child components |
| **swComponentInternalIdMismatch** | 5 |
| **swComponentLightweight** | 1 = Lightweight - makes only the component lightweight |
| **swComponentResolved** | 3 = Resolved - resolves only the component |
| **swComponentSuppressed** | 0 = Fully suppressed - recursively suppresses the component and any child components |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swComponentSuppressionState\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
