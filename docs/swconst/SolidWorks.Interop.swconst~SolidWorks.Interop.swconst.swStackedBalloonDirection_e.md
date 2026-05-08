# swStackedBalloonDirection_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStackedBalloonDirection_e`

Balloon stacking directions.
Balloon stacking directions.

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

<System.Runtime.InteropServices.GuidAttribute("92B8B974-27F0-49C1-83B9-B32B31C197DF")>
Public Enum swStackedBalloonDirection_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swStackedBalloonDirection_e
```

```

[System.Runtime.InteropServices.Guid("92B8B974-27F0-49C1-83B9-B32B31C197DF")]
public enum swStackedBalloonDirection_e : System.Enum 
```

```

public enum swStackedBalloonDirection_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("92B8B974-27F0-49C1-83B9-B32B31C197DF")
public enum swStackedBalloonDirection_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("92B8B974-27F0-49C1-83B9-B32B31C197DF")]
__value public enum swStackedBalloonDirection_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("92B8B974-27F0-49C1-83B9-B32B31C197DF")]
public enum class swStackedBalloonDirection_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swStackedBalloonDir\_Down** | 2 = Balloons stack downwards from the master balloon in the stack |
| **swStackedBalloonDir\_Left** | 3 = Balloons stack to the left from the master balloon in the stack |
| **swStackedBalloonDir\_None** | 0 = Stacking direction does not apply |
| **swStackedBalloonDir\_Right** | 4 = Balloons stack to the right from the master balloon in the stack |
| **swStackedBalloonDir\_Up** | 1 = Balloons stack upwards from the master balloon in the stack |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swStackedBalloonDirection\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
