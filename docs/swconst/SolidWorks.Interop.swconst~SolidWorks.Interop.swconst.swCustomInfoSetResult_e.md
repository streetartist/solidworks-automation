# swCustomInfoSetResult_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCustomInfoSetResult_e`

Result codes when setting custom properties.
Result codes when setting custom properties.

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

<System.Runtime.InteropServices.GuidAttribute("5B24A03E-4CA2-43AB-8A24-56D6B4B0CBE1")>
Public Enum swCustomInfoSetResult_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCustomInfoSetResult_e
```

```

[System.Runtime.InteropServices.Guid("5B24A03E-4CA2-43AB-8A24-56D6B4B0CBE1")]
public enum swCustomInfoSetResult_e : System.Enum 
```

```

public enum swCustomInfoSetResult_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("5B24A03E-4CA2-43AB-8A24-56D6B4B0CBE1")
public enum swCustomInfoSetResult_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("5B24A03E-4CA2-43AB-8A24-56D6B4B0CBE1")]
__value public enum swCustomInfoSetResult_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("5B24A03E-4CA2-43AB-8A24-56D6B4B0CBE1")]
public enum class swCustomInfoSetResult_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCustomInfoSetResult\_LinkedProp** | 3 |
| **swCustomInfoSetResult\_NotPresent** | 1 = Custom property does not exist |
| **swCustomInfoSetResult\_OK** | 0 = Success |
| **swCustomInfoSetResult\_TypeMismatch** | 2 = Specified value has an incorrect type |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCustomInfoSetResult\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
