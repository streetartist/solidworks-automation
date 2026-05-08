# swMoveCopyOptions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMoveCopyOptions_e`

Move/copy options. Bitmask.
Move/copy options. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("1BB5E072-ACB6-4E48-892C-6155E2FC0E0C")>
Public Enum swMoveCopyOptions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swMoveCopyOptions_e
```

```

[System.Runtime.InteropServices.Guid("1BB5E072-ACB6-4E48-892C-6155E2FC0E0C")]
public enum swMoveCopyOptions_e : System.Enum 
```

```

public enum swMoveCopyOptions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("1BB5E072-ACB6-4E48-892C-6155E2FC0E0C")
public enum swMoveCopyOptions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("1BB5E072-ACB6-4E48-892C-6155E2FC0E0C")]
__value public enum swMoveCopyOptions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("1BB5E072-ACB6-4E48-892C-6155E2FC0E0C")]
public enum class swMoveCopyOptions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swMoveCopyOptionsCreateNewFolder** | 2 or 0x2 |
| **swMoveCopyOptionsOverwriteExistingDocs** | 1 or 0x1 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swMoveCopyOptions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
