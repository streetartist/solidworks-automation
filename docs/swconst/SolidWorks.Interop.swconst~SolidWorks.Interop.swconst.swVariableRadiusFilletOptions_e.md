# swVariableRadiusFilletOptions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swVariableRadiusFilletOptions_e`

Variable radius fillet transition options.
Variable radius fillet transition options.

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

<System.Runtime.InteropServices.GuidAttribute("7F11813E-5888-4D18-ADE7-D2B8B31CF5EA")>
Public Enum swVariableRadiusFilletOptions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swVariableRadiusFilletOptions_e
```

```

[System.Runtime.InteropServices.Guid("7F11813E-5888-4D18-ADE7-D2B8B31CF5EA")]
public enum swVariableRadiusFilletOptions_e : System.Enum 
```

```

public enum swVariableRadiusFilletOptions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("7F11813E-5888-4D18-ADE7-D2B8B31CF5EA")
public enum swVariableRadiusFilletOptions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("7F11813E-5888-4D18-ADE7-D2B8B31CF5EA")]
__value public enum swVariableRadiusFilletOptions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("7F11813E-5888-4D18-ADE7-D2B8B31CF5EA")]
public enum class swVariableRadiusFilletOptions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSmoothTransition** | 0 = Fillet changes smoothly from one radius to another when matching a fillet edge to an adjacent face |
| **swStraightTransition** | 1 = Fillet changes from one radius to another linearly without matching edge tangency with an adjacent fillet |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swVariableRadiusFilletOptions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
