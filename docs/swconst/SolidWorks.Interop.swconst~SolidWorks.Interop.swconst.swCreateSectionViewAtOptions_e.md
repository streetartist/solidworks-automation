# swCreateSectionViewAtOptions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCreateSectionViewAtOptions_e`

Options that affect the section view that is created. Bitmask.
Options that affect the section view that is created. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("F70C155D-CDC5-41A7-AE1D-5D57F8361CA6")>
Public Enum swCreateSectionViewAtOptions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCreateSectionViewAtOptions_e
```

```

[System.Runtime.InteropServices.Guid("F70C155D-CDC5-41A7-AE1D-5D57F8361CA6")]
public enum swCreateSectionViewAtOptions_e : System.Enum 
```

```

public enum swCreateSectionViewAtOptions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("F70C155D-CDC5-41A7-AE1D-5D57F8361CA6")
public enum swCreateSectionViewAtOptions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("F70C155D-CDC5-41A7-AE1D-5D57F8361CA6")]
__value public enum swCreateSectionViewAtOptions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("F70C155D-CDC5-41A7-AE1D-5D57F8361CA6")]
public enum class swCreateSectionViewAtOptions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCreateSectionView\_ChangeDirection** | 4 or 0x4; If set, then the direction of this section view is switched; if not set, then the direction of this section view is not switched |
| **swCreateSectionView\_CutSurfaceBodies** | 128 or 0x80: If set, then shows only the intersecting line of a surface in a section view |
| **swCreateSectionView\_DisplaySurfaceCut** | 32 or 0x20; If set, then only the surfaces cut by the section line apear in the section view; if not set, then all model surfaces appear in the section view |
| **swCreateSectionView\_ExcludeFasteners** | 64 or 0x40; If set, then fasteners are not included in the section view; if not set, then fasteners are included in the section view |
| **swCreateSectionView\_NotAligned** | 1 or 0x1; If set, then the section does not snap into alignment with the parent view; if not set, then the section snaps into alignment with the parent view |
| **swCreateSectionView\_OffsetSection** | 2 or 0x2; If set, then an aligned section view is created (two lines at an angle); if not set, a normal projection section view is created |
| **swCreateSectionView\_Partial** | 16 or 0x10; If set, then a partial section view is created; if not set, then a complete section view is created |
| **swCreateSectionView\_ScaleWithModel** | 8 or 0x8; If set, then the section view is scaled with the model; if not set, then the section view is not scaled with the model |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCreateSectionViewAtOptions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
