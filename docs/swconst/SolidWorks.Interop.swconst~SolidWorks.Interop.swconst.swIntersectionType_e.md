# swIntersectionType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swIntersectionType_e`

Curve intersections types.
Curve intersections types.

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

<System.Runtime.InteropServices.GuidAttribute("44C867BB-4261-48BA-A025-528813D9858A")>
Public Enum swIntersectionType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swIntersectionType_e
```

```

[System.Runtime.InteropServices.Guid("44C867BB-4261-48BA-A025-528813D9858A")]
public enum swIntersectionType_e : System.Enum 
```

```

public enum swIntersectionType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("44C867BB-4261-48BA-A025-528813D9858A")
public enum swIntersectionType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("44C867BB-4261-48BA-A025-528813D9858A")]
__value public enum swIntersectionType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("44C867BB-4261-48BA-A025-528813D9858A")]
public enum class swIntersectionType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swIntersectionCOINCIDENCE\_END** | 4 = An intersection at the end of a region of coincidence |
| **swIntersectionCOINCIDENCE\_START** | 3 = An intersection at the start of a region of coincidence |
| **swIntersectionSIMPLE** | 1 = An intersection not adjoining a region of coincidence |
| **swIntersectionTANGENT** | 2 = A tangent intersection |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swIntersectionType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
