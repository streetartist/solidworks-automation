# swFlangeOffsetTypes_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFlangeOffsetTypes_e`

End conditions for both flange length and flange position offset for sheet metal edge and base flanges.
End conditions for both flange length and flange position offset for sheet metal edge and base flanges.

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

<System.Runtime.InteropServices.GuidAttribute("962ABD57-5145-4A20-95C1-15E8B0982D7A")>
Public Enum swFlangeOffsetTypes_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swFlangeOffsetTypes_e
```

```

[System.Runtime.InteropServices.Guid("962ABD57-5145-4A20-95C1-15E8B0982D7A")]
public enum swFlangeOffsetTypes_e : System.Enum 
```

```

public enum swFlangeOffsetTypes_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("962ABD57-5145-4A20-95C1-15E8B0982D7A")
public enum swFlangeOffsetTypes_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("962ABD57-5145-4A20-95C1-15E8B0982D7A")]
__value public enum swFlangeOffsetTypes_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("962ABD57-5145-4A20-95C1-15E8B0982D7A")]
public enum class swFlangeOffsetTypes_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swFlangeOffsetBlind** | 1 = Positions the edge flange based on the length and direction you specify |
| **swFlangeOffsetFromSurface** | 4 |
| **swFlangeOffsetMidPlane** | 5 |
| **swFlangeOffsetUptoEdgeAndMerge** | 6 = Creates the edge flange in a multibody part by merging a selected edge on one body with an Up To reference edge on the second body |
| **swFlangeOffsetUpToSurface** | 3 |
| **swFlangeOffsetUpToVertex** | 2 = Positions the edge flange up to a specified vertex; for flange length, the selected vertex may be either on a plane that is normal to the end face of the edge flange or on a plane that is parallel to the face of the base flange |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swFlangeOffsetTypes\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
