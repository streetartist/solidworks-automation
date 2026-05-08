# swManipulatorOptions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swManipulatorOptions_e`

Manipulator options. Bitmask.
Manipulator options. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("8C01A23A-3603-454A-A8B9-DB86A2B5AB42")>
Public Enum swManipulatorOptions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swManipulatorOptions_e
```

```

[System.Runtime.InteropServices.Guid("8C01A23A-3603-454A-A8B9-DB86A2B5AB42")]
public enum swManipulatorOptions_e : System.Enum 
```

```

public enum swManipulatorOptions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("8C01A23A-3603-454A-A8B9-DB86A2B5AB42")
public enum swManipulatorOptions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("8C01A23A-3603-454A-A8B9-DB86A2B5AB42")]
__value public enum swManipulatorOptions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("8C01A23A-3603-454A-A8B9-DB86A2B5AB42")]
public enum class swManipulatorOptions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swManipulatorOpts\_Default** | 0 or 0x0; Manipulators created using the SOLIDWORKS API are deleted when a component is modified or deleted in the context of an assembly  **NOTE:** This is the default behavior. |
| **swManipulatorOpts\_KeepAfterComponentModify** | 1 or 0x1; Manipulators are not deleted when a component is modified or deleted in the context of an assembly |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swManipulatorOptions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
