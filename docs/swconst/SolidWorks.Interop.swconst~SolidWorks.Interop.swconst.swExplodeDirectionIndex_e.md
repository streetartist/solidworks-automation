# swExplodeDirectionIndex_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swExplodeDirectionIndex_e`

Explode direction manipulator options when creating or editing an explode step.
Explode direction manipulator options when creating or editing an explode step.

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

<System.Runtime.InteropServices.GuidAttribute("6106A10E-B7B6-4FC7-BC59-323CA308F863")>
Public Enum swExplodeDirectionIndex_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swExplodeDirectionIndex_e
```

```

[System.Runtime.InteropServices.Guid("6106A10E-B7B6-4FC7-BC59-323CA308F863")]
public enum swExplodeDirectionIndex_e : System.Enum 
```

```

public enum swExplodeDirectionIndex_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("6106A10E-B7B6-4FC7-BC59-323CA308F863")
public enum swExplodeDirectionIndex_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("6106A10E-B7B6-4FC7-BC59-323CA308F863")]
__value public enum swExplodeDirectionIndex_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("6106A10E-B7B6-4FC7-BC59-323CA308F863")]
public enum class swExplodeDirectionIndex_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swExplodeDirectionIndex\_Unknown** | -1 = Use in [IExplodeStep::SetExplodeDirection](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~SetExplodeDirection.html) to continue using the current enumerator value |
| **swExplodeDirectionIndex\_XAxis** | 0 |
| **swExplodeDirectionIndex\_YAxis** | 1 |
| **swExplodeDirectionIndex\_ZAxis** | 2 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swExplodeDirectionIndex\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
