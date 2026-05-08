# swPropMgrPageTextBoxStyle_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPropMgrPageTextBoxStyle_e`

PropertyManager page textbox styles. Bitmask.
PropertyManager page textbox styles. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("FB98BB90-9428-4375-B5FC-78BB2A91D90D")>
Public Enum swPropMgrPageTextBoxStyle_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swPropMgrPageTextBoxStyle_e
```

```

[System.Runtime.InteropServices.Guid("FB98BB90-9428-4375-B5FC-78BB2A91D90D")]
public enum swPropMgrPageTextBoxStyle_e : System.Enum 
```

```

public enum swPropMgrPageTextBoxStyle_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("FB98BB90-9428-4375-B5FC-78BB2A91D90D")
public enum swPropMgrPageTextBoxStyle_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("FB98BB90-9428-4375-B5FC-78BB2A91D90D")]
__value public enum swPropMgrPageTextBoxStyle_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("FB98BB90-9428-4375-B5FC-78BB2A91D90D")]
public enum class swPropMgrPageTextBoxStyle_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swPropMgrPageTextBoxStyle\_Multiline** | 8 or 0x8 |
| **swPropMgrPageTextBoxStyle\_NoBorder** | 4 or 0x4 |
| **swPropMgrPageTextBoxStyle\_NotifyOnlyWhenFocusLost** | 1 or 0x1; Do not send notification every time a character in the text box changes; instead, only send notification when text box loses focus after the user has made all changes |
| **swPropMgrPageTextBoxStyle\_ReadOnly** | 2 or 0x2 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swPropMgrPageTextBoxStyle\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
