# swAutodimEntities_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAutodimEntities_e`

Entities to dimension ISketch::AutoDimension2 and IDrawingDoc::AutoDimension.
Entities to dimension [ISketch::AutoDimension2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~AutoDimension2.html) and [IDrawingDoc::AutoDimension](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~Solidworks.Interop.sldworks.IDrawingDoc~AutoDimension.html).

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

<System.Runtime.InteropServices.GuidAttribute("DD806D8D-C038-4544-B1D0-58C6A86BCFBD")>
Public Enum swAutodimEntities_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swAutodimEntities_e
```

```

[System.Runtime.InteropServices.Guid("DD806D8D-C038-4544-B1D0-58C6A86BCFBD")]
public enum swAutodimEntities_e : System.Enum 
```

```

public enum swAutodimEntities_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("DD806D8D-C038-4544-B1D0-58C6A86BCFBD")
public enum swAutodimEntities_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("DD806D8D-C038-4544-B1D0-58C6A86BCFBD")]
__value public enum swAutodimEntities_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("DD806D8D-C038-4544-B1D0-58C6A86BCFBD")]
public enum class swAutodimEntities_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAutodimEntitiesAll** | 1 = Autodimensions all of the supported entities in the sketch |
| **swAutodimEntitiesBasedOnPreselect** | 0 = SOLIDWORKS to figure out what to do based on the selected supported entities marked with [swAutodimMarkEntities](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAutodimMark_e.md). If any exist, then autodimension them, just like swAutodimEntitiesSelected. If none exist, then autodimension all supported entities, just like swAutodimEntitiesAll |
| **swAutodimEntitiesSelected** | 2 = Autodimensions selected supported entities marked with [swAutodimMarkEntities](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAutodimMark_e.md). If none exist, then autodimensions all supported entities, just like swAutodimEntitiesAll |

Remarks

Supported entities are lines, points, vertices, faces, sketch entities, center lines, and center marks.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swAutodimEntities\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
