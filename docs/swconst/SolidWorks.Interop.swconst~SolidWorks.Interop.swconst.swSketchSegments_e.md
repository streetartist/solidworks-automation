# swSketchSegments_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSketchSegments_e`

Types of ISketchSegment objects.
Types of [ISketchSegment](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) objects.

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

<System.Runtime.InteropServices.GuidAttribute("C1458726-C592-4374-8A4D-2B7D26283093")>
Public Enum swSketchSegments_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swSketchSegments_e
```

```

[System.Runtime.InteropServices.Guid("C1458726-C592-4374-8A4D-2B7D26283093")]
public enum swSketchSegments_e : System.Enum 
```

```

public enum swSketchSegments_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("C1458726-C592-4374-8A4D-2B7D26283093")
public enum swSketchSegments_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("C1458726-C592-4374-8A4D-2B7D26283093")]
__value public enum swSketchSegments_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("C1458726-C592-4374-8A4D-2B7D26283093")]
public enum class swSketchSegments_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSketchARC** | 1 |
| **swSketchELLIPSE** | 2 |
| **swSketchLINE** | 0 |
| **swSketchPARABOLA** | 5 |
| **swSketchSPLINE** | 3 |
| **swSketchTEXT** | 4 |

Remarks

Based on these types, you can obtain the appropriate derived class (that is, [ISketchLine](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchLine.html), [ISketchArc](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchArc.html), and so on) and call the appropriate derived class functions.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swSketchSegments\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
