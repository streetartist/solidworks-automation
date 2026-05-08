# swUnitsDecimalRounding_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUnitsDecimalRounding_e`

Rounding options for decimal units.
Rounding options for decimal units.

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

<System.Runtime.InteropServices.GuidAttribute("C6F049BE-BF4D-4B27-A26F-9B103867FCE9")>
Public Enum swUnitsDecimalRounding_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swUnitsDecimalRounding_e
```

```

[System.Runtime.InteropServices.Guid("C6F049BE-BF4D-4B27-A26F-9B103867FCE9")]
public enum swUnitsDecimalRounding_e : System.Enum 
```

```

public enum swUnitsDecimalRounding_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("C6F049BE-BF4D-4B27-A26F-9B103867FCE9")
public enum swUnitsDecimalRounding_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("C6F049BE-BF4D-4B27-A26F-9B103867FCE9")]
__value public enum swUnitsDecimalRounding_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("C6F049BE-BF4D-4B27-A26F-9B103867FCE9")]
public enum class swUnitsDecimalRounding_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swUnitsDecimalRounding\_HalfAway** | 0 = Round up to the nearest decimal |
| **swUnitsDecimalRounding\_HalfToEven** | 2 = Round up or down to the next even decimal |
| **swUnitsDecimalRounding\_HalfTowards** | 1 = Round down to the nearest decimal |
| **swUnitsDecimalRounding\_Truncate** | 3 = Truncate the decimal without rounding |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swUnitsDecimalRounding\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
