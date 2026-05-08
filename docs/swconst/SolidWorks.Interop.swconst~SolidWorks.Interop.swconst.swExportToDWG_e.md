# swExportToDWG_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swExportToDWG_e`

Options for the Action parameter of IPartDoc::ExportToDWG2.
Options for the Action parameter of [IPartDoc::ExportToDWG2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~IExportToDWG2.html).

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

<System.Runtime.InteropServices.GuidAttribute("F921E5B0-8FF6-46BE-A51C-7F0E6FBA4DB5")>
Public Enum swExportToDWG_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swExportToDWG_e
```

```

[System.Runtime.InteropServices.Guid("F921E5B0-8FF6-46BE-A51C-7F0E6FBA4DB5")]
public enum swExportToDWG_e : System.Enum 
```

```

public enum swExportToDWG_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("F921E5B0-8FF6-46BE-A51C-7F0E6FBA4DB5")
public enum swExportToDWG_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("F921E5B0-8FF6-46BE-A51C-7F0E6FBA4DB5")]
__value public enum swExportToDWG_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("F921E5B0-8FF6-46BE-A51C-7F0E6FBA4DB5")]
public enum class swExportToDWG_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swExportToDWG\_ExportAnnotationViews** | 3 |
| **swExportToDWG\_ExportSelectedFacesOrLoops** | 2 |
| **swExportToDWG\_ExportSheetMetal** | 1; Valid only if the active document contains sheet metal |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swExportToDWG\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
