# swMacroFeatureOptions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMacroFeatureOptions_e`

Placement of the macro feature in the FeatureManager design tree options. Bitmask.
Placement of the macro feature in the FeatureManager design tree options. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("683072BF-D0FC-4932-A9C2-CA6BB631A8C6")>
Public Enum swMacroFeatureOptions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swMacroFeatureOptions_e
```

```

[System.Runtime.InteropServices.Guid("683072BF-D0FC-4932-A9C2-CA6BB631A8C6")]
public enum swMacroFeatureOptions_e : System.Enum 
```

```

public enum swMacroFeatureOptions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("683072BF-D0FC-4932-A9C2-CA6BB631A8C6")
public enum swMacroFeatureOptions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("683072BF-D0FC-4932-A9C2-CA6BB631A8C6")]
__value public enum swMacroFeatureOptions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("683072BF-D0FC-4932-A9C2-CA6BB631A8C6")]
public enum class swMacroFeatureOptions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swMacroFeatureAlwaysAtEnd** | 1 or 0x1 |
| **swMacroFeatureByDefault** | 0 or 0x0 |
| **swMacroFeatureEmbedMacroFile** | 16 or 0x10; not supported by programming languages for the Microsoft .NET Framework; for example, not supported by C#, Visual Basic .NET, or Managed C++ |
| **swMacroFeatureIsDragable** | 4 or 0x4 |
| **swMacroFeatureIsPatternable** | 2 or 0x2 |
| **swMacroFeatureNoCachedBody** | 8 or 0x8; do not serialize cached body in macro feature |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swMacroFeatureOptions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
