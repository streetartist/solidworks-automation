# swComponentIdentifier_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swComponentIdentifier_e`

Component display options for the FeatureManager design tree. Bitmask.
Component display options for the FeatureManager design tree. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("D97FDC1F-57EB-42B7-AC3B-1D2518621791")>
Public Enum swComponentIdentifier_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swComponentIdentifier_e
```

```

[System.Runtime.InteropServices.Guid("D97FDC1F-57EB-42B7-AC3B-1D2518621791")]
public enum swComponentIdentifier_e : System.Enum 
```

```

public enum swComponentIdentifier_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("D97FDC1F-57EB-42B7-AC3B-1D2518621791")
public enum swComponentIdentifier_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("D97FDC1F-57EB-42B7-AC3B-1D2518621791")]
__value public enum swComponentIdentifier_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("D97FDC1F-57EB-42B7-AC3B-1D2518621791")]
public enum class swComponentIdentifier_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swComponentIdentifier\_ComponentDescription** | 4 |
| **swComponentIdentifier\_ComponentName** | 2 |
| **swComponentIdentifier\_ConfigurationDescription** | 64 |
| **swComponentIdentifier\_ConfigurationName** | 32 |
| **swComponentIdentifier\_DisplayStateName** | 128 |
| **swComponentIdentifier\_EnterpriseItemNumber** | 8 (valid only in SOLIDWORKS Connected) |
| **swComponentIdentifier\_FileTitle** | 256 (valid only in SOLIDWORKS Connected) |
| **swComponentIdentifier\_None** | 0 |
| **swComponentIdentifier\_PhysicalProductDescription** | 16 (valid only in SOLIDWORKS Connected) |
| **swComponentIdentifier\_PhysicalProductTitle** | 1 (valid only in SOLIDWORKS Connected) |
| **swComponentIdentifier\_PLMRevision** | 512 (valid only in SOLIDWORKS Connected) |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swComponentIdentifier\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
