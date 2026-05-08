# swSensorAlertType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSensorAlertType_e`

Types of sensor alert.
Types of sensor alert.

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

<System.Runtime.InteropServices.GuidAttribute("FB300942-139E-4AA2-8C2E-C7CED2FFBF54")>
Public Enum swSensorAlertType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swSensorAlertType_e
```

```

[System.Runtime.InteropServices.Guid("FB300942-139E-4AA2-8C2E-C7CED2FFBF54")]
public enum swSensorAlertType_e : System.Enum 
```

```

public enum swSensorAlertType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("FB300942-139E-4AA2-8C2E-C7CED2FFBF54")
public enum swSensorAlertType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("FB300942-139E-4AA2-8C2E-C7CED2FFBF54")]
__value public enum swSensorAlertType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("FB300942-139E-4AA2-8C2E-C7CED2FFBF54")]
public enum class swSensorAlertType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSensorAlert\_Between** | 6 |
| **swSensorAlert\_Exactly** | 2 |
| **swSensorAlert\_False** | 9 |
| **swSensorAlert\_GreaterThan** | 0 |
| **swSensorAlert\_LessThan** | 1 |
| **swSensorAlert\_NotBetween** | 7 |
| **swSensorAlert\_NotExactly** | 5 |
| **swSensorAlert\_NotGreaterThan** | 3 |
| **swSensorAlert\_NotLessThan** | 4 |
| **swSensorAlert\_True** | 8 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swSensorAlertType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
