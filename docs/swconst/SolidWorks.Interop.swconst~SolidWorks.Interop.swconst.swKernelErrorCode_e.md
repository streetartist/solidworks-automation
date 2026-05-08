# swKernelErrorCode_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swKernelErrorCode_e`

Kernel error codes.
Kernel error codes.

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

<System.Runtime.InteropServices.GuidAttribute("15C61B06-71F6-4C57-82D0-B2CE42EF4B2F")>
Public Enum swKernelErrorCode_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swKernelErrorCode_e
```

```

[System.Runtime.InteropServices.Guid("15C61B06-71F6-4C57-82D0-B2CE42EF4B2F")]
public enum swKernelErrorCode_e : System.Enum 
```

```

public enum swKernelErrorCode_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("15C61B06-71F6-4C57-82D0-B2CE42EF4B2F")
public enum swKernelErrorCode_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("15C61B06-71F6-4C57-82D0-B2CE42EF4B2F")]
__value public enum swKernelErrorCode_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("15C61B06-71F6-4C57-82D0-B2CE42EF4B2F")]
public enum class swKernelErrorCode_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swErrorBodyDontKnit** | -101041 |
| **swErrorCheckFailed** | -105061 |
| **swErrorCheckFailed2** | -113812 |
| **swErrorCurveDiscontinuous** | -100131 |
| **swErrorCurveShort** | -101057 |
| **swErrorEdgeIncorrectOrder** | -116406 |
| **swErrorEdgeisectInvalid** | -116404 |
| **swErrorError** | 0 |
| **swErrorFacecheckFailed** | -113829 |
| **swErrorFaceFaceInconsistent** | -113816 |
| **swErrorFaceRedundant** | -116402 |
| **swErrorFailed** | -101063 |
| **swErrorGeometryDegenerate** | -113806 |
| **swErrorGeometryDiscontinuous** | -113827 |
| **swErrorGeometryMissing** | -113803 |
| **swErrorGeometrySelfx** | -113805 |
| **swErrorHasInvalidentity** | -101004 |
| **swErrorInconsistentDirs** | -116403 |
| **swErrorInvalidEntity** | -100914 |
| **swErrorInvalidGeometry** | -100999 |
| **swErrorInvalidGeometry2** | -113808 |
| **swErrorInvalidKnots** | -100978 |
| **swErrorInvalidLoop** | -116405 |
| **swErrorInvalidParameter** | -100120 |
| **swErrorInvalidPattern** | -101042 |
| **swErrorInvalidSharing** | -100921 |
| **swErrorLoopsInconsistent** | -113826 |
| **swErrorNotEntity** | -100022 |
| **swErrorSuccess** | 1 |
| **swErrorSurfaceDiscontinuous** | -100129 |
| **swErrorTopologySelfx** | -113804 |
| **swErrorUnknown** | -1 |
| **swErrorVertexNotOnCurve** | -113818 |
| **swErrorVerticesTouch** | -113821 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swKernelErrorCode\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
