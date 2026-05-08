# swBodyType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBodyType_e`

Valid body types.
Valid body types.

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

<System.Runtime.InteropServices.GuidAttribute("B0EE039B-BCA7-4EC7-8733-B70359940F67")>
Public Enum swBodyType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swBodyType_e
```

```

[System.Runtime.InteropServices.Guid("B0EE039B-BCA7-4EC7-8733-B70359940F67")]
public enum swBodyType_e : System.Enum 
```

```

public enum swBodyType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("B0EE039B-BCA7-4EC7-8733-B70359940F67")
public enum swBodyType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("B0EE039B-BCA7-4EC7-8733-B70359940F67")]
__value public enum swBodyType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("B0EE039B-BCA7-4EC7-8733-B70359940F67")]
public enum class swBodyType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAllBodies** | -1 = All solid and sheet bodies |
| **swEmptyBody** | 5 = NULL body |
| **swGeneralBody** | 4 = General, nonmanifold body |
| **swGraphicsBody** | 7 = Graphics body |
| **swMeshBody** | 6 = Mesh body |
| **swMinimumBody** | 3 = Point body |
| **swSheetBody** | 1 = Sheet body |
| **swSolidBody** | 0 = Solid body |
| **swWireBody** | 2 = Wire body |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swBodyType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
