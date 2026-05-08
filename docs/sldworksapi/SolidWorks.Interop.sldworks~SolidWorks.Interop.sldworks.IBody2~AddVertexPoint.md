# AddVertexPoint Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddVertexPoint`

Adds a vertex.
Adds a vertex.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddVertexPoint( _
   ByVal Point As System.Object _
) As System.Object
```

```

Dim instance As IBody2
Dim Point As System.Object
Dim value As System.Object
 
value = instance.AddVertexPoint(Point)
```

```

System.object AddVertexPoint( 
   System.object Point
)
```

```

System.Object^ AddVertexPoint( 
   System.Object^ Point
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
[IBody2::IAddVertexPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddVertexPoint.md)
