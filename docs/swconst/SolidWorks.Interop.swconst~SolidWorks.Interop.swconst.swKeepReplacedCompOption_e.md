# swKeepReplacedCompOption_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swKeepReplacedCompOption_e`

Options for replacing components in BOM features.
Options for replacing components in BOM features.

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

<System.Runtime.InteropServices.GuidAttribute("AB6090A3-0659-46B8-B579-F6184ABD580E")>
Public Enum swKeepReplacedCompOption_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swKeepReplacedCompOption_e
```

```

[System.Runtime.InteropServices.Guid("AB6090A3-0659-46B8-B579-F6184ABD580E")]
public enum swKeepReplacedCompOption_e : System.Enum 
```

```

public enum swKeepReplacedCompOption_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("AB6090A3-0659-46B8-B579-F6184ABD580E")
public enum swKeepReplacedCompOption_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("AB6090A3-0659-46B8-B579-F6184ABD580E")]
__value public enum swKeepReplacedCompOption_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("AB6090A3-0659-46B8-B579-F6184ABD580E")]
public enum class swKeepReplacedCompOption_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swKeepBothNewItemNumber** | 0 = Keep both with new item number |
| **swKeepBothSameItemNumber** | 1 = Keep both with same item number |
| **swKeepItemNumber** | 2 = Keep item number and do not keep replaced component |
| **swKeepNewItemNumberRemoveReplacedComp** | 3 = Assign new item number and do not keep replaced component |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swKeepReplacedCompOption\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
