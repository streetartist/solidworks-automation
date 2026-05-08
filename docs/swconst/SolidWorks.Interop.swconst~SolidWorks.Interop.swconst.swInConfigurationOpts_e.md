# swInConfigurationOpts_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInConfigurationOpts_e`

Configuration options.
Configuration options.

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

<System.Runtime.InteropServices.GuidAttribute("B499265E-F332-4756-BC2B-1348BFD6FE1E")>
Public Enum swInConfigurationOpts_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swInConfigurationOpts_e
```

```

[System.Runtime.InteropServices.Guid("B499265E-F332-4756-BC2B-1348BFD6FE1E")]
public enum swInConfigurationOpts_e : System.Enum 
```

```

public enum swInConfigurationOpts_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("B499265E-F332-4756-BC2B-1348BFD6FE1E")
public enum swInConfigurationOpts_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("B499265E-F332-4756-BC2B-1348BFD6FE1E")]
__value public enum swInConfigurationOpts_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("B499265E-F332-4756-BC2B-1348BFD6FE1E")]
public enum class swInConfigurationOpts_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAllConfiguration** | 2 |
| **swConfigPropertySuppressFeatures** | 0 |
| **swLinkedToParent** | 4 = Valid only for derived configurations; if specified for non-derived configurations, then the active configuration is used |
| **swSpecifyConfiguration** | 3 |
| **swSpeedpakConfiguration** | 5 |
| **swThisConfiguration** | 1 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swInConfigurationOpts\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
