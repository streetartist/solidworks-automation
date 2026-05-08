# swGtolTolType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGtolTolType_e`

Tolerance zone types in Gtol frame boxes.
Tolerance zone types in Gtol frame boxes.

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

<System.Runtime.InteropServices.GuidAttribute("B4CF6AB4-6711-4DD6-B56C-1D6F619B412A")>
Public Enum swGtolTolType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swGtolTolType_e
```

```

[System.Runtime.InteropServices.Guid("B4CF6AB4-6711-4DD6-B56C-1D6F619B412A")]
public enum swGtolTolType_e : System.Enum 
```

```

public enum swGtolTolType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("B4CF6AB4-6711-4DD6-B56C-1D6F619B412A")
public enum swGtolTolType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("B4CF6AB4-6711-4DD6-B56C-1D6F619B412A")]
__value public enum swGtolTolType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("B4CF6AB4-6711-4DD6-B56C-1D6F619B412A")]
public enum class swGtolTolType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swGtolTolType\_MAX** | 5 = Specifies a maximum value for a material condition that has already been specified as a modifier of the tolerance in the Gtol; this maximum upper tolerance is typically specified in the Tolerance 2 box with "MAX" |
| **swGtolTolType\_None** | 0 |
| **swGtolTolType\_ProjectedTolerance** | 2 = Applies to holes in which a pin, stud, or screw is to be inserted; controls the perpendicularity of the hole to the extent of the projection from the hole; specified with a circle-P symbol; typically a height is also specified in a separate field |
| **swGtolTolType\_Square** | 3 |
| **swGtolTolType\_UnequallyDisposedProfile** | 4 = Indicates that the profile of a surface tolerance is not symmetrical about the true profile; the value following the circle-U symbol is the amount of the tolerance that is in a direction that would allow additional material to be added to the true profile |
| **swGtolTolType\_Unknown** | 1 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swGtolTolType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
