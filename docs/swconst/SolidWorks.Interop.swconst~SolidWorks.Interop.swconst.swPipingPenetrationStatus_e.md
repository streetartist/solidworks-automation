# swPipingPenetrationStatus_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPipingPenetrationStatus_e`

Piping pentration status.
Piping pentration status.

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

<System.Runtime.InteropServices.GuidAttribute("52A7F449-36B4-4558-8C12-9C4411A90D5B")>
Public Enum swPipingPenetrationStatus_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swPipingPenetrationStatus_e
```

```

[System.Runtime.InteropServices.Guid("52A7F449-36B4-4558-8C12-9C4411A90D5B")]
public enum swPipingPenetrationStatus_e : System.Enum 
```

```

public enum swPipingPenetrationStatus_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("52A7F449-36B4-4558-8C12-9C4411A90D5B")
public enum swPipingPenetrationStatus_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("52A7F449-36B4-4558-8C12-9C4411A90D5B")]
__value public enum swPipingPenetrationStatus_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("52A7F449-36B4-4558-8C12-9C4411A90D5B")]
public enum class swPipingPenetrationStatus_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swPenetrationFailed** | 1 = Unspecified error |
| **swPenetrationFailedAlreadyPenetrating** | 8 = Pipe is already penetrating |
| **swPenetrationFailedBadFitting** | 7 = Pipe cannot be found or fitting to pierce cannot be found |
| **swPenetrationFailedBadSelection** | 6 = Sketch point cannot be used for penetration |
| **swPenetrationFailedDllNotLoaded** | 3 = Routing not installed |
| **swPenetrationFailedMultiBody** | 9 = Pipe cannot pentrate multibody |
| **swPenetrationFailedNoSelection** | 4 = No sketch point selected |
| **swPenetrationFailedNotRouting** | 5 = Sketch is not a routing sketch |
| **swPenetrationFailedPipeTooWide** | 2 = Pipe too wide to cut other pipe |
| **swPenetrationSucceeded** | 0 = Okay |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swPipingPenetrationStatus\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
