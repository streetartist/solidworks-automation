# swBodyOperationError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBodyOperationError_e`

Body operation errors.
Body operation errors.

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

<System.Runtime.InteropServices.GuidAttribute("F1668E03-3E10-4043-91B9-AE5F34714617")>
Public Enum swBodyOperationError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swBodyOperationError_e
```

```

[System.Runtime.InteropServices.Guid("F1668E03-3E10-4043-91B9-AE5F34714617")]
public enum swBodyOperationError_e : System.Enum 
```

```

public enum swBodyOperationError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("F1668E03-3E10-4043-91B9-AE5F34714617")
public enum swBodyOperationError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("F1668E03-3E10-4043-91B9-AE5F34714617")]
__value public enum swBodyOperationError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("F1668E03-3E10-4043-91B9-AE5F34714617")]
public enum class swBodyOperationError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swBodyOperationBooleanFail** | 1058 = Boolean fail error |
| **swBodyOperationDisjointBodies** | 5 = Disjoint bodies error |
| **swBodyOperationEmptyBody** | 6 = Empty body error |
| **swBodyOperationEmptyInputBody** | 7 = Empty input body error |
| **swBodyOperationFailGeomCondition** | 3 = Failed geometry condition |
| **swBodyOperationFailToCutBody** | 4 = Failed to cut body error |
| **swBodyOperationIntersectSolidWithSheets** | 972 = Intersect solid with sheets error |
| **swBodyOperationInvalidInputBody** | 8 = Invalid input body |
| **swBodyOperationMissingGeom** | 96 = Missing geometry error |
| **swBodyOperationNoError** | 0 = No error |
| **swBodyOperationNoIntersect** | 1067 = No intersect error |
| **swBodyOperationNonApiBody** | 1 = Non API body error |
| **swBodyOperationNonManifold** | 547 = Nonmanifold error |
| **swBodyOperationOpposedSheets** | 951 = Boolean fail error; invalid orientation for operation |
| **swBodyOperationPartialCoincidence** | 1040 = Partial coincidence error |
| **swBodyOperationSameToolAndTarget** | 545 = Same tool and target error |
| **swBodyOperationUniteSolidSheet** | 543 = Unite solid sheet error |
| **swBodyOperationUnknownError** | -1 = Unknown error |
| **swBodyOperationWrongType** | 2 = Wrong type error |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swBodyOperationError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
