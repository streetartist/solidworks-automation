# swCollisionGroupSetComponentsErrors_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCollisionGroupSetComponentsErrors_e`

Errors when setting components in collision groups.
Errors when setting components in collision groups.

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

<System.Runtime.InteropServices.GuidAttribute("811BA52D-8A8A-4D77-83D6-46D9A741D974")>
Public Enum swCollisionGroupSetComponentsErrors_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCollisionGroupSetComponentsErrors_e
```

```

[System.Runtime.InteropServices.Guid("811BA52D-8A8A-4D77-83D6-46D9A741D974")]
public enum swCollisionGroupSetComponentsErrors_e : System.Enum 
```

```

public enum swCollisionGroupSetComponentsErrors_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("811BA52D-8A8A-4D77-83D6-46D9A741D974")
public enum swCollisionGroupSetComponentsErrors_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("811BA52D-8A8A-4D77-83D6-46D9A741D974")]
__value public enum swCollisionGroupSetComponentsErrors_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("811BA52D-8A8A-4D77-83D6-46D9A741D974")]
public enum class swCollisionGroupSetComponentsErrors_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCollisionGroupSetComponentsErrors\_ComponentsAddedElsewhere** | 2 = One or more components have already been added to a different collision group |
| **swCollisionGroupSetComponentsErrors\_GroupRemoved** | 3 = The specified collision group is no longer available |
| **swCollisionGroupSetComponentsErrors\_InvalidComponents** | 1 = Components from a different assembly cannot be included in this collision detection |
| **swCollisionGroupSetComponentsErrors\_None** | 0 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCollisionGroupSetComponentsErrors\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
