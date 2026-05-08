# swSMBendState_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSMBendState_e`

Bend state values for a sheet metal part.
Bend state values for a sheet metal part.

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

<System.Runtime.InteropServices.GuidAttribute("346EAE97-207C-4242-B684-90DC4BDB148E")>
Public Enum swSMBendState_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swSMBendState_e
```

```

[System.Runtime.InteropServices.Guid("346EAE97-207C-4242-B684-90DC4BDB148E")]
public enum swSMBendState_e : System.Enum 
```

```

public enum swSMBendState_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("346EAE97-207C-4242-B684-90DC4BDB148E")
public enum swSMBendState_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("346EAE97-207C-4242-B684-90DC4BDB148E")]
__value public enum swSMBendState_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("346EAE97-207C-4242-B684-90DC4BDB148E")]
public enum class swSMBendState_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSMBendStateFlattened** | 2 = The bends are flattened; the model is rolled back to just after a FlattenBends feature, but just before the corresponding ProcessBends feature |
| **swSMBendStateFolded** | 3 = The bends are folded; the model is rolled back to just after a FlattenBends ProcessBends feature pair |
| **swSMBendStateNone** | 0 = Not a sheet metal part; no SheetMetal features present |
| **swSMBendStateSharps** | 1 = The bends are in their sharp state; the part is rolled back to just before the first FlattenBends feature |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swSMBendState\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
