# swLinkDimensionError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swLinkDimensionError_e`

Link dimension errors.
Link dimension errors.

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

<System.Runtime.InteropServices.GuidAttribute("8ACB8EE1-E98A-4FA6-BEAF-4757D9839E53")>
Public Enum swLinkDimensionError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swLinkDimensionError_e
```

```

[System.Runtime.InteropServices.Guid("8ACB8EE1-E98A-4FA6-BEAF-4757D9839E53")]
public enum swLinkDimensionError_e : System.Enum 
```

```

public enum swLinkDimensionError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("8ACB8EE1-E98A-4FA6-BEAF-4757D9839E53")
public enum swLinkDimensionError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("8ACB8EE1-E98A-4FA6-BEAF-4757D9839E53")]
__value public enum swLinkDimensionError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("8ACB8EE1-E98A-4FA6-BEAF-4757D9839E53")]
public enum class swLinkDimensionError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swLinkDimensionError\_AlreadyLinked** | 4 = Dimension already linked elsewhere |
| **swLinkDimensionError\_CannotLink** | 8 = The selected dimensions cannot be linked; combination of failures swLinkDimensionError\_LinkAcrossDocs to swLinkDimensionError\_DrivenByEquation |
| **swLinkDimensionError\_DrivenByEquation** | 7 = Dimension's driven by an equation |
| **swLinkDimensionError\_EmptyString** | 11 = Empty string passed as link text |
| **swLinkDimensionError\_ErrorUknown** | 0 = Unknown error occurred |
| **swLinkDimensionError\_IncompatibleDimTypes** | 3 = Cannot link incompatible dimension types |
| **swLinkDimensionError\_IncompatibleValues** | 6 = Incompatible range of values make these dimensions not linkable |
| **swLinkDimensionError\_InvalidString** | 12 = Invalid string passed as link text; cannot contain the at sign (@) character |
| **swLinkDimensionError\_LinkAcrossDocs** | 2 = Values to be linked must belong to the same model |
| **swLinkDimensionError\_NoError** | 1 = No error; success |
| **swLinkDimensionError\_ReadOnlyOrDriven** | 5 = Dimension is a read-only, driven, or a reference dimension that cannot be linked |
| **swLinkDimensionError\_UnableToCreateSharedParam** | 9 = Shared parameter could not be created |
| **swLinkDimensionError\_UnlinkFailure** | 10 = Dimension was not already linked |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swLinkDimensionError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
