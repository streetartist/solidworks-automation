# swAnimationPlayMode_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAnimationPlayMode_e`

Modes to play animations.
Modes to play animations.

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

<System.Runtime.InteropServices.GuidAttribute("D624F71E-0FA9-485F-868A-C4C15F2DEE96")>
Public Enum swAnimationPlayMode_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swAnimationPlayMode_e
```

```

[System.Runtime.InteropServices.Guid("D624F71E-0FA9-485F-868A-C4C15F2DEE96")]
public enum swAnimationPlayMode_e : System.Enum 
```

```

public enum swAnimationPlayMode_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("D624F71E-0FA9-485F-868A-C4C15F2DEE96")
public enum swAnimationPlayMode_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("D624F71E-0FA9-485F-868A-C4C15F2DEE96")]
__value public enum swAnimationPlayMode_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("D624F71E-0FA9-485F-868A-C4C15F2DEE96")]
public enum class swAnimationPlayMode_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAnimationPlayModeLoop** | 2 = Play from beginning to end, from beginning to end, etc. |
| **swAnimationPlayModeNormal** | 1 = Play from beginning to end once. |
| **swAnimationPlayModeReciprocate** | 3 = Play from beginning to end, from end to beginning, beginning to end, etc. |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swAnimationPlayMode\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
