# swWrapSketchType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swWrapSketchType_e`

Wrap sketch types.
Wrap sketch types.

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

<System.Runtime.InteropServices.GuidAttribute("47BDC789-5E2A-477C-A794-21E369851D00")>
Public Enum swWrapSketchType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swWrapSketchType_e
```

```

[System.Runtime.InteropServices.Guid("47BDC789-5E2A-477C-A794-21E369851D00")]
public enum swWrapSketchType_e : System.Enum 
```

```

public enum swWrapSketchType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("47BDC789-5E2A-477C-A794-21E369851D00")
public enum swWrapSketchType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("47BDC789-5E2A-477C-A794-21E369851D00")]
__value public enum swWrapSketchType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("47BDC789-5E2A-477C-A794-21E369851D00")]
public enum class swWrapSketchType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swWrapSketchType\_Emboss** | 0 = Emboss creates a raised feature on the selected face or faces |
| **swWrapSketchType\_Engrave** | 1 = Engrave, which appears as Deboss in the user interface, creates an indented feature on the selected face or faces |
| **swWrapSketchType\_Scribe** | 2 = Scribe creates an imprint of the sketch contours on the selected face or faces |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swWrapSketchType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
