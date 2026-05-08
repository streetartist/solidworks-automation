# swPackAndGoSaveStatus_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPackAndGoSaveStatus_e`

Status of each document intended for Pack and Go.
Status of each document intended for Pack and Go.

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

<System.Runtime.InteropServices.GuidAttribute("A41A056A-2C33-42E6-9E2B-AE526823C5F5")>
Public Enum swPackAndGoSaveStatus_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swPackAndGoSaveStatus_e
```

```

[System.Runtime.InteropServices.Guid("A41A056A-2C33-42E6-9E2B-AE526823C5F5")]
public enum swPackAndGoSaveStatus_e : System.Enum 
```

```

public enum swPackAndGoSaveStatus_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("A41A056A-2C33-42E6-9E2B-AE526823C5F5")
public enum swPackAndGoSaveStatus_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("A41A056A-2C33-42E6-9E2B-AE526823C5F5")]
__value public enum swPackAndGoSaveStatus_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("A41A056A-2C33-42E6-9E2B-AE526823C5F5")]
public enum class swPackAndGoSaveStatus_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swPackAndGoSaveStatus\_FileAlreadyExist** | 2 = File already exists |
| **swPackAndGoSaveStatus\_SaveError** | 4 = Save error |
| **swPackAndGoSaveStatus\_SaveToEmpty** | 3 = Saving empty file |
| **swPackAndGoSaveStatus\_Succeed** | 0 = Success |
| **swPackAndGoSaveStatus\_UserInputNotCorrect** | 1 = User input not correct |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swPackAndGoSaveStatus\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
