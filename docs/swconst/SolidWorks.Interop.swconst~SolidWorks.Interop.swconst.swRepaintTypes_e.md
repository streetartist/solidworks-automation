# swRepaintTypes_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRepaintTypes_e`

Repaint notification types.
Repaint notification types.

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

<System.Runtime.InteropServices.GuidAttribute("2FCB9119-CE31-4878-A1F3-415C5C90CCCF")>
Public Enum swRepaintTypes_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swRepaintTypes_e
```

```

[System.Runtime.InteropServices.Guid("2FCB9119-CE31-4878-A1F3-415C5C90CCCF")]
public enum swRepaintTypes_e : System.Enum 
```

```

public enum swRepaintTypes_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("2FCB9119-CE31-4878-A1F3-415C5C90CCCF")
public enum swRepaintTypes_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("2FCB9119-CE31-4878-A1F3-415C5C90CCCF")]
__value public enum swRepaintTypes_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("2FCB9119-CE31-4878-A1F3-415C5C90CCCF")]
public enum class swRepaintTypes_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swDamageRepairUpdate** | 7 |
| **swExplodedUpdate** | 4 |
| **swInsertSketchUpdate** | 5 |
| **swLightUpdate** | 1 |
| **swMaterialUpdate** | 2 |
| **swScrollViewUpdate** | 10 |
| **swSectionedExitUpdate** | 9 |
| **swSectionedUpdate** | 3 |
| **swSelectionUpdate** | 8 |
| **swStandardUpdate** | 0 |
| **swViewDisplayUpdate** | 6 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swRepaintTypes\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
