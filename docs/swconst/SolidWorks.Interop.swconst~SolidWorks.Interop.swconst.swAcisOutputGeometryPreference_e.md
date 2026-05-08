# swAcisOutputGeometryPreference_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAcisOutputGeometryPreference_e`

ACIS output geometry types.
ACIS output geometry types.

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

<System.Runtime.InteropServices.GuidAttribute("9D5D9052-7B2D-48C9-90CE-194C0B922D84")>
Public Enum swAcisOutputGeometryPreference_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swAcisOutputGeometryPreference_e
```

```

[System.Runtime.InteropServices.Guid("9D5D9052-7B2D-48C9-90CE-194C0B922D84")]
public enum swAcisOutputGeometryPreference_e : System.Enum 
```

```

public enum swAcisOutputGeometryPreference_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("9D5D9052-7B2D-48C9-90CE-194C0B922D84")
public enum swAcisOutputGeometryPreference_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("9D5D9052-7B2D-48C9-90CE-194C0B922D84")]
__value public enum swAcisOutputGeometryPreference_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("9D5D9052-7B2D-48C9-90CE-194C0B922D84")]
public enum class swAcisOutputGeometryPreference_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAcisOutputAs3DCurves** | 1 = 3D curves without export sketch entities |
| **swAcisOutputAs3DCurves\_IncludeSketchEnts** | 2 = 3D curves with export sketch entities |
| **swAcisOutputAsSolidAndSurface** | 0 = Solid/surface geometry |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swAcisOutputGeometryPreference\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
