# swBendType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBendType_e`

Bend types.
Bend types.

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

<System.Runtime.InteropServices.GuidAttribute("4611547F-410A-4F62-9514-0EF12B2B127E")>
Public Enum swBendType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swBendType_e
```

```

[System.Runtime.InteropServices.Guid("4611547F-410A-4F62-9514-0EF12B2B127E")]
public enum swBendType_e : System.Enum 
```

```

public enum swBendType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("4611547F-410A-4F62-9514-0EF12B2B127E")
public enum swBendType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("4611547F-410A-4F62-9514-0EF12B2B127E")]
__value public enum swBendType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("4611547F-410A-4F62-9514-0EF12B2B127E")]
public enum class swBendType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swBaseBend** | 4 |
| **swEdgeFlangeBend** | 8 |
| **swFlat3dBend** | 6 |
| **swFlatBend** | 2 |
| **swFreeFormBend** | 10 = Obsolete |
| **swHemBend** | 9 |
| **swLoftedBend** | 12 |
| **swMirrorBend** | 7 |
| **swMiterBend** | 5 |
| **swNoneBend** | 3 |
| **swRoundBend** | 1 |
| **swRuledBend** | 11 = Obsolete |
| **swSharpBend** | 0 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swBendType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
