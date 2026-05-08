# swZonalSectionViewZones_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swZonalSectionViewZones_e`

Intersection zones for section views. Bitmask
Intersection zones for section views. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm)

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

<System.Runtime.InteropServices.GuidAttribute("DB97F06F-4FD9-4EAF-BA0B-D1633913504B")>
Public Enum swZonalSectionViewZones_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swZonalSectionViewZones_e
```

```

[System.Runtime.InteropServices.Guid("DB97F06F-4FD9-4EAF-BA0B-D1633913504B")]
public enum swZonalSectionViewZones_e : System.Enum 
```

```

public enum swZonalSectionViewZones_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("DB97F06F-4FD9-4EAF-BA0B-D1633913504B")
public enum swZonalSectionViewZones_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("DB97F06F-4FD9-4EAF-BA0B-D1633913504B")]
__value public enum swZonalSectionViewZones_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("DB97F06F-4FD9-4EAF-BA0B-D1633913504B")]
public enum class swZonalSectionViewZones_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swZonalSectionViewZones\_swZonalSectionViewZone\_1** | 1 or 0x1 |
| **swZonalSectionViewZones\_swZonalSectionViewZone\_2** | 2 or 0x2 |
| **swZonalSectionViewZones\_swZonalSectionViewZone\_3** | 4 or 0x4 |
| **swZonalSectionViewZones\_swZonalSectionViewZone\_4** | 8 or 0x8 |
| **swZonalSectionViewZones\_swZonalSectionViewZone\_5** | 16 or 0x10 |
| **swZonalSectionViewZones\_swZonalSectionViewZone\_6** | 32 or 0x20 |
| **swZonalSectionViewZones\_swZonalSectionViewZone\_7** | 64 or 0x40 |
| **swZonalSectionViewZones\_swZonalSectionViewZone\_8** | 128 or 0x80 |

Remarks

Descriptions of the intersection zones in relation to the number of sectioning planes appear in [ISectionViewData::SectionedZones](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SectionedZones.html).

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swZonalSectionViewZones\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
