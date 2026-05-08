# swFlangePositionTypes_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFlangePositionTypes_e`

Position types for sheet metal edge flanges.
Position types for sheet metal edge flanges.

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

<System.Runtime.InteropServices.GuidAttribute("37B3C852-D0E9-4885-82AF-5C2BBAC11902")>
Public Enum swFlangePositionTypes_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swFlangePositionTypes_e
```

```

[System.Runtime.InteropServices.Guid("37B3C852-D0E9-4885-82AF-5C2BBAC11902")]
public enum swFlangePositionTypes_e : System.Enum 
```

```

public enum swFlangePositionTypes_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("37B3C852-D0E9-4885-82AF-5C2BBAC11902")
public enum swFlangePositionTypes_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("37B3C852-D0E9-4885-82AF-5C2BBAC11902")]
__value public enum swFlangePositionTypes_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("37B3C852-D0E9-4885-82AF-5C2BBAC11902")]
public enum class swFlangePositionTypes_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swFlangePositionTypeBendCenterLine** | 4 |
| **swFlangePositionTypeBendOutside** | 3 |
| **swFlangePositionTypeBendSharp** | 5 = Bend from virtual sharp |
| **swFlangePositionTypeBendTangent** | 6 = The flange position will always be tangent to the side face attached to the selected edge, and the flange length will always maintain the exact length; not valid for the Up To Edge And Merge length end condition |
| **swFlangePositionTypeMaterialInside** | 1 |
| **swFlangePositionTypeMaterialOutside** | 2 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swFlangePositionTypes\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
