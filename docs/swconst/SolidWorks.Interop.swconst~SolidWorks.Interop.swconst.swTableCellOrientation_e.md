# swTableCellOrientation_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTableCellOrientation_e`

Orientations of text in table cells.
Orientations of text in table cells.

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

<System.Runtime.InteropServices.GuidAttribute("8AAE2CD6-5B9C-4C68-9376-BB42473890FB")>
Public Enum swTableCellOrientation_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swTableCellOrientation_e
```

```

[System.Runtime.InteropServices.Guid("8AAE2CD6-5B9C-4C68-9376-BB42473890FB")]
public enum swTableCellOrientation_e : System.Enum 
```

```

public enum swTableCellOrientation_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("8AAE2CD6-5B9C-4C68-9376-BB42473890FB")
public enum swTableCellOrientation_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("8AAE2CD6-5B9C-4C68-9376-BB42473890FB")]
__value public enum swTableCellOrientation_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("8AAE2CD6-5B9C-4C68-9376-BB42473890FB")]
public enum class swTableCellOrientation_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swTableCellOrientation\_Down** | 3 |
| **swTableCellOrientation\_Left** | 1 |
| **swTableCellOrientation\_Right** | 0 |
| **swTableCellOrientation\_Rotate90CCW** | 6 = Rotate text 90 degrees counter clockwise from the current orientation |
| **swTableCellOrientation\_Rotate90CW** | 5 = Rotate text 90 degrees clockwise from the current orientation |
| **swTableCellOrientation\_Up** | 2 |
| **swTableCellOrientation\_Varies** | 4 = Orientation varies in several table cells; not valid when calling [ITableAnnotation::SetCellTextOrientation](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellTextOrientation.html) |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swTableCellOrientation\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
