# swShowMessageBarResult_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swShowMessageBarResult_e`

Message bar display result codes.
Message bar display result codes.

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

<System.Runtime.InteropServices.GuidAttribute("C7F19AC0-5163-4C7E-A4BB-156A16BF2AC6")>
Public Enum swShowMessageBarResult_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swShowMessageBarResult_e
```

```

[System.Runtime.InteropServices.Guid("C7F19AC0-5163-4C7E-A4BB-156A16BF2AC6")]
public enum swShowMessageBarResult_e : System.Enum 
```

```

public enum swShowMessageBarResult_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("C7F19AC0-5163-4C7E-A4BB-156A16BF2AC6")
public enum swShowMessageBarResult_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("C7F19AC0-5163-4C7E-A4BB-156A16BF2AC6")]
__value public enum swShowMessageBarResult_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("C7F19AC0-5163-4C7E-A4BB-156A16BF2AC6")]
public enum class swShowMessageBarResult_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swShowMessageBarResult\_DontShowAgain** | 1 = The message bar is not shown when "Don't show again" is selected |
| **swShowMessageBarResult\_FailedInvalidDefinition** | 2 = The message bar could not be displayed due to an invalid definition (e.g., empty title/description) |
| **swShowMessageBarResult\_FailedInvalidHandler** | 3 = The message bar could not be desiplayed because the Handler argument is NULL or does not support the expected interface |
| **swShowMessageBarResult\_Shown** | 0 = The modeless message bar is shown |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swShowMessageBarResult\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
