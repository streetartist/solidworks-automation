# swMacroFeatureSecurityOptions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMacroFeatureSecurityOptions_e`

Macro feature security options. Bitmask.
Macro feature security options. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("4F3FF558-EE02-4343-963C-42981BF87120")>
Public Enum swMacroFeatureSecurityOptions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swMacroFeatureSecurityOptions_e
```

```

[System.Runtime.InteropServices.Guid("4F3FF558-EE02-4343-963C-42981BF87120")]
public enum swMacroFeatureSecurityOptions_e : System.Enum 
```

```

public enum swMacroFeatureSecurityOptions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("4F3FF558-EE02-4343-963C-42981BF87120")
public enum swMacroFeatureSecurityOptions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("4F3FF558-EE02-4343-963C-42981BF87120")]
__value public enum swMacroFeatureSecurityOptions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("4F3FF558-EE02-4343-963C-42981BF87120")]
public enum class swMacroFeatureSecurityOptions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swMacroFeatureSecurityByDefault** | 0 or 0x0 |
| **swMacroFeatureSecurityCannotBeDeleted** | 1 or 0x1 |
| **swMacroFeatureSecurityCannotBeReplaced** | 8 or 0x8 |
| **swMacroFeatureSecurityCannotBeRolledBack** | 32 or 0x20 |
| **swMacroFeatureSecurityCannotBeSuppressed** | 4 or 0x4 |
| **swMacroFeatureSecurityEnableNote** | 16 or 0x10 |
| **swMacroFeatureSecurityNotEditable** | 2 or 0x2 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swMacroFeatureSecurityOptions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
