# swFaceCoincidentResult_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFaceCoincidentResult_e`

Face coincidence results.
Face coincidence results.

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

<System.Runtime.InteropServices.GuidAttribute("D1ED931F-FA7B-468A-8975-6516BC286785")>
Public Enum swFaceCoincidentResult_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swFaceCoincidentResult_e
```

```

[System.Runtime.InteropServices.Guid("D1ED931F-FA7B-468A-8975-6516BC286785")]
public enum swFaceCoincidentResult_e : System.Enum 
```

```

public enum swFaceCoincidentResult_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("D1ED931F-FA7B-468A-8975-6516BC286785")
public enum swFaceCoincidentResult_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("D1ED931F-FA7B-468A-8975-6516BC286785")]
__value public enum swFaceCoincidentResult_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("D1ED931F-FA7B-468A-8975-6516BC286785")]
public enum class swFaceCoincidentResult_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swFaceCoincident\_FalseBoundary1** | 3 = The two faces are not coincident. At least one point on the boundary of face 1 is not coincident with the boundary of face 2. |
| **swFaceCoincident\_FalseBoundary2** | 4 = The two faces are not coincident. At least one point on the boundary of face 2 is not coincident with the boundary of face 1. |
| **swFaceCoincident\_FalseFace1** | 5 = The two faces are not coincident. At least one point on face 1 is not coincident with face 2. |
| **swFaceCoincident\_FalseFace2** | 6 = The two faces are not coincident. At least one point on face 2 is not coincident with face 1. |
| **swFaceCoincident\_FalseSurface** | 7 = At least one of the faces does not have a surface attached. |
| **swFaceCoincident\_FalseTopology** | 2 = The two faces are not coincident. The number of holes are different. |
| **swFaceCoincident\_True** | 0 = The faces are coincident to the specified tolerance. |
| **swFaceCoincident\_TrueReversed** | 1 = The two faces are coincident to the specified tolerance, but their normals are reversed. |
| **swFaceCoincidentUnknownResult** | -1 = Unknown |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swFaceCoincidentResult\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
