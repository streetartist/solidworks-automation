# swAdvSelectType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAdvSelectType_e`

Conditions of criteria for advanced component selection list. Bitmask.
Conditions of criteria for advanced component selection list. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("D1DF409D-9EB6-458A-9624-6AA7846A56B7")>
Public Enum swAdvSelectType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swAdvSelectType_e
```

```

[System.Runtime.InteropServices.Guid("D1DF409D-9EB6-458A-9624-6AA7846A56B7")]
public enum swAdvSelectType_e : System.Enum 
```

```

public enum swAdvSelectType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("D1DF409D-9EB6-458A-9624-6AA7846A56B7")
public enum swAdvSelectType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("D1DF409D-9EB6-458A-9624-6AA7846A56B7")]
__value public enum swAdvSelectType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("D1DF409D-9EB6-458A-9624-6AA7846A56B7")]
public enum class swAdvSelectType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAdvSelectType\_And** | 1 or 0x1 |
| **swAdvSelectType\_Contains** | 16 or 0x10 |
| **swAdvSelectType\_Does\_Not\_Interferes\_With** | 128 or 0x80 |
| **swAdvSelectType\_Equals** | 4096 or 0x1000 |
| **swAdvSelectType\_Greater\_Than** | 256 or 0x100 |
| **swAdvSelectType\_Greater\_Than\_OR\_Equal** | 1024 or 0x400 |
| **swAdvSelectType\_Interferes\_With** | 64 or 0x40 |
| **swAdvSelectType\_Is\_Ccontained\_By** | 32 or 0x20 |
| **swAdvSelectType\_Is\_Exactly** | 4 or 0x4 |
| **swAdvSelectType\_Is\_No** | 32768 or 0x8000 |
| **swAdvSelectType\_Is\_Not** | 8 or 0x8 |
| **swAdvSelectType\_Is\_Not\_Equal** | 8192 or 0x2000 |
| **swAdvSelectType\_Is\_Yes** | 16384 or 0x4000 |
| **swAdvSelectType\_Less\_Than** | 512 or 0x200 |
| **swAdvSelectType\_Less\_Than\_OR\_Equal** | 2048 or 0x800 |
| **swAdvSelectType\_Or** | 2 or 0x2 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swAdvSelectType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
