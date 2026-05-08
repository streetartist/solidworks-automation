# swAutodimVerticalPlacement_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAutodimVerticalPlacement_e`

Placements of the vertical dimensions created by ISketch::AutoDimension2 and IDrawingDoc::AutoDimension.
Placements of the vertical dimensions created by [ISketch::AutoDimension2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~AutoDimension2.html) and [IDrawingDoc::AutoDimension](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~Solidworks.Interop.sldworks.IDrawingDoc~AutoDimension.html).

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

<System.Runtime.InteropServices.GuidAttribute("E7C74949-FCBF-493B-91B9-66968491E40E")>
Public Enum swAutodimVerticalPlacement_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swAutodimVerticalPlacement_e
```

```

[System.Runtime.InteropServices.Guid("E7C74949-FCBF-493B-91B9-66968491E40E")]
public enum swAutodimVerticalPlacement_e : System.Enum 
```

```

public enum swAutodimVerticalPlacement_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("E7C74949-FCBF-493B-91B9-66968491E40E")
public enum swAutodimVerticalPlacement_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("E7C74949-FCBF-493B-91B9-66968491E40E")]
__value public enum swAutodimVerticalPlacement_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("E7C74949-FCBF-493B-91B9-66968491E40E")]
public enum class swAutodimVerticalPlacement_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAutodimVerticalPlacementLeft** | -1 = Place the vertical dimensions left of the sketch |
| **swAutodimVerticalPlacementRight** | 1 = Place the vertical dimensions right of the sketch |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swAutodimVerticalPlacement\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
