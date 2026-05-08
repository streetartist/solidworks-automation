# swDimensionArrowsSide_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDimensionArrowsSide_e`

Dimension arrow directions.
Dimension arrow directions.

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

<System.Runtime.InteropServices.GuidAttribute("DF21BDD5-5FAE-4B1A-AA68-C280FA66D1E1")>
Public Enum swDimensionArrowsSide_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swDimensionArrowsSide_e
```

```

[System.Runtime.InteropServices.Guid("DF21BDD5-5FAE-4B1A-AA68-C280FA66D1E1")]
public enum swDimensionArrowsSide_e : System.Enum 
```

```

public enum swDimensionArrowsSide_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("DF21BDD5-5FAE-4B1A-AA68-C280FA66D1E1")
public enum swDimensionArrowsSide_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("DF21BDD5-5FAE-4B1A-AA68-C280FA66D1E1")]
__value public enum swDimensionArrowsSide_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("DF21BDD5-5FAE-4B1A-AA68-C280FA66D1E1")]
public enum class swDimensionArrowsSide_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swDimArrowsFollowDoc** | 3 = As per the document's default setting |
| **swDimArrowsInside** | 0 = Always positioned on the inside |
| **swDimArrowsOutside** | 1 = Always positioned on the outside |
| **swDimArrowsSmart** | 2 = Positioned on the inside, if there is room; otherwise, positioned on the outside |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swDimensionArrowsSide\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
