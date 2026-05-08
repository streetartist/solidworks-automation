# swPropertyManagerPageButtons_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPropertyManagerPageButtons_e`

PropertyManager page buttons.
PropertyManager page buttons.

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

<System.Runtime.InteropServices.GuidAttribute("B28A7D76-BCE7-4E4D-BC93-9400CAA8A6E1")>
Public Enum swPropertyManagerPageButtons_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swPropertyManagerPageButtons_e
```

```

[System.Runtime.InteropServices.Guid("B28A7D76-BCE7-4E4D-BC93-9400CAA8A6E1")]
public enum swPropertyManagerPageButtons_e : System.Enum 
```

```

public enum swPropertyManagerPageButtons_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("B28A7D76-BCE7-4E4D-BC93-9400CAA8A6E1")
public enum swPropertyManagerPageButtons_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("B28A7D76-BCE7-4E4D-BC93-9400CAA8A6E1")]
__value public enum swPropertyManagerPageButtons_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("B28A7D76-BCE7-4E4D-BC93-9400CAA8A6E1")]
public enum class swPropertyManagerPageButtons_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swPropertyManagerPageButton\_Back** | 5 |
| **swPropertyManagerPageButton\_Cancel** | 2 |
| **swPropertyManagerPageButton\_Help** | 3 |
| **swPropertyManagerPageButton\_Next** | 4 |
| **swPropertyManagerPageButton\_Ok** | 1 |
| **swPropertyManagerPageButton\_Preview** | 7 |
| **swPropertyManagerPageButton\_Pushpin** | 8 |
| **swPropertyManagerPageButton\_Redo** | 9 |
| **swPropertyManagerPageButton\_Undo** | 6 |
| **swPropertyManagerPageButton\_WhatsNew** | 10 |

Remarks

Enable or disable a button on a PropertyManager page using [IPropertyManagerPage2::EnableButton](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~EnableButton.html).

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swPropertyManagerPageButtons\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
