# swSensorType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSensorType_e`

Types of sensor.
Types of sensor.

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

<System.Runtime.InteropServices.GuidAttribute("B2377107-E6D6-4FAB-9B50-78DE07C8AE8E")>
Public Enum swSensorType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swSensorType_e
```

```

[System.Runtime.InteropServices.Guid("B2377107-E6D6-4FAB-9B50-78DE07C8AE8E")]
public enum swSensorType_e : System.Enum 
```

```

public enum swSensorType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("B2377107-E6D6-4FAB-9B50-78DE07C8AE8E")
public enum swSensorType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("B2377107-E6D6-4FAB-9B50-78DE07C8AE8E")]
__value public enum swSensorType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("B2377107-E6D6-4FAB-9B50-78DE07C8AE8E")]
public enum class swSensorType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSensorDimension** | 2 = Measurement (dimension) sensor |
| **swSensorInterfaceDetection** | 3 = Interference detection sensor; Obsolete |
| **swSensorMassProperty** | 1 = Obsolete |
| **swSensorProximity** | 5 = Obsolete |
| **swSensorSimulation** | 0 = Obsolete |

Remarks

As of SOLIDWORKS 2009 SP02, only sensors of type swSensorDimension are supported. Non-dimension measurement sensors (=4) and all of the other sensor types are no longer supported.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swSensorType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
