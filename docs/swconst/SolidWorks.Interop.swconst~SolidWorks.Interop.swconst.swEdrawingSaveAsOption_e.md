# swEdrawingSaveAsOption_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEdrawingSaveAsOption_e`

eDrawings Save As options.
eDrawings Save As options.

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

<System.Runtime.InteropServices.GuidAttribute("C4DA1103-9D2F-4F8B-A1F4-7418DF7C26EE")>
Public Enum swEdrawingSaveAsOption_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swEdrawingSaveAsOption_e
```

```

[System.Runtime.InteropServices.Guid("C4DA1103-9D2F-4F8B-A1F4-7418DF7C26EE")]
public enum swEdrawingSaveAsOption_e : System.Enum 
```

```

public enum swEdrawingSaveAsOption_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("C4DA1103-9D2F-4F8B-A1F4-7418DF7C26EE")
public enum swEdrawingSaveAsOption_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("C4DA1103-9D2F-4F8B-A1F4-7418DF7C26EE")]
__value public enum swEdrawingSaveAsOption_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("C4DA1103-9D2F-4F8B-A1F4-7418DF7C26EE")]
public enum class swEdrawingSaveAsOption_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swEdrawingSaveActive** | 1 or 0x1; Publish the active configuration or sheet when saving as an eDrawings |
| **swEdrawingSaveAll** | 2 or 0x2; Publish all configurations or sheets when saving as an eDrawings |
| **swEdrawingSaveSelected** | 3 or 0x3; Publish sheets or configurations specified by [swEmodelSelectionList](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceStringListValue_e.md) when saving as an eDrawings |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swEdrawingSaveAsOption\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
