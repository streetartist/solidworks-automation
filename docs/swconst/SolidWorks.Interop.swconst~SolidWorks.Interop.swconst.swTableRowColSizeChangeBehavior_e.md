# swTableRowColSizeChangeBehavior_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTableRowColSizeChangeBehavior_e`

Values indicate how the size of the rest of the table should behave when a height of a row or width of a column changes.
Values indicate how the size of the rest of the table should behave when a height of a row or width of a column changes.

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

<System.Runtime.InteropServices.GuidAttribute("3EE45D03-9C7E-4BE5-9D2E-1180FDF06283")>
Public Enum swTableRowColSizeChangeBehavior_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swTableRowColSizeChangeBehavior_e
```

```

[System.Runtime.InteropServices.Guid("3EE45D03-9C7E-4BE5-9D2E-1180FDF06283")]
public enum swTableRowColSizeChangeBehavior_e : System.Enum 
```

```

public enum swTableRowColSizeChangeBehavior_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("3EE45D03-9C7E-4BE5-9D2E-1180FDF06283")
public enum swTableRowColSizeChangeBehavior_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("3EE45D03-9C7E-4BE5-9D2E-1180FDF06283")]
__value public enum swTableRowColSizeChangeBehavior_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("3EE45D03-9C7E-4BE5-9D2E-1180FDF06283")]
public enum class swTableRowColSizeChangeBehavior_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swTableRowColChange\_AbsorbedByNext** | 1 = The next row or column must absorb the change in size so that the entire table size remains the same |
| **swTableRowColChange\_AbsorbedByPrevious** | 2 = The next row or column must absorb the change in size so that the entire table size remains the same |
| **swTableRowColChange\_TableSizeCanChange** | 0 = The remaining rows or columns can shift, so that the entire table width or height changes |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swTableRowColSizeChangeBehavior\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
