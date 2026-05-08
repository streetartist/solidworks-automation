# swBOMPartNumberSource_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBOMPartNumberSource_e`

Sources from numbers in BOM tables. Bitmask.
Sources from numbers in BOM tables. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("2E05D6C9-4FD3-4B8D-AC19-FCCB7FE26271")>
Public Enum swBOMPartNumberSource_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swBOMPartNumberSource_e
```

```

[System.Runtime.InteropServices.Guid("2E05D6C9-4FD3-4B8D-AC19-FCCB7FE26271")]
public enum swBOMPartNumberSource_e : System.Enum 
```

```

public enum swBOMPartNumberSource_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("2E05D6C9-4FD3-4B8D-AC19-FCCB7FE26271")
public enum swBOMPartNumberSource_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("2E05D6C9-4FD3-4B8D-AC19-FCCB7FE26271")]
__value public enum swBOMPartNumberSource_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("2E05D6C9-4FD3-4B8D-AC19-FCCB7FE26271")]
public enum class swBOMPartNumberSource_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swBOMPartNumber\_ConfigurationName** | 2 or 0x2 |
| **swBOMPartNumber\_DocumentName** | 1 or 0x1 |
| **swBOMPartNumber\_ParentName** | 4 or 0x4 |
| **swBOMPartNumber\_UserSpecified** | 8 or 0x8 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swBOMPartNumberSource\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
