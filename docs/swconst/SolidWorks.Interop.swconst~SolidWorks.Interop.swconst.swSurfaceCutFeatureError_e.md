# swSurfaceCutFeatureError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSurfaceCutFeatureError_e`

Types of surface-cut errors.
Types of surface-cut errors.

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

<System.Runtime.InteropServices.GuidAttribute("600F1F1C-B685-4FBA-A84C-A09C3630A975")>
Public Enum swSurfaceCutFeatureError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swSurfaceCutFeatureError_e
```

```

[System.Runtime.InteropServices.Guid("600F1F1C-B685-4FBA-A84C-A09C3630A975")]
public enum swSurfaceCutFeatureError_e : System.Enum 
```

```

public enum swSurfaceCutFeatureError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("600F1F1C-B685-4FBA-A84C-A09C3630A975")
public enum swSurfaceCutFeatureError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("600F1F1C-B685-4FBA-A84C-A09C3630A975")]
__value public enum swSurfaceCutFeatureError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("600F1F1C-B685-4FBA-A84C-A09C3630A975")]
public enum class swSurfaceCutFeatureError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSurfaceCutFeatureError\_BodiesNotSpecified** | 1 = No bodies specified to cut |
| **swSurfaceCutFeatureError\_InvalidVariant** | 2 = Array passed to [IFeatureManager::InsertCutSurface](ms-help://SolidWorks.Interop.sldworks/SolidWorks/solidworks.interop.sldworks~solidworks.interop.sldworks.IfeatureManager~InsertCutSurface.html) must contain only [body objects](ms-help://SolidWorks.Interop.sldworks/SolidWorks/solidworks.interop.sldworks~solidworks.interop.sldworks.IBody2.html) |
| **swSurfaceCutFeatureError\_NoError** | 0 = No error |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swSurfaceCutFeatureError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
