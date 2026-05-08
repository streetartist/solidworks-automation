# swMateAlign_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMateAlign_e`

Mate alignment types.
Mate alignment types.

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

<System.Runtime.InteropServices.GuidAttribute("14E5DCE6-F352-4422-A5B3-787137E2A051")>
Public Enum swMateAlign_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swMateAlign_e
```

```

[System.Runtime.InteropServices.Guid("14E5DCE6-F352-4422-A5B3-787137E2A051")]
public enum swMateAlign_e : System.Enum 
```

```

public enum swMateAlign_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("14E5DCE6-F352-4422-A5B3-787137E2A051")
public enum swMateAlign_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("14E5DCE6-F352-4422-A5B3-787137E2A051")]
__value public enum swMateAlign_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("14E5DCE6-F352-4422-A5B3-787137E2A051")]
public enum class swMateAlign_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAlignAGAINST** | Obsolete. Do not use. |
| **swAlignNONE** | Obsolete. Do not use. |
| **swAlignSAME** | Obsolete. Do not use. |
| **swMateAlignALIGNED** | 0 |
| **swMateAlignANTI\_ALIGNED** | 1 |
| **swMateAlignCLOSEST** | 2 |

Remarks

These values have been changed to correct improper mate alignment mapping.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swMateAlign\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
