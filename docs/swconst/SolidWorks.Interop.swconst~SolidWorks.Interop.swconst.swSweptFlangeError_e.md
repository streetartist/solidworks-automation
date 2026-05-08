# swSweptFlangeError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSweptFlangeError_e`

Swept flange creation errors. Bitmask.
Swept flange creation errors. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("2DAD7031-5629-4E61-AA3C-64E1E5788CD0")>
Public Enum swSweptFlangeError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swSweptFlangeError_e
```

```

[System.Runtime.InteropServices.Guid("2DAD7031-5629-4E61-AA3C-64E1E5788CD0")]
public enum swSweptFlangeError_e : System.Enum 
```

```

public enum swSweptFlangeError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("2DAD7031-5629-4E61-AA3C-64E1E5788CD0")
public enum swSweptFlangeError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("2DAD7031-5629-4E61-AA3C-64E1E5788CD0")]
__value public enum swSweptFlangeError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("2DAD7031-5629-4E61-AA3C-64E1E5788CD0")]
public enum class swSweptFlangeError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSweptFlangeError\_InvalidPath** | 2 |
| **swSweptFlangeError\_InvalidProfile** | 1 |
| **swSweptFlangeError\_InvalidSheetMetalParameters** | 8 = [ISweptFlangeFeatureData::UseMaterialSheetMetalParameters](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseMaterialSheetMetalParameters.html) and [ISweptFlangeFeatuareData::UseGaugeTable](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseGaugeTable.html) cannot both be set to true |
| **swSweptFlangeError\_None** | 0 |
| **swSweptFlangeError\_SelfIntersectingGeometry** | 4 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swSweptFlangeError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
