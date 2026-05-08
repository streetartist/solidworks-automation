# swBalloonLayoutType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBalloonLayoutType_e`

Arrangements for automatic BOM balloons in relation to the drawing views with which they are associated.
Arrangements for automatic BOM balloons in relation to the drawing views with which they are associated.

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

<System.Runtime.InteropServices.GuidAttribute("C671D1E2-BDDF-4679-A146-CB10F71795AF")>
Public Enum swBalloonLayoutType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swBalloonLayoutType_e
```

```

[System.Runtime.InteropServices.Guid("C671D1E2-BDDF-4679-A146-CB10F71795AF")]
public enum swBalloonLayoutType_e : System.Enum 
```

```

public enum swBalloonLayoutType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("C671D1E2-BDDF-4679-A146-CB10F71795AF")
public enum swBalloonLayoutType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("C671D1E2-BDDF-4679-A146-CB10F71795AF")]
__value public enum swBalloonLayoutType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("C671D1E2-BDDF-4679-A146-CB10F71795AF")]
public enum class swBalloonLayoutType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swDetailingBalloonLayout\_Bottom** | 4 = Along the bottom edge of the drawing view |
| **swDetailingBalloonLayout\_Circle** | 2 = In a circle around the drawing view |
| **swDetailingBalloonLayout\_Left** | 6 = Along the left edge of the drawing view |
| **swDetailingBalloonLayout\_Right** | 5 = Along the right edge of the drawing view |
| **swDetailingBalloonLayout\_Square** | 1 = In a box around the drawing view |
| **swDetailingBalloonLayout\_Top** | 3 = Along the top edge of the drawing view |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swBalloonLayoutType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
