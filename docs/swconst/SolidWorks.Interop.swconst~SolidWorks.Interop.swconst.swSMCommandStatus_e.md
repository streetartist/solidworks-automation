# swSMCommandStatus_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSMCommandStatus_e`

Return conditions for various sheet metal APIs that attempt to do set operations.
Return conditions for various sheet metal APIs that attempt to do set operations.

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

<System.Runtime.InteropServices.GuidAttribute("6CE4987B-522F-4A46-8CBF-1FC48DE4A1A3")>
Public Enum swSMCommandStatus_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swSMCommandStatus_e
```

```

[System.Runtime.InteropServices.Guid("6CE4987B-522F-4A46-8CBF-1FC48DE4A1A3")]
public enum swSMCommandStatus_e : System.Enum 
```

```

public enum swSMCommandStatus_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("6CE4987B-522F-4A46-8CBF-1FC48DE4A1A3")
public enum swSMCommandStatus_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("6CE4987B-522F-4A46-8CBF-1FC48DE4A1A3")]
__value public enum swSMCommandStatus_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("6CE4987B-522F-4A46-8CBF-1FC48DE4A1A3")]
public enum class swSMCommandStatus_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSMErrorInvalidBendState** | 4 = Failed, an invalid bend state was specified |
| **swSMErrorNone** | 0 = Successful, operation completed |
| **swSMErrorNotAPart** | 2 = Failed, sheet metal commands only apply to SOLIDWORKS parts |
| **swSMErrorNotASheetMetalPart** | 3 = Failed, the part contains no sheet metal features |
| **swSMErrorUnknown** | 1 = Failed, for an unknown reason |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swSMCommandStatus\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
