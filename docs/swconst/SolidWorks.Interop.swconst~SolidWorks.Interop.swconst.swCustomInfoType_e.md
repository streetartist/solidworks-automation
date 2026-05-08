# swCustomInfoType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCustomInfoType_e`

Custom property types.
Custom property types.

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

<System.Runtime.InteropServices.GuidAttribute("0C9C7225-2AAC-41B3-8631-E3A1704AE71D")>
Public Enum swCustomInfoType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCustomInfoType_e
```

```

[System.Runtime.InteropServices.Guid("0C9C7225-2AAC-41B3-8631-E3A1704AE71D")]
public enum swCustomInfoType_e : System.Enum 
```

```

public enum swCustomInfoType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("0C9C7225-2AAC-41B3-8631-E3A1704AE71D")
public enum swCustomInfoType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("0C9C7225-2AAC-41B3-8631-E3A1704AE71D")]
__value public enum swCustomInfoType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("0C9C7225-2AAC-41B3-8631-E3A1704AE71D")]
public enum class swCustomInfoType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCustomInfoDate** | 64 = Datetime value |
| **swCustomInfoDouble** | 5 = Double value |
| **swCustomInfoEquation** | 105 = Equation value |
| **swCustomInfoNumber** | 3 = Integer value |
| **swCustomInfoText** | 30 = Text value |
| **swCustomInfoUnknown** | 0 |
| **swCustomInfoYesOrNo** | 11 = Yes or No value |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCustomInfoType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
