# swSheetMetalModifierError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSheetMetalModifierError_e`

Sheet metal feature data errors.
Sheet metal feature data errors.

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

<System.Runtime.InteropServices.GuidAttribute("05E87337-968C-42B8-8989-8A9BBD37B153")>
Public Enum swSheetMetalModifierError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swSheetMetalModifierError_e
```

```

[System.Runtime.InteropServices.Guid("05E87337-968C-42B8-8989-8A9BBD37B153")]
public enum swSheetMetalModifierError_e : System.Enum 
```

```

public enum swSheetMetalModifierError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("05E87337-968C-42B8-8989-8A9BBD37B153")
public enum swSheetMetalModifierError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("05E87337-968C-42B8-8989-8A9BBD37B153")]
__value public enum swSheetMetalModifierError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("05E87337-968C-42B8-8989-8A9BBD37B153")]
public enum class swSheetMetalModifierError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSheetMetalModifierError\_GaugeTablePathNotEmpty** | 5 = [ISheetMetalFeatureData::SetUseGaugeTable's](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheetMetalFeatureData~SetUseGaugeTable) GaugeTableFile parameter must be an empty string for derived sheet-metal features |
| **swSheetMetalModifierError\_InvalidProperty** | 3 |
| **swSheetMetalModifierError\_NoError** | 0 |
| **swSheetMetalModifierError\_NotEnabledOnTemplate** | 2 |
| **swSheetMetalModifierError\_OldArchitecture** | 1 |
| **swSheetMetalModifierError\_UnspecifiedError** | 4 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swSheetMetalModifierError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
