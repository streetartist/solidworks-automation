# swAddGroupBoxOptions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAddGroupBoxOptions_e`

PropertyManager page group box and tab controls. Bitmask.
PropertyManager page group box and tab controls. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("6875D35E-AAB7-4096-8E90-DE604A37E835")>
Public Enum swAddGroupBoxOptions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swAddGroupBoxOptions_e
```

```

[System.Runtime.InteropServices.Guid("6875D35E-AAB7-4096-8E90-DE604A37E835")]
public enum swAddGroupBoxOptions_e : System.Enum 
```

```

public enum swAddGroupBoxOptions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("6875D35E-AAB7-4096-8E90-DE604A37E835")
public enum swAddGroupBoxOptions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("6875D35E-AAB7-4096-8E90-DE604A37E835")]
__value public enum swAddGroupBoxOptions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("6875D35E-AAB7-4096-8E90-DE604A37E835")]
public enum class swAddGroupBoxOptions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swGroupBoxOptions\_Checkbox** | 1 or 0x1 |
| **swGroupBoxOptions\_Checked** | 2 or 0x2 |
| **swGroupBoxOptions\_Expanded** | 8 or 0x8 |
| **swGroupBoxOptions\_Visible** | 4 or 0x4 |

Remarks

Bitmask

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swAddGroupBoxOptions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
