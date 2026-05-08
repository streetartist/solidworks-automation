# swSetValueInConfiguration_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSetValueInConfiguration_e`

Values for indicating in which configurations the value should be set.
Values for indicating in which configurations the value should be set.

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

<System.Runtime.InteropServices.GuidAttribute("6D9C8B56-91ED-49DE-B061-5DFC2BBA2ED9")>
Public Enum swSetValueInConfiguration_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swSetValueInConfiguration_e
```

```

[System.Runtime.InteropServices.Guid("6D9C8B56-91ED-49DE-B061-5DFC2BBA2ED9")]
public enum swSetValueInConfiguration_e : System.Enum 
```

```

public enum swSetValueInConfiguration_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("6D9C8B56-91ED-49DE-B061-5DFC2BBA2ED9")
public enum swSetValueInConfiguration_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("6D9C8B56-91ED-49DE-B061-5DFC2BBA2ED9")]
__value public enum swSetValueInConfiguration_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("6D9C8B56-91ED-49DE-B061-5DFC2BBA2ED9")]
public enum class swSetValueInConfiguration_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSetValue\_InAllConfigurations** | 2 = Set the value in all configurations |
| **swSetValue\_InSpecificConfigurations** | 3 = Set the value in the specific configuration |
| **swSetValue\_InThisConfiguration** | 1 = Set the value in the current configuration only |
| **swSetValue\_NoConfiguration** | -1 = Ignore configurations in drawing sketches |
| **swSetValue\_UseCurrentSetting** | 0 = Use whatever setting this parameter currently has |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swSetValueInConfiguration\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
