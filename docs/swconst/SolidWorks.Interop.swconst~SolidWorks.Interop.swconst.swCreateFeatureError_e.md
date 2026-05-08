# swCreateFeatureError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCreateFeatureError_e`

Error codes that may occur when creating a feature.
Error codes that may occur when creating a feature.

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

<System.Runtime.InteropServices.GuidAttribute("D50963DB-99FD-437B-97C5-92CBEB1E0349")>
Public Enum swCreateFeatureError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCreateFeatureError_e
```

```

[System.Runtime.InteropServices.Guid("D50963DB-99FD-437B-97C5-92CBEB1E0349")]
public enum swCreateFeatureError_e : System.Enum 
```

```

public enum swCreateFeatureError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("D50963DB-99FD-437B-97C5-92CBEB1E0349")
public enum swCreateFeatureError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("D50963DB-99FD-437B-97C5-92CBEB1E0349")]
__value public enum swCreateFeatureError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("D50963DB-99FD-437B-97C5-92CBEB1E0349")]
public enum class swCreateFeatureError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCreateFeatureError\_GenricError\_GeometricError** | 0 = Inputs provided resulted in a geometric error |
| **swCreateFeatureError\_GenricError\_UnknownError** | 1 = Failure reason unknown |
| **swCreateFeatureError\_MateController\_DimensionValueOutOfLimit** | 5 = Value for dimension provided is out of range |
| **swCreateFeatureError\_MateController\_FailedToSolveMates** | 4 = Inputs provided failed to solve mates |
| **swCreateFeatureError\_MateController\_MateNotSet** | 2 = Mate not set when creating mate controller |
| **swCreateFeatureError\_MateController\_MateSelectionsPositionDataMismatch** | 6 = Number of mate selections do not match number of values in position data array |
| **swCreateFeatureError\_MateController\_MateTypeNotSupported** | 3 = Supported mate types are Distance and Limit Distance, Angle and Limit Angle, Width, and Slot |
| **swCreateFeatureError\_SolidToSheetMetal\_FixedFaceOrEdgeIsMissing** | 8 =  Fixed face or edge is missing |
| **swCreateFeatureError\_SolidToSheetMetal\_Success** | 7 = Successfully converted solid to sheet metal |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCreateFeatureError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
