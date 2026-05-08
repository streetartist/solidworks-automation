# swDimensionPrecisionSettings_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDimensionPrecisionSettings_e`

Precision settings for dimensions.
Precision settings for dimensions.

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

<System.Runtime.InteropServices.GuidAttribute("63219915-CEA8-4419-B19D-47112720724E")>
Public Enum swDimensionPrecisionSettings_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swDimensionPrecisionSettings_e
```

```

[System.Runtime.InteropServices.Guid("63219915-CEA8-4419-B19D-47112720724E")]
public enum swDimensionPrecisionSettings_e : System.Enum 
```

```

public enum swDimensionPrecisionSettings_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("63219915-CEA8-4419-B19D-47112720724E")
public enum swDimensionPrecisionSettings_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("63219915-CEA8-4419-B19D-47112720724E")]
__value public enum swDimensionPrecisionSettings_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("63219915-CEA8-4419-B19D-47112720724E")]
public enum class swDimensionPrecisionSettings_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swDoNotChangePrecisionSetting** | -1 = Used by [IDisplayDimension::SetPrecision2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~SetPrecision2.html) only |
| **swPrecisionFollowsDocumentSetting** | -2 = Precision equals the document default precision value |
| **swTolerancePrecisionFollowsNominal** | -3 = Tolerance precision equals the dimension precision value |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swDimensionPrecisionSettings\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
