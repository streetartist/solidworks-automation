# swStep242Error_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStep242Error_e`

Status codes for exporting SOLIDWORKS MBD 3D PDF files to STEP 242.
Status codes for exporting SOLIDWORKS MBD 3D PDF files to STEP 242.

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

<System.Runtime.InteropServices.GuidAttribute("FFEB709A-35DB-456B-AEE0-392FB2701628")>
Public Enum swStep242Error_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swStep242Error_e
```

```

[System.Runtime.InteropServices.Guid("FFEB709A-35DB-456B-AEE0-392FB2701628")]
public enum swStep242Error_e : System.Enum 
```

```

public enum swStep242Error_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("FFEB709A-35DB-456B-AEE0-392FB2701628")
public enum swStep242Error_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("FFEB709A-35DB-456B-AEE0-392FB2701628")]
__value public enum swStep242Error_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("FFEB709A-35DB-456B-AEE0-392FB2701628")]
public enum class swStep242Error_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swPublishStep242\_CustomPropertyError** | 6 |
| **swPublishStep242\_EditionError** | 5 |
| **swPublishStep242\_InvalidPath** | 1 |
| **swPublishStep242\_MBDLicenseNotAvailable** | 4 |
| **swPublishStep242\_Success** | 0 |
| **swPublishStep242\_UnknownError** | 3 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swStep242Error\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
