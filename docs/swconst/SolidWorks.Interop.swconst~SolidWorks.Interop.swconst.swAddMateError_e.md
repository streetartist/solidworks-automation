# swAddMateError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAddMateError_e`

Status after adding or editing a mate.
Status after adding or editing a mate.

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

<System.Runtime.InteropServices.GuidAttribute("379F8727-E2AC-4B2F-8BA7-0FEB4737EF21")>
Public Enum swAddMateError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swAddMateError_e
```

```

[System.Runtime.InteropServices.Guid("379F8727-E2AC-4B2F-8BA7-0FEB4737EF21")]
public enum swAddMateError_e : System.Enum 
```

```

public enum swAddMateError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("379F8727-E2AC-4B2F-8BA7-0FEB4737EF21")
public enum swAddMateError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("379F8727-E2AC-4B2F-8BA7-0FEB4737EF21")]
__value public enum swAddMateError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("379F8727-E2AC-4B2F-8BA7-0FEB4737EF21")]
public enum class swAddMateError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAddMateError\_ErrorUknown** | 0 = Unknown error occurred |
| **swAddMateError\_IncorrectAlignment** | 3 = Unknown mate alignment or mate alignment is not present in [swMateAlign\_e](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMateAlign_e.md) |
| **swAddMateError\_IncorrectGearRatios** | 6 = Mate gear ratios are invalid |
| **swAddMateError\_IncorrectMateType** | 2 = Unknown mate type or mate type not present in [swMateType\_e](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMateType_e.md) |
| **swAddMateError\_IncorrectSelections** | 4 = Incorrect selections for mate |
| **swAddMateError\_NoError** | 1 = Success, no error |
| **swAddMateError\_OverDefinedAssembly** | 5 = Mate is over-defining the assembly |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swAddMateError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
