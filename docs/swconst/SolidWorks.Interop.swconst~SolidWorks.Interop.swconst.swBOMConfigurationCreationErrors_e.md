# swBOMConfigurationCreationErrors_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBOMConfigurationCreationErrors_e`

BOM table configuration creation errors.
BOM table configuration creation errors.

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

<System.Runtime.InteropServices.GuidAttribute("6CCA8498-C8C7-419C-AF8F-074C3EE9761D")>
Public Enum swBOMConfigurationCreationErrors_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swBOMConfigurationCreationErrors_e
```

```

[System.Runtime.InteropServices.Guid("6CCA8498-C8C7-419C-AF8F-074C3EE9761D")]
public enum swBOMConfigurationCreationErrors_e : System.Enum 
```

```

public enum swBOMConfigurationCreationErrors_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("6CCA8498-C8C7-419C-AF8F-074C3EE9761D")
public enum swBOMConfigurationCreationErrors_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("6CCA8498-C8C7-419C-AF8F-074C3EE9761D")]
__value public enum swBOMConfigurationCreationErrors_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("6CCA8498-C8C7-419C-AF8F-074C3EE9761D")]
public enum class swBOMConfigurationCreationErrors_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swBOMTableCreation\_AlreadyExists** | -3 = BOM table already exists for this drawing view |
| **swBOMTableCreation\_ExcelDisabled** | -4 = BOM table cannot be created because Microsoft Excel is disabled on this system |
| **swBOMTableCreation\_Failed** | -5 = BOM table creation failed because the specified template is not valid |
| **swBOMTableCreation\_MustBeDrawingView** | -2 = BOM tables can only be added to a drawing view |
| **swBOMTableCreation\_NoModelForView** | -6 = No model available for drawing view |
| **swBOMTableCreation\_Okay** | 0 = Table was successfully created |
| **swBOMTableCreation\_UnspecifiedError** | -1 = Table could not be created for unknown reasons |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swBOMConfigurationCreationErrors\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
