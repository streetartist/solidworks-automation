# EnumEdgesOriented Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~EnumEdgesOriented`

Gets the enumerated edges and orients them per coedge in the direction corresponding to this vertex.
Gets the enumerated edges and orients them per coedge in the direction corresponding to this vertex.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EnumEdgesOriented() As EnumEdges
```

```

Dim instance As IVertex
Dim value As EnumEdges
 
value = instance.EnumEdgesOriented()
```

```

EnumEdges EnumEdgesOriented()
```

```

EnumEdges^ EnumEdgesOriented(); 
```

#### Return Value

[Enumerated edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumEdges.md)

Remarks

The order of the edges is counter-clockwise.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)  
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.md)
