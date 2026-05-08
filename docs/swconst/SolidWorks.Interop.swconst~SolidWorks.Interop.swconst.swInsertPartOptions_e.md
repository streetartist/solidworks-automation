# swInsertPartOptions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInsertPartOptions_e`

Part insertion options. Bitmask.
Part insertion options. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("8F7BC8B1-D100-4A71-908D-5CE26B17C420")>
Public Enum swInsertPartOptions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swInsertPartOptions_e
```

```

[System.Runtime.InteropServices.Guid("8F7BC8B1-D100-4A71-908D-5CE26B17C420")]
public enum swInsertPartOptions_e : System.Enum 
```

```

public enum swInsertPartOptions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("8F7BC8B1-D100-4A71-908D-5CE26B17C420")
public enum swInsertPartOptions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("8F7BC8B1-D100-4A71-908D-5CE26B17C420")]
__value public enum swInsertPartOptions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("8F7BC8B1-D100-4A71-908D-5CE26B17C420")]
public enum class swInsertPartOptions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swInsertPartBreakLink** | 512 or 0x200 |
| **swInsertPartDontZoomAll** | 262144 or 0x40000 |
| **swInsertPartImportAbsorbedSketchs** | 32 or 0x20 |
| **swInsertPartImportAxes** | 4 or 0x4 |
| **swInsertPartImportCoordinateSystem** | 256 or 0x100 |
| **swInsertPartImportCosmeticThreads** | 16 or 0x10 |
| **swInsertPartImportCustomProperties** | 128 or 0x80 |
| **swInsertPartImportCustomToCutlistProperties** | 65536 or 0x10000 |
| **swInsertPartImportCustomToFileProperties** | 32768 or 0x8000 |
| **swInsertPartImportCutListProperties** | 2048 or 0x800 |
| **swInsertPartImportDimXpertAnnotations** | 131072 or 0x20000 |
| **swInsertPartImportGraphicBodies** | 8388608 or 0x800000 |
| **swInsertPartImportHoleWzdData** | 4096 or 0x1000 |
| **swInsertPartImportIndProps** | 16384 or 0x4000 |
| **swInsertPartImportMaterial** | 524288 or 0x80000; Transfer - Body Material |
| **swInsertPartImportModelDimensions** | 1024 or 0x400 |
| **swInsertPartImportPartMaterial** | 4194304 or 0x400000; Transfer - Part Material |
| **swInsertPartImportPlanes** | 8 or 0x8 |
| **swInsertPartImportPoints** | 2097152 or 0x200000 |
| **swInsertPartImportPropagateVisualPropertiesFromOriginalPart** | 1048576 or 0x100000; Visual Properties - Propagate from original part |
| **swInsertPartImportSMInfo** | 8192 or 0x2000 |
| **swInsertPartImportSolids** | 1 or 0x1 |
| **swInsertPartImportSurfaces** | 2 or 0x2 |
| **swInsertPartImportUnabsorbedSketchs** | 64 or 0x40 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swInsertPartOptions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
