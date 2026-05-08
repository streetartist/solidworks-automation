# swConfigurationOptions2_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConfigurationOptions2_e`

Option bits used when setting configuration options. Bitmask.
Option bits used when setting configuration options. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("995D622F-5316-4EA8-81DD-2B9696AA9FEA")>
Public Enum swConfigurationOptions2_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swConfigurationOptions2_e
```

```

[System.Runtime.InteropServices.Guid("995D622F-5316-4EA8-81DD-2B9696AA9FEA")]
public enum swConfigurationOptions2_e : System.Enum 
```

```

public enum swConfigurationOptions2_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("995D622F-5316-4EA8-81DD-2B9696AA9FEA")
public enum swConfigurationOptions2_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("995D622F-5316-4EA8-81DD-2B9696AA9FEA")]
__value public enum swConfigurationOptions2_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("995D622F-5316-4EA8-81DD-2B9696AA9FEA")]
public enum class swConfigurationOptions2_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swConfigOption\_DoDisolveInBOM** | 256 or 0x100; True to dissolve the configuration in the BOM and promote all of its child components up one level, false to not |
| **swConfigOption\_DontActivate** | 128 or 0x80; True to not activate the configuration, false to activate the configuration |
| **swConfigOption\_DontShowPartsInBOM** | 2 or 0x2; True to show sub-assemblies in the Bill of Materials, false to list child components in the Bill of Materials |
| **swConfigOption\_HideByDefault** | 8 or 0x8; True to hide newly added components, false to not |
| **swConfigOption\_InheritProperties** | Obsolete |
| **swConfigOption\_LinkToParent** | 64 or 0x40; True to link component to parent configuration, false to not |
| **swConfigOption\_MinFeatureManager** | 16 or 0x10; True to suppress new components, false to not |
| **swConfigOption\_SuppressByDefault** | 4 or 0x4; True to suppress newly added features and mates in this configuration, false to not |
| **swConfigOption\_UseAlternateName** | 1 or 0x1; True to use an alternate configuration name, false to not |
| **swConfigOption\_UseDescriptionInBOM** | 512 or 0x200; True to use the description in the BOM, false to not |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swConfigurationOptions2\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
