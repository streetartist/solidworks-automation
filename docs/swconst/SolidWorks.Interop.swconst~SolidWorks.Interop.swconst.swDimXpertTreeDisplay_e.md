# swDimXpertTreeDisplay_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDimXpertTreeDisplay_e`

Types of tree display on the DimXpert tab.
Types of tree display on the DimXpert tab.

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

<System.Runtime.InteropServices.GuidAttribute("520B4921-8196-464C-A7E0-84F6E27D9B9A")>
Public Enum swDimXpertTreeDisplay_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swDimXpertTreeDisplay_e
```

```

[System.Runtime.InteropServices.Guid("520B4921-8196-464C-A7E0-84F6E27D9B9A")]
public enum swDimXpertTreeDisplay_e : System.Enum 
```

```

public enum swDimXpertTreeDisplay_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("520B4921-8196-464C-A7E0-84F6E27D9B9A")
public enum swDimXpertTreeDisplay_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("520B4921-8196-464C-A7E0-84F6E27D9B9A")]
__value public enum swDimXpertTreeDisplay_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("520B4921-8196-464C-A7E0-84F6E27D9B9A")]
public enum class swDimXpertTreeDisplay_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swDimXpertTreeDisplay\_Annotation** | 2 = Show annotation-based tree. |
| **swDimXpertTreeDisplay\_Feature** | 3 = Show feature-based tree. |
| **swDimXpertTreeDisplay\_Flat** | 1 = Show flat tree |

Remarks

The members of this enumeration correspond to the Tree Display options that are available in the right-mouse button menu for a DimXpert schema.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swDimXpertTreeDisplay\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
