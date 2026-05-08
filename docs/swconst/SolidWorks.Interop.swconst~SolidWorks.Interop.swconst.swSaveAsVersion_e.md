# swSaveAsVersion_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSaveAsVersion_e`

Version of a particular format to save the document.
Version of a particular format to save the document.

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

<System.Runtime.InteropServices.GuidAttribute("012B185D-A0CF-45F7-A1F7-E651EACE326A")>
Public Enum swSaveAsVersion_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swSaveAsVersion_e
```

```

[System.Runtime.InteropServices.Guid("012B185D-A0CF-45F7-A1F7-E651EACE326A")]
public enum swSaveAsVersion_e : System.Enum 
```

```

public enum swSaveAsVersion_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("012B185D-A0CF-45F7-A1F7-E651EACE326A")
public enum swSaveAsVersion_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("012B185D-A0CF-45F7-A1F7-E651EACE326A")]
__value public enum swSaveAsVersion_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("012B185D-A0CF-45F7-A1F7-E651EACE326A")]
public enum class swSaveAsVersion_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSaveAsCurrentVersion** | 0 = This is the typical save behavior. |
| **swSaveAsDetachedDrawing** | 4 |
| **swSaveAsFormatProE** | 2 |
| **swSaveAsStandardDrawing** | 3 |
| **swSaveAsSW98plus** | Obsolete and no longer supported. |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swSaveAsVersion\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
