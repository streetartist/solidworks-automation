# swTangencyType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTangencyType_e`

Tangency options for lofts and profile twist options for sweeps.
Tangency options for lofts and profile twist options for sweeps.

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

<System.Runtime.InteropServices.GuidAttribute("1280FD1E-DC66-4EBA-8025-C0FFF060FE02")>
Public Enum swTangencyType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swTangencyType_e
```

```

[System.Runtime.InteropServices.Guid("1280FD1E-DC66-4EBA-8025-C0FFF060FE02")]
public enum swTangencyType_e : System.Enum 
```

```

public enum swTangencyType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("1280FD1E-DC66-4EBA-8025-C0FFF060FE02")
public enum swTangencyType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("1280FD1E-DC66-4EBA-8025-C0FFF060FE02")]
__value public enum swTangencyType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("1280FD1E-DC66-4EBA-8025-C0FFF060FE02")]
public enum class swTangencyType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swMinimumTwist** | 10 = Prevents the profile from becoming self-intersecting as it follows the sweep or loft path; valid only for 3D paths; corresponds to **Profile Twist > Minimum Twist** in the Sweep PropertyManager |
| **swTangencyAllFaces** | 3 = Makes the adjacent faces tangent at the profile; valid only if [swTwistControlType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTwistControlType_e.html) is set to swTwistControlFollowPath and only when attaching a sweep or loft to existing geometry; corresponds to **Profile Twist > Tangent to Adjacent Faces** in the Sweep PropertyManager |
| **swTangencyDirectionVector** | 2 = Sets a direction plane, planar face, line, edge, cylinder, axis, or a pair of vertices; valid only if [swTwistControlType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTwistControlType_e.html) is set to swTwistControlFollowPath; corresponds to **Profile Twist > Specify Direction Vector** in the Sweep PropertyManager |
| **swTangencyNone** | 0 |
| **swTangencyNormalToProfile** | 1 = Aligns the profile normal to the sweep or loft path; valid only for 2D paths; corresponds to **Profile Twist > None** in the Sweep PropertyManager |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swTangencyType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
