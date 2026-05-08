# swFlangeDimTypes_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFlangeDimTypes_e`

Origins for dimensioning Blind or Up To Edge And Merge flange length end conditions in edge flanges.
Origins for dimensioning Blind or Up To Edge And Merge flange length end conditions in edge flanges.

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

<System.Runtime.InteropServices.GuidAttribute("58CA96E8-FD93-491C-8DD2-40D32351232D")>
Public Enum swFlangeDimTypes_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swFlangeDimTypes_e
```

```

[System.Runtime.InteropServices.Guid("58CA96E8-FD93-491C-8DD2-40D32351232D")]
public enum swFlangeDimTypes_e : System.Enum 
```

```

public enum swFlangeDimTypes_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("58CA96E8-FD93-491C-8DD2-40D32351232D")
public enum swFlangeDimTypes_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("58CA96E8-FD93-491C-8DD2-40D32351232D")]
__value public enum swFlangeDimTypes_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("58CA96E8-FD93-491C-8DD2-40D32351232D")]
public enum class swFlangeDimTypes_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swFlangeDimTypeBendTangentArc** | 3 = Flange length is measured from the edge flange face to a line that is tangent to the bend; not valid for the Up To Edge And Merge length end condition |
| **swFlangeDimTypeInnerVirtualSharp** | 2 = Flange length is measured from the edge flange face to an inner virtual sharp (sketch point at the virtual intersection point of two sketch entities) |
| **swFlangeDimTypeOuterVirtualSharp** | 1 = Flange length is measured from the edge flange face to an outer virtual sharp (sketch point at the virtual intersection point of two sketch entities) |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swFlangeDimTypes\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
