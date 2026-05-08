# swPartingLineFeatureStatus_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPartingLineFeatureStatus_e`

Statuses of parting line features.
Statuses of parting line features.

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

<System.Runtime.InteropServices.GuidAttribute("58DB176B-D4D3-4D77-B8ED-EBEA62064093")>
Public Enum swPartingLineFeatureStatus_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swPartingLineFeatureStatus_e
```

```

[System.Runtime.InteropServices.Guid("58DB176B-D4D3-4D77-B8ED-EBEA62064093")]
public enum swPartingLineFeatureStatus_e : System.Enum 
```

```

public enum swPartingLineFeatureStatus_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("58DB176B-D4D3-4D77-B8ED-EBEA62064093")
public enum swPartingLineFeatureStatus_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("58DB176B-D4D3-4D77-B8ED-EBEA62064093")]
__value public enum swPartingLineFeatureStatus_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("58DB176B-D4D3-4D77-B8ED-EBEA62064093")]
public enum class swPartingLineFeatureStatus_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **STATUS\_MOLD\_PARTINGLINE\_EDGES\_OPEN** | 2 = Select edges that form a closed loop |
| **STATUS\_MOLD\_PARTINGLINE\_NON\_SEPARABLE** | 4 = The parting line is complete, but the mold cannot be separated into core and cavity; you might need to create shut-off surfaces |
| **STATUS\_MOLD\_PARTINGLINE\_SEPARABLE** | 3 = The parting line is complete; the mold can be separated into core and cavity |
| **STATUS\_MOLD\_REDUNDANT\_EDGES** | 1 = There are more than enough edges selected to form a parting line; remove any redundant edges or add edges to close gaps between disjoint edge chains |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swPartingLineFeatureStatus\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
