# swImageQualityShaded_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swImageQualityShaded_e`

Quality of tessellation of cylindrical surfaces for shaded rendering output.
Quality of tessellation of cylindrical surfaces for shaded rendering output.

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

<System.Runtime.InteropServices.GuidAttribute("F8CFE0B3-7BF7-4F0B-B982-6A645A0757C9")>
Public Enum swImageQualityShaded_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swImageQualityShaded_e
```

```

[System.Runtime.InteropServices.Guid("F8CFE0B3-7BF7-4F0B-B982-6A645A0757C9")]
public enum swImageQualityShaded_e : System.Enum 
```

```

public enum swImageQualityShaded_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("F8CFE0B3-7BF7-4F0B-B982-6A645A0757C9")
public enum swImageQualityShaded_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("F8CFE0B3-7BF7-4F0B-B982-6A645A0757C9")]
__value public enum swImageQualityShaded_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("F8CFE0B3-7BF7-4F0B-B982-6A645A0757C9")]
public enum class swImageQualityShaded_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swShadedImageQualityCoarse** | 1 |
| **swShadedImageQualityCustom** | 3 = Use [swUserPreferenceDoubleValue\_e.swImageQualityShadedDeviation](DP_ImageQuality.htm) to set a value for the custom shaded image quality. |
| **swShadedImageQualityFine** | 2 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swImageQualityShaded\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
