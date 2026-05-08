# swCropViewErrors_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCropViewErrors_e`

Errors when cropping views.
Errors when cropping views.

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

<System.Runtime.InteropServices.GuidAttribute("C7355766-15E2-45ED-A94E-94A205AA9341")>
Public Enum swCropViewErrors_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCropViewErrors_e
```

```

[System.Runtime.InteropServices.Guid("C7355766-15E2-45ED-A94E-94A205AA9341")]
public enum swCropViewErrors_e : System.Enum 
```

```

public enum swCropViewErrors_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("C7355766-15E2-45ED-A94E-94A205AA9341")
public enum swCropViewErrors_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("C7355766-15E2-45ED-A94E-94A205AA9341")]
__value public enum swCropViewErrors_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("C7355766-15E2-45ED-A94E-94A205AA9341")]
public enum class swCropViewErrors_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCropViewErrors\_CannotCropDetailOrBrokenView** | 2 = Cannot crop detail or broken view |
| **swCropViewErrors\_CannotUnfoldView** | 3 = Cannot unfold view |
| **swCropViewErrors\_IncorrectProfile** | 4 = Bad spline |
| **swCropViewErrors\_NoError** | 1 |
| **swCropViewErrors\_Unknown** | 0 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCropViewErrors\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
