# swInsertAssyOptions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInsertAssyOptions_e`

Insert assembly into part options. Bitmask.
Insert assembly into part options. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("3A351DF1-928F-42AE-A2F9-6405AAC8ACCB")>
Public Enum swInsertAssyOptions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swInsertAssyOptions_e
```

```

[System.Runtime.InteropServices.Guid("3A351DF1-928F-42AE-A2F9-6405AAC8ACCB")]
public enum swInsertAssyOptions_e : System.Enum 
```

```

public enum swInsertAssyOptions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("3A351DF1-928F-42AE-A2F9-6405AAC8ACCB")
public enum swInsertAssyOptions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("3A351DF1-928F-42AE-A2F9-6405AAC8ACCB")]
__value public enum swInsertAssyOptions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("3A351DF1-928F-42AE-A2F9-6405AAC8ACCB")]
public enum class swInsertAssyOptions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swInsertAssyCoordinateSystems** | 10 or 0x10 |
| **swInsertAssyCosmeticThreads** | 20 or 0x20 |
| **swInsertAssyCustomProperties** | 100 or 0x100 |
| **swInsertAssyGraphicsBodies** | 400 or 0x400 |
| **swInsertAssyHoleWizardData** | 200 or 0x200 |
| **swInsertAssyMaterials** | 2 or 0x2 |
| **swInsertAssyPartCutListProps** | 800 or 0x800 |
| **swInsertAssyRefAxes** | 8 or 0x8 |
| **swInsertAssyRefPlanes** | 4 or 0x4 |
| **swInsertAssySketches** | 80 or 0x80 |
| **swInsertAssySurfaceBodies** | 1 or 0x1 |
| **swInsertAssyVisualProperties** | 40 or 0x40 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swInsertAssyOptions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
