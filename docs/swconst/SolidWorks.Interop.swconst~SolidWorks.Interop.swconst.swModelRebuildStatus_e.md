# swModelRebuildStatus_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swModelRebuildStatus_e`

Rebuild status of model. Bitmask.
Rebuild status of model. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("CEF612CA-48F9-468A-AD28-6F0292A403D0")>
Public Enum swModelRebuildStatus_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swModelRebuildStatus_e
```

```

[System.Runtime.InteropServices.Guid("CEF612CA-48F9-468A-AD28-6F0292A403D0")]
public enum swModelRebuildStatus_e : System.Enum 
```

```

public enum swModelRebuildStatus_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("CEF612CA-48F9-468A-AD28-6F0292A403D0")
public enum swModelRebuildStatus_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("CEF612CA-48F9-468A-AD28-6F0292A403D0")]
__value public enum swModelRebuildStatus_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("CEF612CA-48F9-468A-AD28-6F0292A403D0")]
public enum class swModelRebuildStatus_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swModelRebuildStatus\_FrozenFeatureNeedsRebuild** | 2 |
| **swModelRebuildStatus\_FullyRebuilt** | 0 or FALSE |
| **swModelRebuildStatus\_NonFrozenFeatureNeedsRebuild** | 1 or TRUE |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swModelRebuildStatus\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
