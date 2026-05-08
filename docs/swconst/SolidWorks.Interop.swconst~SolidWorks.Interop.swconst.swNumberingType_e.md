# swNumberingType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swNumberingType_e`

Types of numbering for indented BOM tables.
Types of numbering for indented BOM tables.

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

<System.Runtime.InteropServices.GuidAttribute("7001B8A5-05D6-4B47-80DB-8329D63901E3")>
Public Enum swNumberingType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swNumberingType_e
```

```

[System.Runtime.InteropServices.Guid("7001B8A5-05D6-4B47-80DB-8329D63901E3")]
public enum swNumberingType_e : System.Enum 
```

```

public enum swNumberingType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("7001B8A5-05D6-4B47-80DB-8329D63901E3")
public enum swNumberingType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("7001B8A5-05D6-4B47-80DB-8329D63901E3")]
__value public enum swNumberingType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("7001B8A5-05D6-4B47-80DB-8329D63901E3")]
public enum class swNumberingType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swIndentedBOMNotSet** | 3 = The BOM table type is not [swBomType\_e](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBomType_e.md).swBomType\_Indented. |
| **swNumberingType\_Detailed** | 1 |
| **swNumberingType\_Flat** | 2 |
| **swNumberingType\_None** | 0 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swNumberingType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
