# swSkOffsetMakeConstructionType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSkOffsetMakeConstructionType_e`

Convert original and offset sketch entities to construction sketch entities.
Convert original and offset sketch entities to construction sketch entities.

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

<System.Runtime.InteropServices.GuidAttribute("181EE430-7224-44F4-BD9E-B302BC4117FD")>
Public Enum swSkOffsetMakeConstructionType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swSkOffsetMakeConstructionType_e
```

```

[System.Runtime.InteropServices.Guid("181EE430-7224-44F4-BD9E-B302BC4117FD")]
public enum swSkOffsetMakeConstructionType_e : System.Enum 
```

```

public enum swSkOffsetMakeConstructionType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("181EE430-7224-44F4-BD9E-B302BC4117FD")
public enum swSkOffsetMakeConstructionType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("181EE430-7224-44F4-BD9E-B302BC4117FD")]
__value public enum swSkOffsetMakeConstructionType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("181EE430-7224-44F4-BD9E-B302BC4117FD")]
public enum class swSkOffsetMakeConstructionType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSkOffsetDontMakeConstruction** | 0 = Do not the convert original or offset sketch entities to construction sketch entities |
| **swSkOffsetMakeBothConstruction** | 3 = Convert the original and offset sketch entities to construction sketch entities |
| **swSkOffsetMakeOffsConstruction** | 2 = Convert only the offset sketch entities to construction sketch entities |
| **swSkOffsetMakeOrigConstruction** | 1 = Convert only the original sketch entities to construction sketch entities |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swSkOffsetMakeConstructionType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
