# swArrowPosition Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swArrowPosition`

Arrow positions for bubble ToolTips.
Arrow positions for bubble ToolTips.

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

<System.Runtime.InteropServices.GuidAttribute("775FF304-7AC9-4612-B290-3BCFBE354970")>
Public Enum swArrowPosition 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swArrowPosition
```

```

[System.Runtime.InteropServices.Guid("775FF304-7AC9-4612-B290-3BCFBE354970")]
public enum swArrowPosition : System.Enum 
```

```

public enum swArrowPosition = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("775FF304-7AC9-4612-B290-3BCFBE354970")
public enum swArrowPosition extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("775FF304-7AC9-4612-B290-3BCFBE354970")]
__value public enum swArrowPosition : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("775FF304-7AC9-4612-B290-3BCFBE354970")]
public enum class swArrowPosition : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swArrowDownBottomLeft** | 6 = Down and on the bottom-left edge of bubble |
| **swArrowDownBottomRight** | 7 = Down and on the bottom-right edge of bubble |
| **swArrowLeftBottom** | 1 = Left and at bottom corner of bubble |
| **swArrowLeftOrRight** | 10 = Left or right; code decides if arrow on top or bottom corner |
| **swArrowLeftOrRightBottom** | 9 = Left or right and in one of the bottom corners of bubble |
| **swArrowLeftOrRightTop** | 8 = Left or right and in one of the top corners of bubble |
| **swArrowLeftTop** | 0 = Left and at top corner of bubble |
| **swArrowNone** | 14 = No arrow used; instead, a floating |
| **swArrowRightBottom** | 3 = Right and at bottom corner of bubble |
| **swArrowRightTop** | 2 = Right and at top corner of bubble |
| **swArrowUnknown** | 15 = Do not know where to put the arrow; instead, ActiveX control decides where to put arrow or its default position is used |
| **swArrowUpOrDown** | 13 = Upward or downward; code decides if arrow left or right of the bubble |
| **swArrowUpOrDownLeft** | 11 = Upward or downward and on left side of bubble |
| **swArrowUpOrDownRight** | 12 = Upward or downward and on right side of bubble |
| **swArrowUpTopLeft** | 4 = Upward and on the top-left edge of bubble |
| **swArrowUpTopRight** | 5 = Upward and on the top-right edge of bubble |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swArrowPosition**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
