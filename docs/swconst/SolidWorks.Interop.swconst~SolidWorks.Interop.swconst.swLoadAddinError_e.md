# swLoadAddinError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swLoadAddinError_e`

Add-in load errors.
Add-in load errors.

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

<System.Runtime.InteropServices.GuidAttribute("54715A22-6AD4-489B-914A-176A29D8D81F")>
Public Enum swLoadAddinError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swLoadAddinError_e
```

```

[System.Runtime.InteropServices.Guid("54715A22-6AD4-489B-914A-176A29D8D81F")]
public enum swLoadAddinError_e : System.Enum 
```

```

public enum swLoadAddinError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("54715A22-6AD4-489B-914A-176A29D8D81F")
public enum swLoadAddinError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("54715A22-6AD4-489B-914A-176A29D8D81F")]
__value public enum swLoadAddinError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("54715A22-6AD4-489B-914A-176A29D8D81F")]
public enum class swLoadAddinError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAddinAlreadyLoaded** | 2 |
| **swAddinNotLoaded** | 1 |
| **swAddinsDisabled** | 4 |
| **swFileNotFound** | 3 |
| **swLicenseError** | 7 |
| **swLoadConflict** | 5 |
| **swRegistrationError** | 6 |
| **swSuccess** | 0 |
| **swUnknownError** | -1 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swLoadAddinError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
