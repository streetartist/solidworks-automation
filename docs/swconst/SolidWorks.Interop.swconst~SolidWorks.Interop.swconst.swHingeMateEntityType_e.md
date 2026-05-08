# swHingeMateEntityType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swHingeMateEntityType_e`

Hinge mate entity types.
Hinge mate entity types.

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

<System.Runtime.InteropServices.GuidAttribute("BE32FCE6-6CCD-4C45-AAED-025FE83E6F32")>
Public Enum swHingeMateEntityType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swHingeMateEntityType_e
```

```

[System.Runtime.InteropServices.Guid("BE32FCE6-6CCD-4C45-AAED-025FE83E6F32")]
public enum swHingeMateEntityType_e : System.Enum 
```

```

public enum swHingeMateEntityType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("BE32FCE6-6CCD-4C45-AAED-025FE83E6F32")
public enum swHingeMateEntityType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("BE32FCE6-6CCD-4C45-AAED-025FE83E6F32")]
__value public enum swHingeMateEntityType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("BE32FCE6-6CCD-4C45-AAED-025FE83E6F32")]
public enum class swHingeMateEntityType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swHingeMateEntityType\_Angle** | 2 = Select two faces to define the extent of angular rotation |
| **swHingeMateEntityType\_Coincident** | 1 = Select two coincident entities:   - a plane or planar face - another plane, planar face, edge, or point |
| **swHingeMateEntityType\_Concentric** | 0 = Select two concentric entities; valid selections are the same as for concentric mates |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swHingeMateEntityType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
