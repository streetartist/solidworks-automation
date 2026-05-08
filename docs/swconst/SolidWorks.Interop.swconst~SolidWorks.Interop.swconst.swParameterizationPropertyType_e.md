# swParameterizationPropertyType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swParameterizationPropertyType_e`

Properties of U and V parameters.
Properties of U and V parameters.

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

<System.Runtime.InteropServices.GuidAttribute("04EA05A7-AB61-4B8A-B812-0611943541AA")>
Public Enum swParameterizationPropertyType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swParameterizationPropertyType_e
```

```

[System.Runtime.InteropServices.Guid("04EA05A7-AB61-4B8A-B812-0611943541AA")]
public enum swParameterizationPropertyType_e : System.Enum 
```

```

public enum swParameterizationPropertyType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("04EA05A7-AB61-4B8A-B812-0611943541AA")
public enum swParameterizationPropertyType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("04EA05A7-AB61-4B8A-B812-0611943541AA")]
__value public enum swParameterizationPropertyType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("04EA05A7-AB61-4B8A-B812-0611943541AA")]
public enum class swParameterizationPropertyType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swParameterizationPropertyType\_AllDerivativesContinuous** | 13737 |
| **swParameterizationPropertyType\_AllDerivativesNotContinuous** | 13738 |
| **swParameterizationPropertyType\_BoundsCoincident** | 13746 = Bounds at the ends of the parameter range are coincident |
| **swParameterizationPropertyType\_Circular** | 13740 = The parameter represents an angle around a circle; A circle indicates that the other parameter is a constant |
| **swParameterizationPropertyType\_Linear** | 13739 = The parameter is proportional to the distance along a straight line; A straight line indicates that the other parameter is a constant |
| **swParameterizationPropertyType\_Periodic** | 13701 = Periodic parameterization |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swParameterizationPropertyType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
