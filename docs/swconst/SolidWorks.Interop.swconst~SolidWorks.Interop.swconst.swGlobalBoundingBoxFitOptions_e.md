# swGlobalBoundingBoxFitOptions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGlobalBoundingBoxFitOptions_e`

Global bounding box fit types.
Global bounding box fit types.

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

<System.Runtime.InteropServices.GuidAttribute("F2DE8744-53BC-4490-B254-B0D490A7CF3C")>
Public Enum swGlobalBoundingBoxFitOptions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swGlobalBoundingBoxFitOptions_e
```

```

[System.Runtime.InteropServices.Guid("F2DE8744-53BC-4490-B254-B0D490A7CF3C")]
public enum swGlobalBoundingBoxFitOptions_e : System.Enum 
```

```

public enum swGlobalBoundingBoxFitOptions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("F2DE8744-53BC-4490-B254-B0D490A7CF3C")
public enum swGlobalBoundingBoxFitOptions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("F2DE8744-53BC-4490-B254-B0D490A7CF3C")]
__value public enum swGlobalBoundingBoxFitOptions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("F2DE8744-53BC-4490-B254-B0D490A7CF3C")]
public enum class swGlobalBoundingBoxFitOptions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swBoundingBoxType\_BestFit** | 1 = Orientation of the bounding box is based on the X-Y plane |
| **swBoundingBoxType\_CustomPlane** | 2 = Specify the orientation plane or planar face on which to base the bounding box |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swGlobalBoundingBoxFitOptions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
