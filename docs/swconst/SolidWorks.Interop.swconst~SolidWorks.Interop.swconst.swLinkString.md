# swLinkString Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swLinkString`

Types of links for errors and trouble-shooting bubbles.
Types of links for errors and trouble-shooting bubbles.

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

<System.Runtime.InteropServices.GuidAttribute("80C4DAFA-C8B3-4DBA-95E7-2C721E07F1BB")>
Public Enum swLinkString 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swLinkString
```

```

[System.Runtime.InteropServices.Guid("80C4DAFA-C8B3-4DBA-95E7-2C721E07F1BB")]
public enum swLinkString : System.Enum 
```

```

public enum swLinkString = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("80C4DAFA-C8B3-4DBA-95E7-2C721E07F1BB")
public enum swLinkString extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("80C4DAFA-C8B3-4DBA-95E7-2C721E07F1BB")]
__value public enum swLinkString : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("80C4DAFA-C8B3-4DBA-95E7-2C721E07F1BB")]
public enum class swLinkString : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swLinkStringNone** | 0 = None |
| **swLinkStringTroubleShootTip** | 2 = Trouble-shooting tip |
| **swLinkStringUserDefined** | 1 = User-defined |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swLinkString**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
