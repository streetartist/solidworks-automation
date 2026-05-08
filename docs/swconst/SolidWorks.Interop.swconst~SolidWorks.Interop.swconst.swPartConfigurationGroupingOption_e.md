# swPartConfigurationGroupingOption_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPartConfigurationGroupingOption_e`

Part configuration groupings for BOM table display.
Part configuration groupings for BOM table display.

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

<System.Runtime.InteropServices.GuidAttribute("916EE5DE-E545-4391-9AD9-752FEFB47EAB")>
Public Enum swPartConfigurationGroupingOption_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swPartConfigurationGroupingOption_e
```

```

[System.Runtime.InteropServices.Guid("916EE5DE-E545-4391-9AD9-752FEFB47EAB")]
public enum swPartConfigurationGroupingOption_e : System.Enum 
```

```

public enum swPartConfigurationGroupingOption_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("916EE5DE-E545-4391-9AD9-752FEFB47EAB")
public enum swPartConfigurationGroupingOption_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("916EE5DE-E545-4391-9AD9-752FEFB47EAB")]
__value public enum swPartConfigurationGroupingOption_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("916EE5DE-E545-4391-9AD9-752FEFB47EAB")]
public enum class swPartConfigurationGroupingOption_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swDisplay\_AllConfigurationOfSamePart\_AsOneItem** | 2 = display configurations of the same part as one item |
| **swDisplay\_ConfigurationOfSamePart\_AsSeparateItem** | 1 = display configurations of the same part as separate items |
| **swDisplay\_ConfigurationWithSameName\_AsOneItem** | 3 = display configurations with the same name as one item |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swPartConfigurationGroupingOption\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
