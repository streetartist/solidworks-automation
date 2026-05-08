# swRayPtsResults_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRayPtsResults_e`

Types of intersections and whether the rays are entering or exiting the body when they hit. Bitmask.
Types of intersections and whether the rays are entering or exiting the body when they hit. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("896BB66F-ED47-472D-A997-A3D76D75A794")>
Public Enum swRayPtsResults_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swRayPtsResults_e
```

```

[System.Runtime.InteropServices.Guid("896BB66F-ED47-472D-A997-A3D76D75A794")]
public enum swRayPtsResults_e : System.Enum 
```

```

public enum swRayPtsResults_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("896BB66F-ED47-472D-A997-A3D76D75A794")
public enum swRayPtsResults_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("896BB66F-ED47-472D-A997-A3D76D75A794")]
__value public enum swRayPtsResults_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("896BB66F-ED47-472D-A997-A3D76D75A794")]
public enum class swRayPtsResults_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swRayPtsResultsEDGE** | 4 or 0x4; Edge hit |
| **swRayPtsResultsENTER** | 16 or 0x10; Ray was entering body when it hit (optionally appears when swRayPtsOptsENTRY\_EXIT is specified in the options argument to [IModelDoc2::RayIntersections](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~RayIntersections.html)) |
| **swRayPtsResultsEXIT** | 32 or 0x20; Ray was exiting body when it hit (optionally appears when swRayPtsOptsENTRY\_EXIT is specified in the options argument to [IModelDoc2::RayIntersections](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~RayIntersections.html)) |
| **swRayPtsResultsFACE** | 1 or 0x1; Simple face hit |
| **swRayPtsResultsSILHOUETTE** | 2 or 0x2; Grazing face hit |
| **swRayPtsResultsUnknown** | 0 or 0x0; Unknown |
| **swRayPtsResultsVERTEX** | 8 or 0x8; Vertex hit |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swRayPtsResults\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
