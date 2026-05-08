# swImportDxfDwg_ImportMethod_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swImportDxfDwg_ImportMethod_e`

DXF/DWG import methods.
DXF/DWG import methods.

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

<System.Runtime.InteropServices.GuidAttribute("05605263-506D-4708-934C-6CE6F3E4B971")>
Public Enum swImportDxfDwg_ImportMethod_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swImportDxfDwg_ImportMethod_e
```

```

[System.Runtime.InteropServices.Guid("05605263-506D-4708-934C-6CE6F3E4B971")]
public enum swImportDxfDwg_ImportMethod_e : System.Enum 
```

```

public enum swImportDxfDwg_ImportMethod_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("05605263-506D-4708-934C-6CE6F3E4B971")
public enum swImportDxfDwg_ImportMethod_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("05605263-506D-4708-934C-6CE6F3E4B971")]
__value public enum swImportDxfDwg_ImportMethod_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("05605263-506D-4708-934C-6CE6F3E4B971")]
public enum class swImportDxfDwg_ImportMethod_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swImportDxfDwg\_DoNotImportSheet** | 0 = Do not import this sheet (layout) |
| **swImportDxfDwg\_ImportToDrawing** | 1 = Import this sheet (layout) to a sheet in a new drawing |
| **swImportDxfDwg\_ImportToExistingDrawing** | 3 = Import this sheet (layout) into an existing drawing |
| **swImportDxfDwg\_ImportToExistingPart** | 4 = Import this sheet (layout) into an existing part |
| **swImportDxfDwg\_ImportToPartSketch** | 2 = Import this sheet (layout) into a sketch in a new part |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swImportDxfDwg\_ImportMethod\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
