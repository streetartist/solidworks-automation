# swEndConditions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndConditions_e`

End conditions for creation of a variety of features.
End conditions for creation of a variety of features.

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

<System.Runtime.InteropServices.GuidAttribute("718284B5-F5D6-4239-A90C-89AAE86BDB91")>
Public Enum swEndConditions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swEndConditions_e
```

```

[System.Runtime.InteropServices.Guid("718284B5-F5D6-4239-A90C-89AAE86BDB91")]
public enum swEndConditions_e : System.Enum 
```

```

public enum swEndConditions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("718284B5-F5D6-4239-A90C-89AAE86BDB91")
public enum swEndConditions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("718284B5-F5D6-4239-A90C-89AAE86BDB91")]
__value public enum swEndConditions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("718284B5-F5D6-4239-A90C-89AAE86BDB91")]
public enum class swEndConditions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swEndCondBlind** | 0 |
| **swEndCondMidPlane** | 6 |
| **swEndCondOffsetFromSurface** | 5 |
| **swEndCondThroughAll** | 1 |
| **swEndCondThroughAllBoth** | 9 |
| **swEndCondThroughNext** | 2 |
| **swEndCondUpToBody** | 7 |
| **swEndCondUpToNext** | 11 |
| **swEndCondUpToSelection** | 10 |
| **swEndCondUpToSurface** | 4 = Do not use; superseded by swEndCondUpToSelection |
| **swEndCondUpToVertex** | 3 = Do not use; superseded by swEndCondUpToSelection |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swEndConditions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
