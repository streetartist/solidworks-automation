# swCollisionDetectionResults_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCollisionDetectionResults_e`

Collision detection results.
Collision detection results.

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

<System.Runtime.InteropServices.GuidAttribute("D56C18B0-4F51-4A3A-83C6-1D5DE9F57C35")>
Public Enum swCollisionDetectionResults_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCollisionDetectionResults_e
```

```

[System.Runtime.InteropServices.Guid("D56C18B0-4F51-4A3A-83C6-1D5DE9F57C35")]
public enum swCollisionDetectionResults_e : System.Enum 
```

```

public enum swCollisionDetectionResults_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("D56C18B0-4F51-4A3A-83C6-1D5DE9F57C35")
public enum swCollisionDetectionResults_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("D56C18B0-4F51-4A3A-83C6-1D5DE9F57C35")]
__value public enum swCollisionDetectionResults_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("D56C18B0-4F51-4A3A-83C6-1D5DE9F57C35")]
public enum class swCollisionDetectionResults_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCollisionDetectionResult\_CollisionDetected** | 1 |
| **swCollisionDetectionResult\_FailedNotEnoughGroups** | -1 = You must define more than one collision group containing two or more unsuppressed components in different collision groups |
| **swCollisionDetectionResult\_NoCollision** | 0 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCollisionDetectionResults\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
