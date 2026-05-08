# swConcentricAlignmentType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConcentricAlignmentType_e`

Concentric mate alignment types.
Concentric mate alignment types.

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

<System.Runtime.InteropServices.GuidAttribute("B1B3AEBC-2098-4D14-9A8B-6D1081B8ACBA")>
Public Enum swConcentricAlignmentType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swConcentricAlignmentType_e
```

```

[System.Runtime.InteropServices.Guid("B1B3AEBC-2098-4D14-9A8B-6D1081B8ACBA")]
public enum swConcentricAlignmentType_e : System.Enum 
```

```

public enum swConcentricAlignmentType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("B1B3AEBC-2098-4D14-9A8B-6D1081B8ACBA")
public enum swConcentricAlignmentType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("B1B3AEBC-2098-4D14-9A8B-6D1081B8ACBA")]
__value public enum swConcentricAlignmentType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("B1B3AEBC-2098-4D14-9A8B-6D1081B8ACBA")]
public enum class swConcentricAlignmentType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swConcentricAlignConcentric** | 0; Align both mates to be exactly concentric; neither mate is misaligned |
| **swConcentricAlignLinkedMate** | 2; Align the linked mate to be exactly concentric, causing the currently edited mate to be misaligned |
| **swConcentricAlignSymmetric** | 3; Misalign both concentric mates, splitting the misalignment deviation evenly between mates |
| **swConcentricAlignThisMate** | 1; Align the mate currently being edited to be exactly concentric, causing the linked mate to be misaligned |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swConcentricAlignmentType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
