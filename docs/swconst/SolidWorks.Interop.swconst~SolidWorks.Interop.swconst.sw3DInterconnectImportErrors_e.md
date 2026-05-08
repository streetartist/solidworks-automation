# sw3DInterconnectImportErrors_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.sw3DInterconnectImportErrors_e`

3D Interconnect import errors.
3D Interconnect import errors.

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

<System.Runtime.InteropServices.GuidAttribute("F664778D-8DD5-474F-A370-E9B7CF9741C0")>
Public Enum sw3DInterconnectImportErrors_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As sw3DInterconnectImportErrors_e
```

```

[System.Runtime.InteropServices.Guid("F664778D-8DD5-474F-A370-E9B7CF9741C0")]
public enum sw3DInterconnectImportErrors_e : System.Enum 
```

```

public enum sw3DInterconnectImportErrors_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("F664778D-8DD5-474F-A370-E9B7CF9741C0")
public enum sw3DInterconnectImportErrors_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("F664778D-8DD5-474F-A370-E9B7CF9741C0")]
__value public enum sw3DInterconnectImportErrors_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("F664778D-8DD5-474F-A370-E9B7CF9741C0")]
public enum class sw3DInterconnectImportErrors_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **sw3DInterconnectImportErrors\_AssemblyNotSaved** | 3 |
| **sw3DInterconnectImportErrors\_BreakLinkUnavailable** | 4 = Break link is not available for the selected 3D Interconnect feature; break link is only available for top-level assemblies |
| **sw3DInterconnectImportErrors\_Disabled** | 1 = 3D Interconnect is not enabled; to enable set **Tools > Options > System Options > Import > Enable 3D Interconnect** or call calling [ISldWorks::SetUserPreferenceToggle](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html)([swUserPreferenceToggle\_e](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.md).swMultiCAD\_Enable3DInterconnect, True) |
| **sw3DInterconnectImportErrors\_IncompatibleType** | 2 = Specified file type is not correct |
| **sw3DInterconnectImportErrors\_None** | 0 |
| **sw3DInterconnectImportErrors\_ParametersUnavailable** | 5 = Only top-level 3D Interconnect features can be edited |
| **sw3DInterconnectImportErrors\_TransferOptionNeeded** | 6 = One or more import options need to be specified for this import |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.sw3DInterconnectImportErrors\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
