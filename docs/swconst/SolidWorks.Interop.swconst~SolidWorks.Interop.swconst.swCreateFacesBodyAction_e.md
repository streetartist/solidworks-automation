# swCreateFacesBodyAction_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCreateFacesBodyAction_e`

Options for creating missing faces on an open body.
Options for creating missing faces on an open body.

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

<System.Runtime.InteropServices.GuidAttribute("CC02444A-527E-4BC9-BF77-C368908F2145")>
Public Enum swCreateFacesBodyAction_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCreateFacesBodyAction_e
```

```

[System.Runtime.InteropServices.Guid("CC02444A-527E-4BC9-BF77-C368908F2145")]
public enum swCreateFacesBodyAction_e : System.Enum 
```

```

public enum swCreateFacesBodyAction_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("CC02444A-527E-4BC9-BF77-C368908F2145")
public enum swCreateFacesBodyAction_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("CC02444A-527E-4BC9-BF77-C368908F2145")]
__value public enum swCreateFacesBodyAction_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("CC02444A-527E-4BC9-BF77-C368908F2145")]
public enum class swCreateFacesBodyAction_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCreateFacesBodyActionCap** | 1 = Cap the missing face |
| **swCreateFacesBodyActionGrow** | 2 = Grow the missing face |
| **swCreateFacesBodyActionGrowFromParent** | 3 = Grow the missing face from the parent |
| **swCreateFacesBodyActionLeaveRubber** | 4 = Create a virtual face topological entity without any associated geometry |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCreateFacesBodyAction\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
