# swSlicingTypes_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSlicingTypes_e`

Types of slicing. Bitmask.
Types of slicing. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("FB7EE151-A1DB-406E-9677-4F785123EDC2")>
Public Enum swSlicingTypes_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swSlicingTypes_e
```

```

[System.Runtime.InteropServices.Guid("FB7EE151-A1DB-406E-9677-4F785123EDC2")]
public enum swSlicingTypes_e : System.Enum 
```

```

public enum swSlicingTypes_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("FB7EE151-A1DB-406E-9677-4F785123EDC2")
public enum swSlicingTypes_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("FB7EE151-A1DB-406E-9677-4F785123EDC2")]
__value public enum swSlicingTypes_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("FB7EE151-A1DB-406E-9677-4F785123EDC2")]
public enum class swSlicingTypes_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSlicingTypes\_Circle** | 4 = Creates a circle whose diameter equals the average of the length and width of the rectangle that encloses all the sketch entities; circle is located at the intersection of the source geometry and the slicing plane |
| **swSlicingTypes\_Exact** | 2 = Creates an exact intersection of the mesh BREP body and graphics body resulting in a polyline; set only if swSlicingTypes\_Intersection is also set; not valid with swSlicingTypes\_Circle and swSlicingTypes\_Rectangle |
| **swSlicingTypes\_Intersection** | 1 = For SOLIDWORKS BREP geometry, the slicing is identical to what is generated using the Intersection Curve tool; for mesh BREP and graphics bodies, sketches generated cannot be modified |
| **swSlicingTypes\_None** | 0 |
| **swSlicingTypes\_Rectangle** | 8 = Creates a rectangle that encloses all the sketch entities and is located at the intersection of the source geometry and the slicing plane |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swSlicingTypes\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
