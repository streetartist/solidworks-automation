# swFilletOverFlowType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFilletOverFlowType_e`

Fillet overflow types.
Fillet overflow types.

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

<System.Runtime.InteropServices.GuidAttribute("24812B11-4ADE-4B8B-BA35-9867E4398175")>
Public Enum swFilletOverFlowType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swFilletOverFlowType_e
```

```

[System.Runtime.InteropServices.Guid("24812B11-4ADE-4B8B-BA35-9867E4398175")]
public enum swFilletOverFlowType_e : System.Enum 
```

```

public enum swFilletOverFlowType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("24812B11-4ADE-4B8B-BA35-9867E4398175")
public enum swFilletOverFlowType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("24812B11-4ADE-4B8B-BA35-9867E4398175")]
__value public enum swFilletOverFlowType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("24812B11-4ADE-4B8B-BA35-9867E4398175")]
public enum class swFilletOverFlowType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swFilletOverFlowType\_Default** | 0 = Default; system picks the appropriate method to create a fillet when the fillet surface overflows to adjacent surfaces; it either smoothly blends with adjacent surfaces or limits the fillet surface with the adjacent edges, thereby not changing the edge, or trims the fillet surface by the adjacent surface onto which the fillet overflows; the method actually used by default depending on the geometric condition; this option always tries to create a fillet if possible |
| **swFilletOverFlowType\_KeepEdge** | 1 = Edges that are overflowed by the fillet are not modified; the fillet surface is trimmed by all the adjacent edges; as a result, an additional transition fillet surface might be needed to complete the fillet |
| **swFilletOverFlowType\_KeepSurface** | 2 = Fillet surface is either merged with the adjacent surfaces smoothly or trimmed by the adjacent surfaces; as a result, it is unlikely that an additional transition fillet surface is created |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swFilletOverFlowType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
