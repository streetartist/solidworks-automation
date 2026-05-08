# swCornerTreatmentTrimType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerTreatmentTrimType_e`

Structure system corner treatment trim types.
Structure system corner treatment trim types.

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

<System.Runtime.InteropServices.GuidAttribute("7297913D-8F53-48D4-A1C4-63B4964DDB84")>
Public Enum swCornerTreatmentTrimType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCornerTreatmentTrimType_e
```

```

[System.Runtime.InteropServices.Guid("7297913D-8F53-48D4-A1C4-63B4964DDB84")]
public enum swCornerTreatmentTrimType_e : System.Enum 
```

```

public enum swCornerTreatmentTrimType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("7297913D-8F53-48D4-A1C4-63B4964DDB84")
public enum swCornerTreatmentTrimType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("7297913D-8F53-48D4-A1C4-63B4964DDB84")]
__value public enum swCornerTreatmentTrimType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("7297913D-8F53-48D4-A1C4-63B4964DDB84")]
public enum class swCornerTreatmentTrimType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCornerTreatmentTrim\_BodyTrim** | 1 = Conforms the intersecting member to the shape of adjacent faces by adding or removing material according to trim order |
| **swCornerTreatmentTrim\_MiterTrim** | 2 = Trims the members at a 45 degree angle; valid only for two member corner treatments |
| **swCornerTreatmentTrim\_PlanarTrim** | 0 = Cuts the intersecting member with a plane using first contact or full contact trim |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCornerTreatmentTrimType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
