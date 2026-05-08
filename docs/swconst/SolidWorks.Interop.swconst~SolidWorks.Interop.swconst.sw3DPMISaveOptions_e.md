# sw3DPMISaveOptions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.sw3DPMISaveOptions_e`

3D PMI (Product and Manufacturing Information) save options when comparing two different versions of the same model. Bitmask.
3D PMI (Product and Manufacturing Information) save options when comparing two different versions of the same model. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("9F6435D6-FC80-474A-AB87-74B032D6D9CA")>
Public Enum sw3DPMISaveOptions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As sw3DPMISaveOptions_e
```

```

[System.Runtime.InteropServices.Guid("9F6435D6-FC80-474A-AB87-74B032D6D9CA")]
public enum sw3DPMISaveOptions_e : System.Enum 
```

```

public enum sw3DPMISaveOptions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("9F6435D6-FC80-474A-AB87-74B032D6D9CA")
public enum sw3DPMISaveOptions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("9F6435D6-FC80-474A-AB87-74B032D6D9CA")]
__value public enum sw3DPMISaveOptions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("9F6435D6-FC80-474A-AB87-74B032D6D9CA")]
public enum class sw3DPMISaveOptions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAddReportToDesignBinder** | 1 or 0x1 |
| **swDimXpertData** | 4 or 0x4 |
| **swReferenceData** | 8 or 0x8 |
| **swViewReportOnSave** | 2 or 0x2 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.sw3DPMISaveOptions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
