# swSketchCheckFeatureProfileUsage_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSketchCheckFeatureProfileUsage_e`

Types of features to check to see if this sketch is valid for use in creating the specified feature.
Types of features to check to see if this sketch is valid for use in creating the specified feature.

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

<System.Runtime.InteropServices.GuidAttribute("4C9E5A28-6466-49B1-86D9-7596E6023559")>
Public Enum swSketchCheckFeatureProfileUsage_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swSketchCheckFeatureProfileUsage_e
```

```

[System.Runtime.InteropServices.Guid("4C9E5A28-6466-49B1-86D9-7596E6023559")]
public enum swSketchCheckFeatureProfileUsage_e : System.Enum 
```

```

public enum swSketchCheckFeatureProfileUsage_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("4C9E5A28-6466-49B1-86D9-7596E6023559")
public enum swSketchCheckFeatureProfileUsage_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("4C9E5A28-6466-49B1-86D9-7596E6023559")]
__value public enum swSketchCheckFeatureProfileUsage_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("4C9E5A28-6466-49B1-86D9-7596E6023559")]
public enum class swSketchCheckFeatureProfileUsage_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSketchCheckFeature\_BASEEXTRUDE** | 1 |
| **swSketchCheckFeature\_BASEEXTRUDETHIN** | 2 |
| **swSketchCheckFeature\_BASEREVOLVE** | 6 |
| **swSketchCheckFeature\_BASEREVOLVETHIN** | 7 |
| **swSketchCheckFeature\_BOSSEXTRUDE** | 3 |
| **swSketchCheckFeature\_BOSSEXTRUDETHIN** | 4 |
| **swSketchCheckFeature\_BOSSREVOLVE** | 8 |
| **swSketchCheckFeature\_BOSSREVOLVETHIN** | 9 |
| **swSketchCheckFeature\_CUTEXTRUDE** | 11 |
| **swSketchCheckFeature\_CUTEXTRUDETHIN** | 12 |
| **swSketchCheckFeature\_CUTREVOLVE** | 13 |
| **swSketchCheckFeature\_CUTREVOLVETHIN** | 14 |
| **swSketchCheckFeature\_LOFTGUIDE** | 20 |
| **swSketchCheckFeature\_LOFTSECTION** | 18 |
| **swSketchCheckFeature\_MOLD\_PARTINGSURFACES** | 23 |
| **swSketchCheckFeature\_RIBSECTION** | 21 |
| **swSketchCheckFeature\_SHEETMETAL\_BASEFLANGE** | 22 |
| **swSketchCheckFeature\_SURFACEEXTRUDE** | 5 |
| **swSketchCheckFeature\_SURFACELOFTSECTION** | 19 |
| **swSketchCheckFeature\_SURFACEREVOLVE** | 10 |
| **swSketchCheckFeature\_SURFACESWEEPSECTION** | 16 |
| **swSketchCheckFeature\_SWEEPPATHORGUIDE** | 17 |
| **swSketchCheckFeature\_SWEEPSECTION** | 15 |
| **swSketchCheckFeature\_UNSET** | 0 = Check for things that are wrong in any feature usage |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swSketchCheckFeatureProfileUsage\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
