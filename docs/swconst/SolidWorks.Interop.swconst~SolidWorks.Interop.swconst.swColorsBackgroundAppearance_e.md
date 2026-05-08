# swColorsBackgroundAppearance_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swColorsBackgroundAppearance_e`

Backgrounds for graphics area.
Backgrounds for graphics area.

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

<System.Runtime.InteropServices.GuidAttribute("1FCA4C85-C829-439C-A1EB-11BECCB9EA74")>
Public Enum swColorsBackgroundAppearance_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swColorsBackgroundAppearance_e
```

```

[System.Runtime.InteropServices.Guid("1FCA4C85-C829-439C-A1EB-11BECCB9EA74")]
public enum swColorsBackgroundAppearance_e : System.Enum 
```

```

public enum swColorsBackgroundAppearance_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("1FCA4C85-C829-439C-A1EB-11BECCB9EA74")
public enum swColorsBackgroundAppearance_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("1FCA4C85-C829-439C-A1EB-11BECCB9EA74")]
__value public enum swColorsBackgroundAppearance_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("1FCA4C85-C829-439C-A1EB-11BECCB9EA74")]
public enum class swColorsBackgroundAppearance_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swColorsBackgroundAppearance\_DocumentScene** | 3 |
| **swColorsBackgroundAppearance\_Gradient** | 1 |
| **swColorsBackgroundAppearance\_Image** | 2 |
| **swColorsBackgroundAppearance\_Plain** | 0 |

Remarks

Use with [swUserPreferenceIntegerValue\_e.swColorsBackgroundAppearance](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceIntegerValue_e.md).

Use the system-level string [swUserPreferenceStringValue\_e.swColorsBackgroundImageFile](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceStringValue_e.md) to set the name of the file containing the image to display as the background of the SOLIDWORKS graphics area.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swColorsBackgroundAppearance\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
