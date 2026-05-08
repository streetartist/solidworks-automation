# swMatesDefaultMisalignment_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMatesDefaultMisalignment_e`

Concentric mate misalignment options.
Concentric mate misalignment options.

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

<System.Runtime.InteropServices.GuidAttribute("9273E7B6-123F-44B4-B71A-08D8FCC756AC")>
Public Enum swMatesDefaultMisalignment_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swMatesDefaultMisalignment_e
```

```

[System.Runtime.InteropServices.Guid("9273E7B6-123F-44B4-B71A-08D8FCC756AC")]
public enum swMatesDefaultMisalignment_e : System.Enum 
```

```

public enum swMatesDefaultMisalignment_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("9273E7B6-123F-44B4-B71A-08D8FCC756AC")
public enum swMatesDefaultMisalignment_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("9273E7B6-123F-44B4-B71A-08D8FCC756AC")]
__value public enum swMatesDefaultMisalignment_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("9273E7B6-123F-44B4-B71A-08D8FCC756AC")]
public enum class swMatesDefaultMisalignment_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swMatesAlignFirstConcentricMate** | 0; Align this mate; align the mate currently being edited to be exactly concentric, causing the linked mate to be misaligned |
| **swMatesAlignSecondConcentricMate** | 1; Align linked mate; aligns the linked mate to be exactly concentric, causing the currently edited mate to be misaligned |
| **swMatesSymmetric** | 2; Symmetric; misaligns both concentric mates, splitting the deviation evenly between mates |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swMatesDefaultMisalignment\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
