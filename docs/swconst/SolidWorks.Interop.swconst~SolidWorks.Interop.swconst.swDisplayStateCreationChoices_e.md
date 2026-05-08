# swDisplayStateCreationChoices_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDisplayStateCreationChoices_e`

Display-state preserve options.
Display-state preserve options.

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

<System.Runtime.InteropServices.GuidAttribute("364E0061-3E6E-428F-B228-FE8FC2DC5EB6")>
Public Enum swDisplayStateCreationChoices_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swDisplayStateCreationChoices_e
```

```

[System.Runtime.InteropServices.Guid("364E0061-3E6E-428F-B228-FE8FC2DC5EB6")]
public enum swDisplayStateCreationChoices_e : System.Enum 
```

```

public enum swDisplayStateCreationChoices_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("364E0061-3E6E-428F-B228-FE8FC2DC5EB6")
public enum swDisplayStateCreationChoices_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("364E0061-3E6E-428F-B228-FE8FC2DC5EB6")]
__value public enum swDisplayStateCreationChoices_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("364E0061-3E6E-428F-B228-FE8FC2DC5EB6")]
public enum class swDisplayStateCreationChoices_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swDisplayStateCreation\_AskUser** | -1; Display the dialog where the user can select the display states (PhotoWorks material and SOLIDWORKS colors) he or she wants to preserve; however, if **swDisplayStateCreation\_AskUser** is set and the user opens the file using **ISldWorks::OpenDoc***n* (where *n* is the version number of the method), then both display states are preserved and the dialog is not displayed; valid in documents created in SOLIDWORKS 2009 and earlier |
| **swDisplayStateCreation\_BothPWSW** | 3; Preserve both PhotoWorks and SOLIDWORKS display states; valid in documents created in SOLIDWORKS 2009 and earlier |
| **swDisplayStateCreation\_PW** | 1; Preserve PhotoWorks material display state only; valid in documents created in SOLIDWORKS 2009 and earlier |
| **swDisplayStateCreation\_SW** | 2; Preserve SOLIDWORKS color display state only; valid in documents created in SOLIDWORKS 2009 and earlier |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swDisplayStateCreationChoices\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
