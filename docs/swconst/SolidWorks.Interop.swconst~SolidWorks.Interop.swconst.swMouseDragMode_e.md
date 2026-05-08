# swMouseDragMode_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMouseDragMode_e`

Current command states.
Current command states.

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

<System.Runtime.InteropServices.GuidAttribute("37E77752-3B9D-44DA-A8B7-24357A2ED88A")>
Public Enum swMouseDragMode_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swMouseDragMode_e
```

```

[System.Runtime.InteropServices.Guid("37E77752-3B9D-44DA-A8B7-24357A2ED88A")]
public enum swMouseDragMode_e : System.Enum 
```

```

public enum swMouseDragMode_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("37E77752-3B9D-44DA-A8B7-24357A2ED88A")
public enum swMouseDragMode_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("37E77752-3B9D-44DA-A8B7-24357A2ED88A")]
__value public enum swMouseDragMode_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("37E77752-3B9D-44DA-A8B7-24357A2ED88A")]
public enum class swMouseDragMode_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAssemblySmartMates** | 4 = Assembly component smartmate mode |
| **swInsertDimension** | 9 = Insert dimension mode |
| **swRollView** | 10 = Roll view mode |
| **swRotateAssemblyComponentAboutAxis** | 3 = Assembly component rotate about axis mode |
| **swRotateAssemblyComponentAboutCenter** | 2 = Assembly component rotate mode |
| **swRotateView** | 5 = View rotate mode |
| **swTranslateAssemblyComponent** | 1 = Assembly component move mode |
| **swTranslateView** | 6 = View translate mode |
| **swTurnView** | 11 = Turn view mode |
| **swZoomToAreaOfView** | 8 = View zoom-to mode |
| **swZoomView** | 7 = View zoom mode |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swMouseDragMode\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
