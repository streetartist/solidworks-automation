# swMirrorComponentMirrorType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMirrorComponentMirrorType_e`

Mirror positions for mirroring components.
Mirror positions for mirroring components.

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

<System.Runtime.InteropServices.GuidAttribute("324ADDD1-43DA-4E10-B532-EDE0389BE4F5")>
Public Enum swMirrorComponentMirrorType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swMirrorComponentMirrorType_e
```

```

[System.Runtime.InteropServices.Guid("324ADDD1-43DA-4E10-B532-EDE0389BE4F5")]
public enum swMirrorComponentMirrorType_e : System.Enum 
```

```

public enum swMirrorComponentMirrorType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("324ADDD1-43DA-4E10-B532-EDE0389BE4F5")
public enum swMirrorComponentMirrorType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("324ADDD1-43DA-4E10-B532-EDE0389BE4F5")]
__value public enum swMirrorComponentMirrorType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("324ADDD1-43DA-4E10-B532-EDE0389BE4F5")]
public enum class swMirrorComponentMirrorType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swMirrorType\_CenterOfBoundingBox** | 0 = Positions the mirror so that the center of a bounding box for the selected components is mirrored about the mirror plane |
| **swMirrorType\_CenterOfMass** | 1 = Positions the mirror so that the center of mass of the selected components is mirrored about the mirror plane |
| **swMirrorType\_ComponentOrigin** | 2 = Positions the mirror so that the component origins are mirrored about the mirror plane |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swMirrorComponentMirrorType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
