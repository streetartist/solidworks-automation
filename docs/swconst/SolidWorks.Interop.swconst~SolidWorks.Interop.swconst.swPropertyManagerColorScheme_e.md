# swPropertyManagerColorScheme_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPropertyManagerColorScheme_e`

Color schemes for PropertyManager pages.
Color schemes for PropertyManager pages.

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

<System.Runtime.InteropServices.GuidAttribute("F0A63F08-319D-444F-B6CF-2AB9788970CF")>
Public Enum swPropertyManagerColorScheme_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swPropertyManagerColorScheme_e
```

```

[System.Runtime.InteropServices.Guid("F0A63F08-319D-444F-B6CF-2AB9788970CF")]
public enum swPropertyManagerColorScheme_e : System.Enum 
```

```

public enum swPropertyManagerColorScheme_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("F0A63F08-319D-444F-B6CF-2AB9788970CF")
public enum swPropertyManagerColorScheme_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("F0A63F08-319D-444F-B6CF-2AB9788970CF")]
__value public enum swPropertyManagerColorScheme_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("F0A63F08-319D-444F-B6CF-2AB9788970CF")]
public enum class swPropertyManagerColorScheme_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swPropertyManagerColorScheme\_Blue** | 1 |
| **swPropertyManagerColorScheme\_Default** | 7 |
| **swPropertyManagerColorScheme\_Gray** | 2 |
| **swPropertyManagerColorScheme\_Mustard** | 3 |
| **swPropertyManagerColorScheme\_Olive** | 4 |
| **swPropertyManagerColorScheme\_Sand** | 5 |
| **swPropertyManagerColorScheme\_SeaGreen** | 6 |
| **swPropertyManagerColorScheme\_Windows** | 8 |

Remarks

These enumerators describe themes for the various colors used in the PropertyManager pages, not a specific color. When a scheme is changed, any open PropertyManager pages are immediately updated to the new color scheme.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swPropertyManagerColorScheme\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
