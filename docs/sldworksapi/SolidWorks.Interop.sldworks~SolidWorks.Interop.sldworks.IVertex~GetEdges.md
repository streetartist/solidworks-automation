# GetEdges Method (IVertex)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetEdges`

Gets a list of enumerated edges corresponding to this vertex.
Gets a list of enumerated edges corresponding to this vertex.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEdges() As System.Object
```

```

Dim instance As IVertex
Dim value As System.Object
 
value = instance.GetEdges()
```

```

System.object GetEdges()
```

```

System.Object^ GetEdges(); 
```

#### Return Value

Array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumEdges.md) corresponding to this vertex

Example

[Get Edges for Vertex (VBA)](Get_Edges_for_Vertex_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)  
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.md)  
[IVertex::EnumEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~EnumEdges.md)
