# swMirrorPartOptions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMirrorPartOptions_e`

Options for creating a mirror part. Bitmask.
Options for creating a mirror part. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("3C451CE0-B6DF-47A7-B699-D258D802CFDB")>
Public Enum swMirrorPartOptions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swMirrorPartOptions_e
```

```

[System.Runtime.InteropServices.Guid("3C451CE0-B6DF-47A7-B699-D258D802CFDB")]
public enum swMirrorPartOptions_e : System.Enum 
```

```

public enum swMirrorPartOptions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("3C451CE0-B6DF-47A7-B699-D258D802CFDB")
public enum swMirrorPartOptions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("3C451CE0-B6DF-47A7-B699-D258D802CFDB")]
__value public enum swMirrorPartOptions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("3C451CE0-B6DF-47A7-B699-D258D802CFDB")]
public enum class swMirrorPartOptions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swMirrorPartOptions\_ImportAbsorbedSketchs** | 32 or 0x20 |
| **swMirrorPartOptions\_ImportAxes** | 4 or 0x4 |
| **swMirrorPartOptions\_ImportBodyMaterial** | 32768 or 0x8000 |
| **swMirrorPartOptions\_ImportCoordinateSystem** | 256 or 0x100 |
| **swMirrorPartOptions\_ImportCosmeticThreads** | 16 or 0x10 |
| **swMirrorPartOptions\_ImportCustomProperties** | 128 or 0x80 |
| **swMirrorPartOptions\_ImportCutListProperties** | 2048 or 0x800 |
| **swMirrorPartOptions\_ImportDimXpertAnnotations** | 16384 or 0x4000 |
| **swMirrorPartOptions\_ImportHoleWizardData** | 1024 or 0x400 |
| **swMirrorPartOptions\_ImportIndProps** | 8192 or 0x2000 = Lets you edit the sheet-metal definition in the mirrored part, which updates the cut-list properties |
| **swMirrorPartOptions\_ImportModelDimensions** | 512 or 0x200 |
| **swMirrorPartOptions\_ImportPartMaterial** | 65536 or 0x10000 |
| **swMirrorPartOptions\_ImportPlanes** | 8 or 0x8 |
| **swMirrorPartOptions\_ImportSMInfo** | 4096 or 0x1000 = Transfers the sheet-metal and flat-pattern information from the original part to the mirrored part; e.g., fixed face, grain direction, bendlines, and bounding box |
| **swMirrorPartOptions\_ImportSolids** | 1 or 0x1 |
| **swMirrorPartOptions\_ImportSurfaces** | 2 or 0x2 |
| **swMirrorPartOptions\_ImportUnabsorbedSketchs** | 64 or 0x40 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swMirrorPartOptions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
