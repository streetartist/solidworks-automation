# swComponentResolveStatus_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swComponentResolveStatus_e`

States for resolving components.
States for resolving components.

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

<System.Runtime.InteropServices.GuidAttribute("E1A295CC-A16D-4C95-927D-B6B8A02197A1")>
Public Enum swComponentResolveStatus_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swComponentResolveStatus_e
```

```

[System.Runtime.InteropServices.Guid("E1A295CC-A16D-4C95-927D-B6B8A02197A1")]
public enum swComponentResolveStatus_e : System.Enum 
```

```

public enum swComponentResolveStatus_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("E1A295CC-A16D-4C95-927D-B6B8A02197A1")
public enum swComponentResolveStatus_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("E1A295CC-A16D-4C95-927D-B6B8A02197A1")]
__value public enum swComponentResolveStatus_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("E1A295CC-A16D-4C95-927D-B6B8A02197A1")]
public enum class swComponentResolveStatus_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swResolveAbortedByUser** | 1 = User aborted resolving the components |
| **swResolveError** | 3 = Not used |
| **swResolveNotPerformed** | 2 = Some of the components did not get resolved despite the user requesting it |
| **swResolveOk** | 0 = Components resolved okay |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swComponentResolveStatus\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
