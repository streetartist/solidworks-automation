# IAddVertexPoint Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddVertexPoint`

Adds a vertex.
Adds a vertex.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddVertexPoint( _
   ByRef Point As System.Double _
) As Vertex
```

```

Dim instance As IBody2
Dim Point As System.Double
Dim value As Vertex
 
value = instance.IAddVertexPoint(Point)
```

```

Vertex IAddVertexPoint( 
   ref System.double Point
)
```

```

Vertex^ IAddVertexPoint( 
   System.double% Point
) 
```

#### Parameters

*Point*
:   Vertex to add

#### Return Value

[IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::AddVertexPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddVertexPoint.md)
