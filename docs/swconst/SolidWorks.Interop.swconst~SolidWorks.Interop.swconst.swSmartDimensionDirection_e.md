# swSmartDimensionDirection_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSmartDimensionDirection_e`

Smart dimension extension line directions or rapid dimensioning selector quadrants.
Smart dimension extension line directions or rapid dimensioning selector quadrants.

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

<System.Runtime.InteropServices.GuidAttribute("C080E902-883C-4847-B9DA-24F9AD27F9A4")>
Public Enum swSmartDimensionDirection_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swSmartDimensionDirection_e
```

```

[System.Runtime.InteropServices.Guid("C080E902-883C-4847-B9DA-24F9AD27F9A4")]
public enum swSmartDimensionDirection_e : System.Enum 
```

```

public enum swSmartDimensionDirection_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("C080E902-883C-4847-B9DA-24F9AD27F9A4")
public enum swSmartDimensionDirection_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("C080E902-883C-4847-B9DA-24F9AD27F9A4")]
__value public enum swSmartDimensionDirection_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("C080E902-883C-4847-B9DA-24F9AD27F9A4")]
public enum class swSmartDimensionDirection_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSmartDimensionDirection\_Down** | 3 |
| **swSmartDimensionDirection\_Left** | 2 |
| **swSmartDimensionDirection\_Right** | 0 |
| **swSmartDimensionDirection\_Up** | 1 |

Remarks

In parts, this enumerator is used to specify the extension line that is needed to unambiguously define the angle to dimension. In the user interface, a direction manipulator appears during dimensioning if selected entities do not fully specify the angle to dimension. This enumerator specifies the directions of that manipulator.

In drawings that have **Rapid dimensioning** turned on, this enumerator may be used to specify the quadrant or side of the entities to which to add the display dimension.

See [IModelDocExtension::AddDimension](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDimension.html).

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swSmartDimensionDirection\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
