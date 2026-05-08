# swHandleWindowFromHandleCreationFailure_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swHandleWindowFromHandleCreationFailure_e`

Actions on failure to create a .NET control on a PropertyManager page.
Actions on failure to create a .NET control on a PropertyManager page.

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

<System.Runtime.InteropServices.GuidAttribute("F065DB91-3BD0-49B4-94DD-04226D344938")>
Public Enum swHandleWindowFromHandleCreationFailure_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swHandleWindowFromHandleCreationFailure_e
```

```

[System.Runtime.InteropServices.Guid("F065DB91-3BD0-49B4-94DD-04226D344938")]
public enum swHandleWindowFromHandleCreationFailure_e : System.Enum 
```

```

public enum swHandleWindowFromHandleCreationFailure_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("F065DB91-3BD0-49B4-94DD-04226D344938")
public enum swHandleWindowFromHandleCreationFailure_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("F065DB91-3BD0-49B4-94DD-04226D344938")]
__value public enum swHandleWindowFromHandleCreationFailure_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("F065DB91-3BD0-49B4-94DD-04226D344938")]
public enum class swHandleWindowFromHandleCreationFailure_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swHandleWindowFromHandleCreationFailure\_Cancel** | 1 = Create the PropertyManager page without the .NET control. (default) |
| **swHandleWindowFromHandleCreationFailure\_Continue** | 3 = Cancel the creation of the PropertyManager page. |
| **swHandleWindowFromHandleCreationFailure\_Retry** | 2 = Try to create the .NET control again. |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swHandleWindowFromHandleCreationFailure\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
