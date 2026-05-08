# swFeatureFillSurfaceOptions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFeatureFillSurfaceOptions_e`

Feature fill surface options. Bitmask.
Feature fill surface options. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("C9B3C166-2707-46C6-81A3-C2DC6A040138")>
Public Enum swFeatureFillSurfaceOptions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swFeatureFillSurfaceOptions_e
```

```

[System.Runtime.InteropServices.Guid("C9B3C166-2707-46C6-81A3-C2DC6A040138")]
public enum swFeatureFillSurfaceOptions_e : System.Enum 
```

```

public enum swFeatureFillSurfaceOptions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("C9B3C166-2707-46C6-81A3-C2DC6A040138")
public enum swFeatureFillSurfaceOptions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("C9B3C166-2707-46C6-81A3-C2DC6A040138")]
__value public enum swFeatureFillSurfaceOptions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("C9B3C166-2707-46C6-81A3-C2DC6A040138")]
public enum class swFeatureFillSurfaceOptions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swMergeResult** | 4 or 0x4; Corresponds to [IFillSurfaceFeatureData::Merge](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillSurfaceFeatureData~Merge.html) |
| **swOptimizeSurface** | 1 or 0x1; Optimize surface |
| **swReverseDirection** | 8 or 0x8; Corresponds to [IFillSurfaceFeatureData::ReverseDirection](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillSurfaceFeatureData~ReverseDirection.html) |
| **swReverseSurface** | 16 or 0x10; Corresponds to [IFillSurfaceFeatureData::ReverseSurface](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillSurfaceFeatureData~ReverseSurface.html) |
| **swTryToFormSolid** | 2 or 0x2; Corresponds to [IFillSurfaceFeatureData::TryToFormSolid](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillSurfaceFeatureData~TryToFormSolid.html) |

Remarks

Some options might not work because the topology of the surface fill to be created might not permit them. In these cases, the options are ignored.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swFeatureFillSurfaceOptions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
