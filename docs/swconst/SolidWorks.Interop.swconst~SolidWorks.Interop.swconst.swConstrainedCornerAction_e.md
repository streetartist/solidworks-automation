# swConstrainedCornerAction_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConstrainedCornerAction_e`

Actions to take if the corner to be filleted is constrained or has a dimension.
Actions to take if the corner to be filleted is constrained or has a dimension.

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

<System.Runtime.InteropServices.GuidAttribute("3A4FDFEC-E351-465D-AD7E-D7966FF148DA")>
Public Enum swConstrainedCornerAction_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swConstrainedCornerAction_e
```

```

[System.Runtime.InteropServices.Guid("3A4FDFEC-E351-465D-AD7E-D7966FF148DA")]
public enum swConstrainedCornerAction_e : System.Enum 
```

```

public enum swConstrainedCornerAction_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("3A4FDFEC-E351-465D-AD7E-D7966FF148DA")
public enum swConstrainedCornerAction_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("3A4FDFEC-E351-465D-AD7E-D7966FF148DA")]
__value public enum swConstrainedCornerAction_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("3A4FDFEC-E351-465D-AD7E-D7966FF148DA")]
public enum class swConstrainedCornerAction_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swConstrainedCornerDeleteGeometry** | 2 = Delete the constraint or dimension and add the fillet |
| **swConstrainedCornerInteract** | 0 = Ask the user whether to delete the geometry or stop processing |
| **swConstrainedCornerKeepGeometry** | 1 = Keep the constraint or dimension by creating a virtual intersection point before adding the fillet |
| **swConstrainedCornerStopProcessing** | 3 = Do not delete the constraint or dimension and do not create the fillet |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swConstrainedCornerAction\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
