# EnumCoEdges Method (IEdge)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~EnumCoEdges`

Lists the coedges that reference this edge.
Lists the coedges that reference this edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EnumCoEdges() As EnumCoEdges
```

```

Dim instance As IEdge
Dim value As EnumCoEdges
 
value = instance.EnumCoEdges()
```

```

EnumCoEdges EnumCoEdges()
```

```

EnumCoEdges^ EnumCoEdges(); 
```

#### Return Value

Pointer to the [enumerated list of coedges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumCoEdges.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)  
[IEnumCoEdges::Next Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumCoEdges~Next.md)
