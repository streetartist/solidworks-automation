# swNotifyEntityType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swNotifyEntityType_e`

Notification entity types.
Notification entity types.

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

<System.Runtime.InteropServices.GuidAttribute("11EF5D72-006D-412D-B5DD-B8E706032D59")>
Public Enum swNotifyEntityType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swNotifyEntityType_e
```

```

[System.Runtime.InteropServices.Guid("11EF5D72-006D-412D-B5DD-B8E706032D59")]
public enum swNotifyEntityType_e : System.Enum 
```

```

public enum swNotifyEntityType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("11EF5D72-006D-412D-B5DD-B8E706032D59")
public enum swNotifyEntityType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("11EF5D72-006D-412D-B5DD-B8E706032D59")]
__value public enum swNotifyEntityType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("11EF5D72-006D-412D-B5DD-B8E706032D59")]
public enum class swNotifyEntityType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swNotifyBlockDef** | Obsolete |
| **swNotifyComponent** | 2 = Assembly component is being added, renamed, or deleted |
| **swNotifyComponentInternal** | 8 = Assembly component is internal to the assembly |
| **swNotifyConfiguration** | 1 = Configuration is being added, renamed, or deleted |
| **swNotifyDerivedConfiguration** | 4 = Derived configuration is being added, renamed, or deleted |
| **swNotifyDrawingSheet** | 5 = Drawing sheet is being added, renamed, or deleted |
| **swNotifyDrawingView** | 6 = Drawing view is being added, renamed, or deleted |
| **swNotifyFeature** | 3 = Feature is being added, renamed, or deleted |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swNotifyEntityType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
