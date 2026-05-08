# swHealActionType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swHealActionType_e`

Healing actions.
Healing actions.

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

<System.Runtime.InteropServices.GuidAttribute("7E6F559E-FED3-4898-9A80-1F0B21B0BA38")>
Public Enum swHealActionType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swHealActionType_e
```

```

[System.Runtime.InteropServices.Guid("7E6F559E-FED3-4898-9A80-1F0B21B0BA38")]
public enum swHealActionType_e : System.Enum 
```

```

public enum swHealActionType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("7E6F559E-FED3-4898-9A80-1F0B21B0BA38")
public enum swHealActionType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("7E6F559E-FED3-4898-9A80-1F0B21B0BA38")]
__value public enum swHealActionType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("7E6F559E-FED3-4898-9A80-1F0B21B0BA38")]
public enum class swHealActionType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swHealAction\_Cap** | 2 = Finds a surface where all edges of the wound lie and attaches this to a face and covers the wound; SOLIDWORKS creates a new face to cover the wound |
| **swHealAction\_GrowParent** | 1 = Extends the parent faces around the wound to cover it |
| **swHealAction\_Shrink** | 0 = If extending faces does not yield a solution, then SOLIDWORKS tries to shrink the faces |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swHealActionType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
