# swDocTemplateTypes_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDocTemplateTypes_e`

Document template types. Bitmask.
Document template types. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("5A904024-83A4-4E12-B892-31AA047285AC")>
Public Enum swDocTemplateTypes_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swDocTemplateTypes_e
```

```

[System.Runtime.InteropServices.Guid("5A904024-83A4-4E12-B892-31AA047285AC")]
public enum swDocTemplateTypes_e : System.Enum 
```

```

public enum swDocTemplateTypes_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("5A904024-83A4-4E12-B892-31AA047285AC")
public enum swDocTemplateTypes_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("5A904024-83A4-4E12-B892-31AA047285AC")]
__value public enum swDocTemplateTypes_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("5A904024-83A4-4E12-B892-31AA047285AC")]
public enum class swDocTemplateTypes_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swDocTemplateTypeASSEMBLY** | 4 or 0x4 |
| **swDocTemplateTypeDRAWING** | 8 or 0x8 |
| **swDocTemplateTypeInContext** | 16 or 0x10 |
| **swDocTemplateTypeNONE** | 1 or 0x1 |
| **swDocTemplateTypePART** | 2 or 0x2 |

Remarks

These values can be OR'd together to indicate on which toolbar the document types should reside.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swDocTemplateTypes\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
