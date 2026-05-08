# swCollisionGroupApplyTransformErrors_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCollisionGroupApplyTransformErrors_e`

Errors when applying transforms to collision groups.
Errors when applying transforms to collision groups.

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

<System.Runtime.InteropServices.GuidAttribute("39D329E9-FE38-4BAE-BA05-DD57B4A3A983")>
Public Enum swCollisionGroupApplyTransformErrors_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCollisionGroupApplyTransformErrors_e
```

```

[System.Runtime.InteropServices.Guid("39D329E9-FE38-4BAE-BA05-DD57B4A3A983")]
public enum swCollisionGroupApplyTransformErrors_e : System.Enum 
```

```

public enum swCollisionGroupApplyTransformErrors_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("39D329E9-FE38-4BAE-BA05-DD57B4A3A983")
public enum swCollisionGroupApplyTransformErrors_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("39D329E9-FE38-4BAE-BA05-DD57B4A3A983")]
__value public enum swCollisionGroupApplyTransformErrors_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("39D329E9-FE38-4BAE-BA05-DD57B4A3A983")]
public enum class swCollisionGroupApplyTransformErrors_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCollisionGroupApplyTransformErrors\_GroupRemoved** | 3 = The specified collision group is no longer available |
| **swCollisionGroupApplyTransformErrors\_InvalidTransforms** | 2 = Array of transforms contains a null pointer for one or more elements or a pointer to an object other than an [IMathTransform](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.html) |
| **swCollisionGroupApplyTransformErrors\_None** | 0 |
| **swCollisionGroupApplyTransformErrors\_SizeMismatch** | 1 = Array of transforms does not contain one [IMathTransform](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.html) for each component in the collision group |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCollisionGroupApplyTransformErrors\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
