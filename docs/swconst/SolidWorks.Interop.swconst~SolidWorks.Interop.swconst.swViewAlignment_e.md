# swViewAlignment_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swViewAlignment_e`

Values for alignment of views.
Values for alignment of views.

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

<System.Runtime.InteropServices.GuidAttribute("C11E0BFF-869F-4397-88E6-BF65C2D2AE93")>
Public Enum swViewAlignment_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swViewAlignment_e
```

```

[System.Runtime.InteropServices.Guid("C11E0BFF-869F-4397-88E6-BF65C2D2AE93")]
public enum swViewAlignment_e : System.Enum 
```

```

public enum swViewAlignment_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("C11E0BFF-869F-4397-88E6-BF65C2D2AE93")
public enum swViewAlignment_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("C11E0BFF-869F-4397-88E6-BF65C2D2AE93")]
__value public enum swViewAlignment_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("C11E0BFF-869F-4397-88E6-BF65C2D2AE93")]
public enum class swViewAlignment_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swViewAlignBoth** | 3 = View is aligned and has aligned children |
| **swViewAligned** | 2 = View is aligned with a parent view |
| **swViewAlignedChildren** | 1 = View has children aligned with it |
| **swViewAlignNone** | 0 = View has no alignment restrictions |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swViewAlignment\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
