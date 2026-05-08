# swArcEndCondition_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swArcEndCondition_e`

Arc endpoint conditions for linear dimensions.
Arc endpoint conditions for linear dimensions.

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

<System.Runtime.InteropServices.GuidAttribute("B7D8DDC4-5070-4A2E-A420-CF955A985C9C")>
Public Enum swArcEndCondition_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swArcEndCondition_e
```

```

[System.Runtime.InteropServices.Guid("B7D8DDC4-5070-4A2E-A420-CF955A985C9C")]
public enum swArcEndCondition_e : System.Enum 
```

```

public enum swArcEndCondition_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("B7D8DDC4-5070-4A2E-A420-CF955A985C9C")
public enum swArcEndCondition_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("B7D8DDC4-5070-4A2E-A420-CF955A985C9C")]
__value public enum swArcEndCondition_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("B7D8DDC4-5070-4A2E-A420-CF955A985C9C")]
public enum class swArcEndCondition_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swArcEndConditionCenter** | 1 = End point is the center of the arc |
| **swArcEndConditionMax** | 3 = End point is the furthest point on the arc |
| **swArcEndConditionMin** | 2 = End point is the nearest point on the arc |
| **swArcEndConditionNone** | 0 = End point is not related to an arc |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swArcEndCondition\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
