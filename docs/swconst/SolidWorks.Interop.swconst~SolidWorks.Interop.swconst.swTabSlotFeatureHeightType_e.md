# swTabSlotFeatureHeightType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTabSlotFeatureHeightType_e`

Types of tab height calculations in Tab and Slot groups.
Types of tab height calculations in Tab and Slot groups.

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

<System.Runtime.InteropServices.GuidAttribute("C9ECDFE1-72F8-45B7-88AF-C635EA6667C0")>
Public Enum swTabSlotFeatureHeightType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swTabSlotFeatureHeightType_e
```

```

[System.Runtime.InteropServices.Guid("C9ECDFE1-72F8-45B7-88AF-C635EA6667C0")]
public enum swTabSlotFeatureHeightType_e : System.Enum 
```

```

public enum swTabSlotFeatureHeightType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("C9ECDFE1-72F8-45B7-88AF-C635EA6667C0")
public enum swTabSlotFeatureHeightType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("C9ECDFE1-72F8-45B7-88AF-C635EA6667C0")]
__value public enum swTabSlotFeatureHeightType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("C9ECDFE1-72F8-45B7-88AF-C635EA6667C0")]
public enum class swTabSlotFeatureHeightType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **Blind** | 0 = Specify a tab height |
| **OffsetFromSurface** | 2 = Specify an offset and the slot face from which to offset the tab |
| **UpToSurface** | 1 = The height is calculated internally in reference to the slot face |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swTabSlotFeatureHeightType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
