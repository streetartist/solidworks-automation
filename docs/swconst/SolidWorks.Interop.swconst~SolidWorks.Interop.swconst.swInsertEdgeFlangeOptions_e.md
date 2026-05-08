# swInsertEdgeFlangeOptions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInsertEdgeFlangeOptions_e`

Sheet metal edge flange options. Bitmask.
Sheet metal edge flange options. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("9C9737A4-700E-400A-B00E-B3C4ED3C32C3")>
Public Enum swInsertEdgeFlangeOptions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swInsertEdgeFlangeOptions_e
```

```

[System.Runtime.InteropServices.Guid("9C9737A4-700E-400A-B00E-B3C4ED3C32C3")]
public enum swInsertEdgeFlangeOptions_e : System.Enum 
```

```

public enum swInsertEdgeFlangeOptions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("9C9737A4-700E-400A-B00E-B3C4ED3C32C3")
public enum swInsertEdgeFlangeOptions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("9C9737A4-700E-400A-B00E-B3C4ED3C32C3")]
__value public enum swInsertEdgeFlangeOptions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("9C9737A4-700E-400A-B00E-B3C4ED3C32C3")]
public enum class swInsertEdgeFlangeOptions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swInsertEdgeFlangeDoOffset** | 4 or 0x4 |
| **swInsertEdgeFlangeFlipDir** | 2 or 0x2 |
| **swInsertEdgeFlangeReverseOffsetDir** | 8 or 0x8 |
| **swInsertEdgeFlangeTearClip** | 16 or 0x10 |
| **swInsertEdgeFlangeTrimSideBend** | 32 or 0x20 |
| **swInsertEdgeFlangeUseDefaultRadius** | 1 or 0x1 |
| **swInsertEdgeFlangeUseDefaultRelief** | 128 or 0x80 |
| **swInsertEdgeFlangeUseReliefRatio** | 64 or 0x40 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swInsertEdgeFlangeOptions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
