# swEdrawingsAttachmentOption_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEdrawingsAttachmentOption_e`

Configuration options for creating and attaching STEP files when publishing a part or assembly to eDrawings.
Configuration options for creating and attaching STEP files when publishing a part or assembly to eDrawings.

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

<System.Runtime.InteropServices.GuidAttribute("5B122CDD-932E-4152-B2FE-870EB1456E18")>
Public Enum swEdrawingsAttachmentOption_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swEdrawingsAttachmentOption_e
```

```

[System.Runtime.InteropServices.Guid("5B122CDD-932E-4152-B2FE-870EB1456E18")]
public enum swEdrawingsAttachmentOption_e : System.Enum 
```

```

public enum swEdrawingsAttachmentOption_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("5B122CDD-932E-4152-B2FE-870EB1456E18")
public enum swEdrawingsAttachmentOption_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("5B122CDD-932E-4152-B2FE-870EB1456E18")]
__value public enum swEdrawingsAttachmentOption_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("5B122CDD-932E-4152-B2FE-870EB1456E18")]
public enum class swEdrawingsAttachmentOption_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swEdrawingsAttachActive** | 1 = Create and attach STEP files to the active configuration only |
| **swEdrawingsAttachAll** | 2 = Create and attach STEP files to all configurations |
| **swEdrawingsAttachNone** | 0 = Do not create and attach any STEP files |
| **swEdrawingsAttachSelected** | 3 = Create and attach STEP files to specified configurations only |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swEdrawingsAttachmentOption\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
