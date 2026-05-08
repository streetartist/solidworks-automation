# swCreateExplodeStepError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCreateExplodeStepError_e`

Return codes when creating an explode step.
Return codes when creating an explode step.

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

<System.Runtime.InteropServices.GuidAttribute("644F3882-77B6-4FF8-ADC8-F5036A9B149C")>
Public Enum swCreateExplodeStepError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCreateExplodeStepError_e
```

```

[System.Runtime.InteropServices.Guid("644F3882-77B6-4FF8-ADC8-F5036A9B149C")]
public enum swCreateExplodeStepError_e : System.Enum 
```

```

public enum swCreateExplodeStepError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("644F3882-77B6-4FF8-ADC8-F5036A9B149C")
public enum swCreateExplodeStepError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("644F3882-77B6-4FF8-ADC8-F5036A9B149C")]
__value public enum swCreateExplodeStepError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("644F3882-77B6-4FF8-ADC8-F5036A9B149C")]
public enum class swCreateExplodeStepError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCreateExplodeStepError\_EditingComponentInContext** | 6 = A component being edited in context is blocking explode step creation. |
| **swCreateExplodeStepError\_Generic** | 1 = Explode step creation failed. |
| **swCreateExplodeStepError\_InvalidRadialAxis** | 4 = A radial explode step is not allowed using the selected components. |
| **swCreateExplodeStepError\_NoComponents** | 3 = Components to move must be selected. |
| **swCreateExplodeStepError\_NoExplodeView** | 2 = An explode view must be active in the current configuration to create an explode step. |
| **swCreateExplodeStepError\_OpenExplodePMP** | 5 = The open Explode PropertyManager is blocking step creation. |
| **swCreateExplodeStepError\_Successful** | 0 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCreateExplodeStepError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
