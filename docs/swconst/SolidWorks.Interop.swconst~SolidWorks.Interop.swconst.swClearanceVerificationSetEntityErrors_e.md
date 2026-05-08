# swClearanceVerificationSetEntityErrors_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swClearanceVerificationSetEntityErrors_e`

Error codes when setting entities for clearance verification.
Error codes when setting entities for clearance verification.

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

<System.Runtime.InteropServices.GuidAttribute("E409B45B-6D6C-4F1E-BD2E-58F5797D9EED")>
Public Enum swClearanceVerificationSetEntityErrors_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swClearanceVerificationSetEntityErrors_e
```

```

[System.Runtime.InteropServices.Guid("E409B45B-6D6C-4F1E-BD2E-58F5797D9EED")]
public enum swClearanceVerificationSetEntityErrors_e : System.Enum 
```

```

public enum swClearanceVerificationSetEntityErrors_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("E409B45B-6D6C-4F1E-BD2E-58F5797D9EED")
public enum swClearanceVerificationSetEntityErrors_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("E409B45B-6D6C-4F1E-BD2E-58F5797D9EED")]
__value public enum swClearanceVerificationSetEntityErrors_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("E409B45B-6D6C-4F1E-BD2E-58F5797D9EED")]
public enum class swClearanceVerificationSetEntityErrors_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swClearanceVerification\_swComponentAlreadySelected** | 2 = Same component added twice or component added whose face is in face array |
| **swClearanceVerification\_swFacesAlreadySelected** | 1 = Same face added twice |
| **swClearanceVerification\_swInsufficientEntities** | 5 = Face and component arrays are empty |
| **swClearanceVerification\_swInvalidComponent** | 3 = Not a valid SOLIDWORKS component |
| **swClearanceVerification\_swInvalidFace** | 4 = Not a valid SOLIDWORKS face |
| **swClearanceVerification\_swSuccess** | 0 |
| **swClearanceVerification\_Unknown** | -1 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swClearanceVerificationSetEntityErrors\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
