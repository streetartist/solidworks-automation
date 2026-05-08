# swReorderComponentsWhere_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swReorderComponentsWhere_e`

Where to move the components.
Where to move the components.

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

<System.Runtime.InteropServices.GuidAttribute("7FBDD209-9314-4882-BC7B-5E33CA8E0EBF")>
Public Enum swReorderComponentsWhere_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swReorderComponentsWhere_e
```

```

[System.Runtime.InteropServices.Guid("7FBDD209-9314-4882-BC7B-5E33CA8E0EBF")]
public enum swReorderComponentsWhere_e : System.Enum 
```

```

public enum swReorderComponentsWhere_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("7FBDD209-9314-4882-BC7B-5E33CA8E0EBF")
public enum swReorderComponentsWhere_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("7FBDD209-9314-4882-BC7B-5E33CA8E0EBF")]
__value public enum swReorderComponentsWhere_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("7FBDD209-9314-4882-BC7B-5E33CA8E0EBF")]
public enum class swReorderComponentsWhere_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swReorderComponents\_After** | 1 = Move the source components to just after the target |
| **swReorderComponents\_Before** | 2 = Move the source components to just before the target |
| **swReorderComponents\_FirstInFolder** | 4 = Move the source components into the target folder, as the first items in the folder |
| **swReorderComponents\_LastInFolder** | 3 = Move the source components into the target folder, as the last items in the folder |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swReorderComponentsWhere\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
