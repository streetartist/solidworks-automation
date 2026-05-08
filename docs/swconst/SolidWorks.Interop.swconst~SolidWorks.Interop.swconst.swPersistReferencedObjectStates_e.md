# swPersistReferencedObjectStates_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPersistReferencedObjectStates_e`

Object codes for objects' persistent reference IDs. Bitmask.
Object codes for objects' persistent reference IDs. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("56FAA591-44B8-441E-B634-E269F9A044C0")>
Public Enum swPersistReferencedObjectStates_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swPersistReferencedObjectStates_e
```

```

[System.Runtime.InteropServices.Guid("56FAA591-44B8-441E-B634-E269F9A044C0")]
public enum swPersistReferencedObjectStates_e : System.Enum 
```

```

public enum swPersistReferencedObjectStates_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("56FAA591-44B8-441E-B634-E269F9A044C0")
public enum swPersistReferencedObjectStates_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("56FAA591-44B8-441E-B634-E269F9A044C0")]
__value public enum swPersistReferencedObjectStates_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("56FAA591-44B8-441E-B634-E269F9A044C0")]
public enum class swPersistReferencedObjectStates_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swPersistReferencedObject\_Deleted** | 4 or 0x4 |
| **swPersistReferencedObject\_Invalid** | 1 or 0x1 |
| **swPersistReferencedObject\_Ok** | 0 or 0x0 |
| **swPersistReferencedObject\_Suppressed** | 2 or 0x2 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swPersistReferencedObjectStates\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
