# swSetValueReturnStatus_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSetValueReturnStatus_e`

Return values for attempting to set the value of a parameter.
Return values for attempting to set the value of a parameter.

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

<System.Runtime.InteropServices.GuidAttribute("B995F23D-32D3-46B2-902D-F840CE143210")>
Public Enum swSetValueReturnStatus_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swSetValueReturnStatus_e
```

```

[System.Runtime.InteropServices.Guid("B995F23D-32D3-46B2-902D-F840CE143210")]
public enum swSetValueReturnStatus_e : System.Enum 
```

```

public enum swSetValueReturnStatus_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("B995F23D-32D3-46B2-902D-F840CE143210")
public enum swSetValueReturnStatus_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("B995F23D-32D3-46B2-902D-F840CE143210")]
__value public enum swSetValueReturnStatus_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("B995F23D-32D3-46B2-902D-F840CE143210")]
public enum class swSetValueReturnStatus_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSetValue\_DrivenDimension** | 3 = Cannot be done on a dimension driven by geometry |
| **swSetValue\_Failure** | 1 = Failed for an unknown reason |
| **swSetValue\_FrozenFeatureOwner** | 5 = Owner of the dimension is frozen |
| **swSetValue\_InvalidValue** | 2 = Not a valid value for change parameter |
| **swSetValue\_ModelNotLoaded** | 4 = Model must be loaded in order to set this value |
| **swSetValue\_Successful** | 0 = Successful |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swSetValueReturnStatus\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
