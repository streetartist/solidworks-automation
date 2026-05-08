# swHoleTableTagOrder_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swHoleTableTagOrder_e`

Method by which to assign tag numbers to holes of the same size.
Method by which to assign tag numbers to holes of the same size.

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

<System.Runtime.InteropServices.GuidAttribute("3F0F8AD8-6F19-4F32-B5FD-4A2FA7A72AEA")>
Public Enum swHoleTableTagOrder_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swHoleTableTagOrder_e
```

```

[System.Runtime.InteropServices.Guid("3F0F8AD8-6F19-4F32-B5FD-4A2FA7A72AEA")]
public enum swHoleTableTagOrder_e : System.Enum 
```

```

public enum swHoleTableTagOrder_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("3F0F8AD8-6F19-4F32-B5FD-4A2FA7A72AEA")
public enum swHoleTableTagOrder_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("3F0F8AD8-6F19-4F32-B5FD-4A2FA7A72AEA")]
__value public enum swHoleTableTagOrder_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("3F0F8AD8-6F19-4F32-B5FD-4A2FA7A72AEA")]
public enum class swHoleTableTagOrder_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swHoleTableTagOrder\_Radial** | 3 = Number holes in order of increasing radial angle from the table view origin, starting at -180 degrees in a counterclockwise direction |
| **swHoleTableTagOrder\_ReduceToolPath** | 2 = Number holes in next nearest order, starting at the table view origin |
| **swHoleTableTagOrder\_XY** | 1 = Number holes in order of their XLoc and YLoc |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swHoleTableTagOrder\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
