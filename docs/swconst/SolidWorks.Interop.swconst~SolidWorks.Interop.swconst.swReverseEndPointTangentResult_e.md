# swReverseEndPointTangentResult_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swReverseEndPointTangentResult_e`

Result codes for ISketchManager::ReverseEndPointTangent.
Result codes for [ISketchManager::ReverseEndPointTangent](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ReverseEndPointTangent.html).

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

<System.Runtime.InteropServices.GuidAttribute("D0A7D6AB-D2AF-4F28-8EA6-901B16E09705")>
Public Enum swReverseEndPointTangentResult_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swReverseEndPointTangentResult_e
```

```

[System.Runtime.InteropServices.Guid("D0A7D6AB-D2AF-4F28-8EA6-901B16E09705")]
public enum swReverseEndPointTangentResult_e : System.Enum 
```

```

public enum swReverseEndPointTangentResult_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("D0A7D6AB-D2AF-4F28-8EA6-901B16E09705")
public enum swReverseEndPointTangentResult_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("D0A7D6AB-D2AF-4F28-8EA6-901B16E09705")]
__value public enum swReverseEndPointTangentResult_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("D0A7D6AB-D2AF-4F28-8EA6-901B16E09705")]
public enum class swReverseEndPointTangentResult_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swReverseEndPointTangent\_ConstraintConflict** | 2 = Reversing the end point tangent direction creates a conflict with existing constraints |
| **swReverseEndPointTangent\_InvalidSelection** | 1 = Select a valid end point tangent direction entity |
| **swReverseEndPointTangent\_Success** | 0 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swReverseEndPointTangentResult\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
