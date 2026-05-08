# swDocumentTypes_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDocumentTypes_e`

Document types.
Document types.

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

<System.Runtime.InteropServices.GuidAttribute("55A9AAAE-97D1-4621-A5A9-21A67CDCE87A")>
Public Enum swDocumentTypes_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swDocumentTypes_e
```

```

[System.Runtime.InteropServices.Guid("55A9AAAE-97D1-4621-A5A9-21A67CDCE87A")]
public enum swDocumentTypes_e : System.Enum 
```

```

public enum swDocumentTypes_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("55A9AAAE-97D1-4621-A5A9-21A67CDCE87A")
public enum swDocumentTypes_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("55A9AAAE-97D1-4621-A5A9-21A67CDCE87A")]
__value public enum swDocumentTypes_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("55A9AAAE-97D1-4621-A5A9-21A67CDCE87A")]
public enum class swDocumentTypes_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swDocASSEMBLY** | 2 |
| **swDocDRAWING** | 3 |
| **swDocIMPORTED\_ASSEMBLY** | 7; Multi-CAD |
| **swDocIMPORTED\_PART** | 6; Multi-CAD |
| **swDocLAYOUT** | 5 |
| **swDocNONE** | 0 |
| **swDocPART** | 1 |
| **swDocSDM** | 4 |

Remarks

When opening library feature parts, use swDocPART.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swDocumentTypes\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
