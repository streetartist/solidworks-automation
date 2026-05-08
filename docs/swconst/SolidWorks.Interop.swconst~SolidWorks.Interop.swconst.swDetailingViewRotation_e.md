# swDetailingViewRotation_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDetailingViewRotation_e`

View rotation options.
View rotation options.

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

<System.Runtime.InteropServices.GuidAttribute("B757AA03-6B8B-4F10-835A-1C7990A917A6")>
Public Enum swDetailingViewRotation_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swDetailingViewRotation_e
```

```

[System.Runtime.InteropServices.Guid("B757AA03-6B8B-4F10-835A-1C7990A917A6")]
public enum swDetailingViewRotation_e : System.Enum 
```

```

public enum swDetailingViewRotation_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("B757AA03-6B8B-4F10-835A-1C7990A917A6")
public enum swDetailingViewRotation_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("B757AA03-6B8B-4F10-835A-1C7990A917A6")]
__value public enum swDetailingViewRotation_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("B757AA03-6B8B-4F10-835A-1C7990A917A6")]
public enum class swDetailingViewRotation_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swDetailingViewRotation\_DisplayAngle** | 4 = Display the rotation angle only |
| **swDetailingViewRotation\_DisplayROTATEDAngleCWCCW** | 3 =  Display the word ROTATED, the rotation angle, and either CW (clockwise) or CCW (counterclockwise) |
| **swDetailingViewRotation\_DisplaySymbol** | 2 = Display the rotation symbol only |
| **swDetailingViewRotation\_DisplaySymbolAngle** | 1 = Display both the rotation symbol and the rotation angle |
| **swDetailingViewRotation\_None** | 0 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swDetailingViewRotation\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
