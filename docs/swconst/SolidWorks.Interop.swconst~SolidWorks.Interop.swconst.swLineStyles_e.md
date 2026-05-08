# swLineStyles_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swLineStyles_e`

Line styles used in drawings.
Line styles used in drawings.

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

<System.Runtime.InteropServices.GuidAttribute("10F58840-632B-4A7C-8E24-961452DAF9FB")>
Public Enum swLineStyles_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swLineStyles_e
```

```

[System.Runtime.InteropServices.Guid("10F58840-632B-4A7C-8E24-961452DAF9FB")]
public enum swLineStyles_e : System.Enum 
```

```

public enum swLineStyles_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("10F58840-632B-4A7C-8E24-961452DAF9FB")
public enum swLineStyles_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("10F58840-632B-4A7C-8E24-961452DAF9FB")]
__value public enum swLineStyles_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("10F58840-632B-4A7C-8E24-961452DAF9FB")]
public enum class swLineStyles_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swLineCENTER** | 4 |
| **swLineCHAIN** | 3 |
| **swLineCHAINTHICK** | 6 = Thin/Thick Chain |
| **swLineCONTINUOUS** | 0 = Solid |
| **swLineDEFAULT** | 7 |
| **swLineHIDDEN** | 1 = Dashed |
| **swLinePHANTOM** | 2 |
| **swLineSTITCH** | 5 |

Remarks

Open a drawing and view line style appearances in **Tools > Options > Document Properties > Line Style**.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swLineStyles\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
