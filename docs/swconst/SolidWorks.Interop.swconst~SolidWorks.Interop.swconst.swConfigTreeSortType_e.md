# swConfigTreeSortType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConfigTreeSortType_e`

Order in which configurations are listed in the ConfigurationManager.
Order in which configurations are listed in the ConfigurationManager.

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

<System.Runtime.InteropServices.GuidAttribute("2F9E37D6-55AA-4FC0-B7DD-9AD3AD327AA9")>
Public Enum swConfigTreeSortType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swConfigTreeSortType_e
```

```

[System.Runtime.InteropServices.Guid("2F9E37D6-55AA-4FC0-B7DD-9AD3AD327AA9")]
public enum swConfigTreeSortType_e : System.Enum 
```

```

public enum swConfigTreeSortType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("2F9E37D6-55AA-4FC0-B7DD-9AD3AD327AA9")
public enum swConfigTreeSortType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("2F9E37D6-55AA-4FC0-B7DD-9AD3AD327AA9")]
__value public enum swConfigTreeSortType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("2F9E37D6-55AA-4FC0-B7DD-9AD3AD327AA9")]
public enum class swConfigTreeSortType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSortType\_DesignTable** | 3 = Order of the configurations in the ConfigurationManager is dictated by the order of the configurations in the design table |
| **swSortType\_History** | 0 = Order of the configurations in the ConfigurationManager is dictated by the date the configuration was created, from earliest created at the top of the list to most recently created at the bottom of the list |
| **swSortType\_Literal** | 2 = Order of the configurations in the ConfigurationManager is alphabetical |
| **swSortType\_Numeric** | 1 = Order of the configurations in the ConfigurationManager is by ascending alpha or numeric value |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swConfigTreeSortType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
