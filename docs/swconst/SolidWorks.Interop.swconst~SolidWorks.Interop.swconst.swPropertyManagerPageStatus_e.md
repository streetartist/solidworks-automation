# swPropertyManagerPageStatus_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPropertyManagerPageStatus_e`

PropertyManager page statuses.
PropertyManager page statuses.

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

<System.Runtime.InteropServices.GuidAttribute("787382D0-1E2F-4B00-B0E5-CB976E39280B")>
Public Enum swPropertyManagerPageStatus_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swPropertyManagerPageStatus_e
```

```

[System.Runtime.InteropServices.Guid("787382D0-1E2F-4B00-B0E5-CB976E39280B")]
public enum swPropertyManagerPageStatus_e : System.Enum 
```

```

public enum swPropertyManagerPageStatus_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("787382D0-1E2F-4B00-B0E5-CB976E39280B")
public enum swPropertyManagerPageStatus_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("787382D0-1E2F-4B00-B0E5-CB976E39280B")]
__value public enum swPropertyManagerPageStatus_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("787382D0-1E2F-4B00-B0E5-CB976E39280B")]
public enum class swPropertyManagerPageStatus_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swPropertyManagerPage\_CreationFailure** | -1 |
| **swPropertyManagerPage\_NoDocument** | -2 = A PropertyManager page can only be shown in a SOLIDWORKS document window; you can create and set up the page without a document being active, but there must be a document active when you try to show the page; if there is no active document window, then swPropertyManagerPage\_NoDocument is returned |
| **swPropertyManagerPage\_Okay** | 0 |
| **swPropertyManagerPage\_UnsupportedHandler** | 1 = The PropertyManager page is created and shown; however, a problem exists; for example, you must specify the handler when you create the PropertyManager page; your add-in must implement [IPropertyManagerPage2Handler4](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler4.md) so that SOLIDWORKS can call back certain methods when operations, such as clicking a button, occur on the PropertyManager page;if the interface that is passed in does not support PropertyManagerPage2Handler4, then swPropertyManagerPage\_UnsupportedHandler is returned |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swPropertyManagerPageStatus\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
