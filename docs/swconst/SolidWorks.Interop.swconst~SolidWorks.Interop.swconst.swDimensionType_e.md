# swDimensionType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDimensionType_e`

Types of dimensions.
Types of dimensions.

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

<System.Runtime.InteropServices.GuidAttribute("F69AD815-224C-4478-BB91-C90F70F596CA")>
Public Enum swDimensionType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swDimensionType_e
```

```

[System.Runtime.InteropServices.Guid("F69AD815-224C-4478-BB91-C90F70F596CA")]
public enum swDimensionType_e : System.Enum 
```

```

public enum swDimensionType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("F69AD815-224C-4478-BB91-C90F70F596CA")
public enum swDimensionType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("F69AD815-224C-4478-BB91-C90F70F596CA")]
__value public enum swDimensionType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("F69AD815-224C-4478-BB91-C90F70F596CA")]
public enum class swDimensionType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAngularDimension** | 3 = Angular dimension type |
| **swAngularOrdinateDimension** | 16 = Angular ordinate dimension |
| **swArcLengthDimension** | 4 = Arc length dimension type |
| **swChamferDimension** | 10 |
| **swDiameterDimension** | 6 = Diameter dimension |
| **swDiametricLinearDimension** | 15 = Doubled distance linear dimension |
| **swDimensionTypeUnknown** | 0 = Dimension type could not be determined |
| **swHorLinearDimension** | 11 = Horizontal linear dimension |
| **swHorOrdinateDimension** | 7 = Horizontal ordinate dimension |
| **swLinearDimension** | 2 = Linear dimension type |
| **swOrdinateDimension** | 1 = Base ordinate and its subordinates are of this type |
| **swRadialDimension** | 5 = Radial dimension |
| **swRadialLinearDimension** | 14 = Doubled distance radial dimension |
| **swScalarDimension** | 13 |
| **swVertLinearDimension** | 12 = Vertical linear dimension |
| **swVertOrdinateDimension** | 8 = Vertical ordinate dimension |
| **swZAxisDimension** | 9 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swDimensionType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
