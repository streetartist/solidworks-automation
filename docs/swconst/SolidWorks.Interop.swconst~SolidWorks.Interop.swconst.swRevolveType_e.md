# swRevolveType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRevolveType_e`

Revolve feature types.
Revolve feature types.

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

<System.Runtime.InteropServices.GuidAttribute("5B9D8B74-3E23-446C-BDA2-7948BEA489DF")>
Public Enum swRevolveType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swRevolveType_e
```

```

[System.Runtime.InteropServices.Guid("5B9D8B74-3E23-446C-BDA2-7948BEA489DF")]
public enum swRevolveType_e : System.Enum 
```

```

public enum swRevolveType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("5B9D8B74-3E23-446C-BDA2-7948BEA489DF")
public enum swRevolveType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("5B9D8B74-3E23-446C-BDA2-7948BEA489DF")]
__value public enum swRevolveType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("5B9D8B74-3E23-446C-BDA2-7948BEA489DF")]
public enum class swRevolveType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swRevolveTypeMidPlane** | 1 = Mid-plane revolution |
| **swRevolveTypeMidPlane360Degrees** | 4 = Create revolve: mid-plane revolution with a 360-degree angle  - or -  Edit revolve: mid-plane revolution with a 360-degree angle; if you use [IRevolveFeatureData2::SetRevolutionAngle](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevolveFeatureData2~SetRevolutionAngle.html), then the 360-degree angle is overwritten |
| **swRevolveTypeOneDirection** | 0 = One-direction revolution |
| **swRevolveTypeOneDirection360Degrees** | 3 = Create revolve: one direction revolution with a 360-degree angle  - or -  Edit revolve: one direction revolution with a 360-degree angle; if you use [IRevolveFeatureData2::SetRevolutionAngle](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevolveFeatureData2~SetRevolutionAngle.html), then the 360-degree angle is overwritten |
| **swRevolveTypeTwoDirection** | 2 = Two direction revolution |
| **swRevolveTypeTwoDirection360Degrees** | 5 = Create and edit revolves: two direction revolution |

Remarks

|  |  |
| --- | --- |
| To... | Use... |
| Create revolve | [IFeatureManager::FeatureRevolve](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureRevolve.html)  [IFeatureManager::FeatureRevolveCut](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureRevolveCut.html)  [IFeatureManager::FeatureRevolveThin](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureRevolveThin.html)  [IFeatureManager::FeatureRevolveThinCut](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureRevolveThinCut.html) |
| Edit revolve | [IRevolveFeatureData2::Type](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevolveFeatureData2~Type.html) |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swRevolveType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
