# swRotationAxisIndex_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRotationAxisIndex_e`

Rotation ring manipulator options when creating or editing an explode step.
Rotation ring manipulator options when creating or editing an explode step.

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

<System.Runtime.InteropServices.GuidAttribute("66A07AB5-6B62-4827-AEA7-0E8AABA37F21")>
Public Enum swRotationAxisIndex_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swRotationAxisIndex_e
```

```

[System.Runtime.InteropServices.Guid("66A07AB5-6B62-4827-AEA7-0E8AABA37F21")]
public enum swRotationAxisIndex_e : System.Enum 
```

```

public enum swRotationAxisIndex_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("66A07AB5-6B62-4827-AEA7-0E8AABA37F21")
public enum swRotationAxisIndex_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("66A07AB5-6B62-4827-AEA7-0E8AABA37F21")]
__value public enum swRotationAxisIndex_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("66A07AB5-6B62-4827-AEA7-0E8AABA37F21")]
public enum class swRotationAxisIndex_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swRotationAxisIndex\_Unknown** | -1 = Use in [IExplodeStep::SetRotationAxis](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~SetRotationAxis.html) to continue using the current enumerator value |
| **swRotationAxisIndex\_XYRing** | 0 |
| **swRotationAxisIndex\_YZRing** | 1 |
| **swRotationAxisIndex\_ZXRing** | 2 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swRotationAxisIndex\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
