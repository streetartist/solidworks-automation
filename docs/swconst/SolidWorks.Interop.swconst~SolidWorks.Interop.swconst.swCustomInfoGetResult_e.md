# swCustomInfoGetResult_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCustomInfoGetResult_e`

Result codes when getting custom properties.
Result codes when getting custom properties.

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

<System.Runtime.InteropServices.GuidAttribute("55A446F8-FA41-4B62-85E6-C174667B6C67")>
Public Enum swCustomInfoGetResult_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCustomInfoGetResult_e
```

```

[System.Runtime.InteropServices.Guid("55A446F8-FA41-4B62-85E6-C174667B6C67")]
public enum swCustomInfoGetResult_e : System.Enum 
```

```

public enum swCustomInfoGetResult_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("55A446F8-FA41-4B62-85E6-C174667B6C67")
public enum swCustomInfoGetResult_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("55A446F8-FA41-4B62-85E6-C174667B6C67")]
__value public enum swCustomInfoGetResult_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("55A446F8-FA41-4B62-85E6-C174667B6C67")]
public enum class swCustomInfoGetResult_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCustomInfoGetResult\_CachedValue** | 0 = Cached value was returned |
| **swCustomInfoGetResult\_NotPresent** | 1 = Custom property does not exist |
| **swCustomInfoGetResult\_ResolvedValue** | 2 = Resolved value was returned |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCustomInfoGetResult\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
