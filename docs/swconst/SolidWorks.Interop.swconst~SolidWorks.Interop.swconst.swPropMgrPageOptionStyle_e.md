# swPropMgrPageOptionStyle_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPropMgrPageOptionStyle_e`

PropertyManage page group option styles. Bitmask.
PropertyManage page group option styles. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("D2B31E89-6D6C-4566-9E76-EF36B411AF69")>
Public Enum swPropMgrPageOptionStyle_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swPropMgrPageOptionStyle_e
```

```

[System.Runtime.InteropServices.Guid("D2B31E89-6D6C-4566-9E76-EF36B411AF69")]
public enum swPropMgrPageOptionStyle_e : System.Enum 
```

```

public enum swPropMgrPageOptionStyle_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("D2B31E89-6D6C-4566-9E76-EF36B411AF69")
public enum swPropMgrPageOptionStyle_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("D2B31E89-6D6C-4566-9E76-EF36B411AF69")]
__value public enum swPropMgrPageOptionStyle_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("D2B31E89-6D6C-4566-9E76-EF36B411AF69")]
public enum class swPropMgrPageOptionStyle_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swPropMgrPageOptionStyle\_FirstInGroup** | 1 or 0x1; This is the beginning of a group of option items; any following option items without this value set are considered part of the group; the next option with this value set indicates the start of a new option group |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swPropMgrPageOptionStyle\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
