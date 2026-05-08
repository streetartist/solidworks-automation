# swTolerances_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTolerances_e`

Tolerance types.
Tolerance types.

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

<System.Runtime.InteropServices.GuidAttribute("00860169-2A5E-4FCF-B8D1-516FB29BC74B")>
Public Enum swTolerances_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swTolerances_e
```

```

[System.Runtime.InteropServices.Guid("00860169-2A5E-4FCF-B8D1-516FB29BC74B")]
public enum swTolerances_e : System.Enum 
```

```

public enum swTolerances_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("00860169-2A5E-4FCF-B8D1-516FB29BC74B")
public enum swTolerances_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("00860169-2A5E-4FCF-B8D1-516FB29BC74B")]
__value public enum swTolerances_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("00860169-2A5E-4FCF-B8D1-516FB29BC74B")]
public enum class swTolerances_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swBSCurveNonRationalOutputTol** | 1 = 3D nonrational b-spline curve output tolerance (meters) |
| **swBSCurveOutputTol** | 0 = 3D b-spline curve output tolerance (meters) |
| **swCurveChordTessellationTol** | 5 = Chord tolerance or deviation for tessellation for curves |
| **swSurfAngularTessellationTol** | 4 = Angular tolerance or deviation for tessellation for surfaces |
| **swSurfChordTessellationTol** | 3 = Chord tolerance or deviation for tessellation for surfaces |
| **swUVCurveOutputTol** | 2 = 2D trim curve output tolerance (fraction of characteristic minimum face dimension) |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swTolerances\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
