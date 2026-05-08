# swPropMgrPageSliderStyle_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPropMgrPageSliderStyle_e`

PropertyManager page slider styles. Bitmask.
PropertyManager page slider styles. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("696DA3AC-1F56-4642-9DEC-B373EA4BD6D0")>
Public Enum swPropMgrPageSliderStyle_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swPropMgrPageSliderStyle_e
```

```

[System.Runtime.InteropServices.Guid("696DA3AC-1F56-4642-9DEC-B373EA4BD6D0")]
public enum swPropMgrPageSliderStyle_e : System.Enum 
```

```

public enum swPropMgrPageSliderStyle_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("696DA3AC-1F56-4642-9DEC-B373EA4BD6D0")
public enum swPropMgrPageSliderStyle_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("696DA3AC-1F56-4642-9DEC-B373EA4BD6D0")]
__value public enum swPropMgrPageSliderStyle_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("696DA3AC-1F56-4642-9DEC-B373EA4BD6D0")]
public enum class swPropMgrPageSliderStyle_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swPropMgrPageSliderStyle\_AutoTicks** | 2 or 0x2; If set, then tick marks are created based on swPropMgrPageSliderStyle\_BottomLeftTicks and swPropMgrPageSliderStyle\_TopRightTicks |
| **swPropMgrPageSliderStyle\_BottomLeftTicks** | 4 or 0x4; If set, then tick marks appear at the bottom (horizontal) or left (vertical) of the slider |
| **swPropMgrPageSliderStyle\_NotifyWhileTracking** | 16 or 0x10; If set, then your application is notified when the user is dragging the slider, each time the value changes; if not set, then your application is not notified when the user is dragging the slider, only when the user is done dragging the slider; setting this bit allows your application to react immediately to changes, but it does generate many more callbacks, so it is less efficient |
| **swPropMgrPageSliderStyle\_TopRightTicks** | 8 or 0x8; If set, then tick marks appear at the top (horizontal) or right (vertical) of the slider |
| **swPropMgrPageSliderStyle\_Vertical** | 1 or 0x1; If set, then the slider is oriented vertically; if not set, then the slider is oriented horizontally |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swPropMgrPageSliderStyle\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
