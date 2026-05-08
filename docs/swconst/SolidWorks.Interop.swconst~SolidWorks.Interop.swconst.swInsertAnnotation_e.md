# swInsertAnnotation_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInsertAnnotation_e`

Annotation types. Bitmask.
Annotation types. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("6609A7F9-2A3F-4FA0-82BC-41C707EF811B")>
Public Enum swInsertAnnotation_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swInsertAnnotation_e
```

```

[System.Runtime.InteropServices.Guid("6609A7F9-2A3F-4FA0-82BC-41C707EF811B")]
public enum swInsertAnnotation_e : System.Enum 
```

```

public enum swInsertAnnotation_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("6609A7F9-2A3F-4FA0-82BC-41C707EF811B")
public enum swInsertAnnotation_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("6609A7F9-2A3F-4FA0-82BC-41C707EF811B")]
__value public enum swInsertAnnotation_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("6609A7F9-2A3F-4FA0-82BC-41C707EF811B")]
public enum class swInsertAnnotation_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swInsertAxes** | 512 or 0x200 |
| **swInsertCenterOfMass** | 33554432 or 0x2000000 |
| **swInsertCThreads** | 1 or 0x1; insert annotation cosmetic threads |
| **swInsertCurves** | 1024 or 0x400 |
| **swInsertDatums** | 2 or 0x2 |
| **swInsertDatumTargets** | 4 or 0x4 |
| **swInsertDimensions** | 8 or 0x8 |
| **swInsertDimensionsMarkedForDrawing** | 32768 or 0x8000 |
| **swInsertDimensionsNotMarkedForDrawing** | 524288 or 0x80000 |
| **swInsertGTols** | 32 or 0x20; insert annotation geometric tolerances |
| **swInsertholeCallout** | 1048576 or 0x100000 |
| **swInsertHoleWizardLocationDimensions** | 131072 or 0x20000 |
| **swInsertHoleWizardProfileDimensions** | 65536 or 0x10000 |
| **swInsertInstanceCounts** | 16 or 0x10; insert dimension instance/revolution counts |
| **swInsertNotes** | 64 or 0x40 |
| **swInsertOrigins** | 16384 or 0x4000 |
| **swInsertPlanes** | 2048 or 0x800 |
| **swInsertPoints** | 8192 or 0x2000; insert routing points |
| **swInsertRefPoints** | 262144 or 0x40000; insert reference geometry points |
| **swInsertSFSymbols** | 128 or 0x80; insert annotation surface finishes |
| **swInsertSketches** | 4194304 or 0x400000 |
| **swInsertSurfaces** | 4096 or 0x1000 |
| **swInsertTolerancedDims** | 16777216 or 0x1000000 |
| **swInsertWeldBeads** | 2097152 or 0x200000; insert annotation weld bead caterpillars |
| **swInsertWeldBeads\_ET** | 8388608 or 0x800000; insert annotation weld bead end treatments |
| **swInsertWelds** | 256 or 0x100; insert annotation weld symbols |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swInsertAnnotation\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
