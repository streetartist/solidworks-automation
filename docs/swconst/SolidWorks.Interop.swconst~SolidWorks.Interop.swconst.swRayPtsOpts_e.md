# swRayPtsOpts_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRayPtsOpts_e`

Ray points options. Bitmask.
Ray points options. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("CFB53C67-434F-49DA-BCAC-507C9E428D28")>
Public Enum swRayPtsOpts_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swRayPtsOpts_e
```

```

[System.Runtime.InteropServices.Guid("CFB53C67-434F-49DA-BCAC-507C9E428D28")]
public enum swRayPtsOpts_e : System.Enum 
```

```

public enum swRayPtsOpts_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("CFB53C67-434F-49DA-BCAC-507C9E428D28")
public enum swRayPtsOpts_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("CFB53C67-434F-49DA-BCAC-507C9E428D28")]
__value public enum swRayPtsOpts_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("CFB53C67-434F-49DA-BCAC-507C9E428D28")]
public enum class swRayPtsOpts_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swRayPtsOptsENTRY\_EXIT** | 4 or 0x4; Output requested of whether ray was entering or exiting body when it hit |
| **swRayPtsOptsNORMALS** | 1 or 0x1; Output of normals requested |
| **swRayPtsOptsTOPOLS** | 2 or 0x2; Output of entities hit requested |
| **swRayPtsOptsUNBLOCK** | 8 or 0x8; Allow the system to respond while waiting |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swRayPtsOpts\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
