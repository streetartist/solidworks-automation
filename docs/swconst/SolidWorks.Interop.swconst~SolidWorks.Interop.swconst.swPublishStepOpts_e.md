# swPublishStepOpts_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPublishStepOpts_e`

Options for publishing to Step 242.
Options for publishing to Step 242.

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

<System.Runtime.InteropServices.GuidAttribute("08A46722-38F9-409D-BBFC-D4FE0CEEC0F8")>
Public Enum swPublishStepOpts_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swPublishStepOpts_e
```

```

[System.Runtime.InteropServices.Guid("08A46722-38F9-409D-BBFC-D4FE0CEEC0F8")]
public enum swPublishStepOpts_e : System.Enum 
```

```

public enum swPublishStepOpts_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("08A46722-38F9-409D-BBFC-D4FE0CEEC0F8")
public enum swPublishStepOpts_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("08A46722-38F9-409D-BBFC-D4FE0CEEC0F8")]
__value public enum swPublishStepOpts_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("08A46722-38F9-409D-BBFC-D4FE0CEEC0F8")]
public enum class swPublishStepOpts_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swPublishStepOpts\_FaceEdgeSTEP242** | 2 = Export face/edge properties/IDs |
| **swPublishStepOpts\_None** | 0 |
| **swPublishStepOpts\_SplitFacesSTEP242** | 1 = Split features with 360 degree faces (holes, cylinders, cones) into two |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swPublishStepOpts\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
