# swConfigurationChangeTypes_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConfigurationChangeTypes_e`

Types of configuration changes.
Types of configuration changes.

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

<System.Runtime.InteropServices.GuidAttribute("14E2E92A-34A8-4223-9017-A522FB7E6508")>
Public Enum swConfigurationChangeTypes_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swConfigurationChangeTypes_e
```

```

[System.Runtime.InteropServices.Guid("14E2E92A-34A8-4223-9017-A522FB7E6508")]
public enum swConfigurationChangeTypes_e : System.Enum 
```

```

public enum swConfigurationChangeTypes_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("14E2E92A-34A8-4223-9017-A522FB7E6508")
public enum swConfigurationChangeTypes_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("14E2E92A-34A8-4223-9017-A522FB7E6508")]
__value public enum swConfigurationChangeTypes_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("14E2E92A-34A8-4223-9017-A522FB7E6508")]
public enum class swConfigurationChangeTypes_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swConfigurationChangeTypes\_AddChildConfiguration** | 2 |
| **swConfigurationChangeTypes\_AddDisplayState** | 6 |
| **swConfigurationChangeTypes\_ChangeRepresentationParent** | 14 |
| **swConfigurationChangeTypes\_ComponentVisibilityState** | 4 |
| **swConfigurationChangeTypes\_ConvertToPhysicalProduct** | 13 = Change to Physical Product for SOLIDWORKS Connected only; used in [DAssemblyDocEvents\_ConfigurationChangeNotifyEventHandler](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ConfigurationChangeNotifyEventHandler.html) |
| **swConfigurationChangeTypes\_ConvertToRepresentation** | 12 = Change to Representation for SOLIDWORKS Connected only; used in DAssemblyDocEvents\_ConfigurationChangeNotifyEventHandler |
| **swConfigurationChangeTypes\_CustomProperty** | 5 |
| **swConfigurationChangeTypes\_DimensionValue** | 0 |
| **swConfigurationChangeTypes\_Feature** | 9 |
| **swConfigurationChangeTypes\_RemoveChildConfiguration** | 3 |
| **swConfigurationChangeTypes\_RemoveDisplayState** | 7 |
| **swConfigurationChangeTypes\_RenameDisplayState** | 8 |
| **swConfigurationChangeTypes\_SuppressionState** | 1 |
| **swConfigurationChangeTypes\_Undefined** | -1 |
| **swConfigurationChangeTypes\_Unused1** | 10 = Not used |
| **swConfigurationChangeTypes\_Unused2** | 11 = Not used |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swConfigurationChangeTypes\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
