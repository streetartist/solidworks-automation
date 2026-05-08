# swBalloonStyle_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBalloonStyle_e`

Balloon styles.
Balloon styles.

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

<System.Runtime.InteropServices.GuidAttribute("9954D56E-85B5-485C-A98B-99834E71B1FA")>
Public Enum swBalloonStyle_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swBalloonStyle_e
```

```

[System.Runtime.InteropServices.Guid("9954D56E-85B5-485C-A98B-99834E71B1FA")]
public enum swBalloonStyle_e : System.Enum 
```

```

public enum swBalloonStyle_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("9954D56E-85B5-485C-A98B-99834E71B1FA")
public enum swBalloonStyle_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("9954D56E-85B5-485C-A98B-99834E71B1FA")]
__value public enum swBalloonStyle_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("9954D56E-85B5-485C-A98B-99834E71B1FA")]
public enum class swBalloonStyle_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swBS\_ArcBracket** | 14 |
| **swBS\_ArclenSym** | 16 |
| **swBS\_Box** | 4 |
| **swBS\_Circular** | 1 |
| **swBS\_Diamond** | 5 |
| **swBS\_DoubleArrow** | 18 |
| **swBS\_FixedSym** | 17 |
| **swBS\_FlagPentagon** | 8 |
| **swBS\_FlagTriangle** | 9 |
| **swBS\_Hexagon** | 3 |
| **swBS\_Inspection** | 13 |
| **swBS\_None** | 0 |
| **swBS\_Pentagon** | 6; Can be used for label location selection **Circular Spit Line** |
| **swBS\_RectBracket** | 15 |
| **swBS\_SCircle** | 12 |
| **swBS\_SplitCirc** | 7; Not valid for notes; only valid for balloons |
| **swBS\_SplitSquare** | 19; Can be used for label location selection **Square Spit Line** |
| **swBS\_Square** | 11 |
| **swBS\_Triangle** | 2 |
| **swBS\_Underline** | 10 |
| **swBS\_Verbose** | 20 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swBalloonStyle\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
