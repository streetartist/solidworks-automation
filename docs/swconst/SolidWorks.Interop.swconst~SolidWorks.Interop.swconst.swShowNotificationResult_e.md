# swShowNotificationResult_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swShowNotificationResult_e`

User notification display return values.
User notification display return values.

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

<System.Runtime.InteropServices.GuidAttribute("0C8BD2C2-BA60-4DF0-B79D-6FC16A23F2B6")>
Public Enum swShowNotificationResult_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swShowNotificationResult_e
```

```

[System.Runtime.InteropServices.Guid("0C8BD2C2-BA60-4DF0-B79D-6FC16A23F2B6")]
public enum swShowNotificationResult_e : System.Enum 
```

```

public enum swShowNotificationResult_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("0C8BD2C2-BA60-4DF0-B79D-6FC16A23F2B6")
public enum swShowNotificationResult_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("0C8BD2C2-BA60-4DF0-B79D-6FC16A23F2B6")]
__value public enum swShowNotificationResult_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("0C8BD2C2-BA60-4DF0-B79D-6FC16A23F2B6")]
public enum class swShowNotificationResult_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swShowNotificationResult\_DontShowAgain** | 1 = The user notification is not shown when "Don't show again" is selected |
| **swShowNotificationResult\_FailedInvalidDefinition** | 2 = The user notification could not be displayed due to an invalid definition (e.g., empty title/description) |
| **swShowNotificationResult\_FailedInvalidHandler** | 3 = The user notification could not be desiplayed because the Handler argument is NULL or does not support the expected interface |
| **swShowNotificationResult\_Shown** | 0 = The user notification is shown |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swShowNotificationResult\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
