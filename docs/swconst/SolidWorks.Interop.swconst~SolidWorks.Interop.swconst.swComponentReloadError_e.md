# swComponentReloadError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swComponentReloadError_e`

Codes returned when reloading components in assemblies.
Codes returned when reloading components in assemblies.

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

<System.Runtime.InteropServices.GuidAttribute("C1CB1A52-C2FF-40A5-B56B-E58E6F9E33CD")>
Public Enum swComponentReloadError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swComponentReloadError_e
```

```

[System.Runtime.InteropServices.Guid("C1CB1A52-C2FF-40A5-B56B-E58E6F9E33CD")]
public enum swComponentReloadError_e : System.Enum 
```

```

public enum swComponentReloadError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("C1CB1A52-C2FF-40A5-B56B-E58E6F9E33CD")
public enum swComponentReloadError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("C1CB1A52-C2FF-40A5-B56B-E58E6F9E33CD")]
__value public enum swComponentReloadError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("C1CB1A52-C2FF-40A5-B56B-E58E6F9E33CD")]
public enum class swComponentReloadError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swComponentLightWeightError** | 8 |
| **swDocumentAlreadyOpenedError** | 12 |
| **swDocumentEventError** | 13 |
| **swDocumentHasNoView** | 11 |
| **swDocumentNotChanged** | 14 |
| **swFileDoesntExistError** | 9 |
| **swFileInvalidOrSameNameError** | 10 |
| **swFileNotSavedError** | 5 |
| **swFutureVersionError** | 2 |
| **swInvalidComponentError** | 6 |
| **swInvalidOption** | 4 |
| **swModifiedNotReloadedError** | 3 |
| **swReadOnlyChanged** | 16 |
| **swReloadCancel** | 15 |
| **swReloadOkay** | 0 |
| **swUnexpectedError** | 7 |
| **swWriteAccessError** | 1 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swComponentReloadError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
