# swSlotMateConstraintOptions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSlotMateConstraintOptions_e`

Slot mate constraint options.
Slot mate constraint options.

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

<System.Runtime.InteropServices.GuidAttribute("2316F9CD-4580-4651-9333-BB705286A39D")>
Public Enum swSlotMateConstraintOptions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swSlotMateConstraintOptions_e
```

```

[System.Runtime.InteropServices.Guid("2316F9CD-4580-4651-9333-BB705286A39D")]
public enum swSlotMateConstraintOptions_e : System.Enum 
```

```

public enum swSlotMateConstraintOptions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("2316F9CD-4580-4651-9333-BB705286A39D")
public enum swSlotMateConstraintOptions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("2316F9CD-4580-4651-9333-BB705286A39D")]
__value public enum swSlotMateConstraintOptions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("2316F9CD-4580-4651-9333-BB705286A39D")]
public enum class swSlotMateConstraintOptions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSlotMateConstraintOption\_Centered** | 1 = Center the component in the slot |
| **swSlotMateConstraintOption\_Distance** | 2 = Place the component axis at a specified distance from the end of the slot |
| **swSlotMateConstraintOption\_Free** | 0 = Allow the component to move freely in the slot |
| **swSlotMateConstraintOption\_Percent** | 3 = Place the component axis at a specified percent of slot length distance from the end of the slot |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swSlotMateConstraintOptions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
