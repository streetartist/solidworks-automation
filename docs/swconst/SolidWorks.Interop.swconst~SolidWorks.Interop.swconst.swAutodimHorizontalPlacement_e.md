# swAutodimHorizontalPlacement_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAutodimHorizontalPlacement_e`

Placements for the horizontal dimensions created by ISketch::AutoDimension2 and IDrawingDoc::AutoDimension.
Placements for the horizontal dimensions created by [ISketch::AutoDimension2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~AutoDimension2.html) and [IDrawingDoc::AutoDimension](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~Solidworks.Interop.sldworks.IDrawingDoc~AutoDimension.html).

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

<System.Runtime.InteropServices.GuidAttribute("4A5F1BF3-8803-4AF9-B38B-ED6C8039F9C7")>
Public Enum swAutodimHorizontalPlacement_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swAutodimHorizontalPlacement_e
```

```

[System.Runtime.InteropServices.Guid("4A5F1BF3-8803-4AF9-B38B-ED6C8039F9C7")]
public enum swAutodimHorizontalPlacement_e : System.Enum 
```

```

public enum swAutodimHorizontalPlacement_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("4A5F1BF3-8803-4AF9-B38B-ED6C8039F9C7")
public enum swAutodimHorizontalPlacement_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("4A5F1BF3-8803-4AF9-B38B-ED6C8039F9C7")]
__value public enum swAutodimHorizontalPlacement_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("4A5F1BF3-8803-4AF9-B38B-ED6C8039F9C7")]
public enum class swAutodimHorizontalPlacement_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAutodimHorizontalPlacementAbove** | 1 = Place the horizontal dimensions above the sketch. |
| **swAutodimHorizontalPlacementBelow** | -1 = Place the horizontal dimensions below the sketch. |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swAutodimHorizontalPlacement\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
