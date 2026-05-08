# swEdgeFlangeError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEdgeFlangeError_e`

Edge flange error codes.
Edge flange error codes.

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

<System.Runtime.InteropServices.GuidAttribute("B385B014-AC3D-4A71-A01E-B79CAE3B3D63")>
Public Enum swEdgeFlangeError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swEdgeFlangeError_e
```

```

[System.Runtime.InteropServices.Guid("B385B014-AC3D-4A71-A01E-B79CAE3B3D63")]
public enum swEdgeFlangeError_e : System.Enum 
```

```

public enum swEdgeFlangeError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("B385B014-AC3D-4A71-A01E-B79CAE3B3D63")
public enum swEdgeFlangeError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("B385B014-AC3D-4A71-A01E-B79CAE3B3D63")]
__value public enum swEdgeFlangeError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("B385B014-AC3D-4A71-A01E-B79CAE3B3D63")]
public enum class swEdgeFlangeError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swEdgeFlangeError\_EdgeAlreadyExists** | 4 = Specified edge already exists |
| **swEdgeFlangeError\_EdgeNotSpecified** | 1 = Input array of edges is empty |
| **swEdgeFlangeError\_GenericError** | 7 = Unknown error |
| **swEdgeFlangeError\_InvalidEdge** | 5 = Specified edge is invalid |
| **swEdgeFlangeError\_MustSpecifyAtLeastOneEdge** | 6 = You must specify at least one edge |
| **swEdgeFlangeError\_NoError** | 0 = No error |
| **swEdgeFlangeError\_NumberOfEdgesAndSketchesNotEqual** | 3 = Number of edges must equal the number of sketches |
| **swEdgeFlangeError\_SketchNotSpecified** | 2 = Input array of sketches is empty |

Remarks

These error codes are returned by [IEdgeFlangeFeatureData::AddEdges](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdgeFlangeFeatureData~AddEdges.html) and [IEdgeFlangeFeatureData::RemoveEdges](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdgeFlangeFeatureData~RemoveEdges.html).

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swEdgeFlangeError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
