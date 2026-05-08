# swSaveItemsPathError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSaveItemsPathError_e`

Error return codes for IAdvancedSaveAsOptions::ModifyItemsNameAndPath.
Error return codes for [IAdvancedSaveAsOptions::ModifyItemsNameAndPath](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~ModifyItemsNameAndPath.html).

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

<System.Runtime.InteropServices.GuidAttribute("1EE7DA29-9522-4677-BF60-1A38CA2A50BE")>
Public Enum swSaveItemsPathError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swSaveItemsPathError_e
```

```

[System.Runtime.InteropServices.Guid("1EE7DA29-9522-4677-BF60-1A38CA2A50BE")]
public enum swSaveItemsPathError_e : System.Enum 
```

```

public enum swSaveItemsPathError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("1EE7DA29-9522-4677-BF60-1A38CA2A50BE")
public enum swSaveItemsPathError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("1EE7DA29-9522-4677-BF60-1A38CA2A50BE")]
__value public enum swSaveItemsPathError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("1EE7DA29-9522-4677-BF60-1A38CA2A50BE")]
public enum class swSaveItemsPathError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSaveItemsPathError\_ArraySizeNotMatching** | 1 = Input arrays must be the same size |
| **swSaveItemsPathError\_InvalidPath** | 2 = Path provided does not exist or user does not have write access |
| **swSaveItemsPathError\_Succeeded** | 0 |
| **swSaveItemsPathError\_WrongComponentName** | 3 = Name provided is not supported by SOLIDWORKS |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swSaveItemsPathError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
