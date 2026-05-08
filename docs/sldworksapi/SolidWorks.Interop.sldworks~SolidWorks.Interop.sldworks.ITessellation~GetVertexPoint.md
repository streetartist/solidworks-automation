# GetVertexPoint Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetVertexPoint`

Gets the X, Y and Z values that describe a tessellation vertex.
Gets the X, Y and Z values that describe a tessellation vertex.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetVertexPoint( _
   ByVal VertexId As System.Integer _
) As System.Object
```

```

Dim instance As ITessellation
Dim VertexId As System.Integer
Dim value As System.Object
 
value = instance.GetVertexPoint(VertexId)
```

```

System.object GetVertexPoint( 
   System.int VertexId
)
```

```

System.Object^ GetVertexPoint( 
   System.int VertexId
) 
```

#### Parameters

*VertexId*
:   Tessellation vertex ID of the vertex for which you want to get the X Y Z position values

#### Return Value

Array of 3 doubles that describe the tessellation vertex's X, Y, and Z position

Example

[Tessellate a Body (C#)](Tessellate_a_Body_Example_CSharp.htm)  
[Tessellate a Body (VB.NET)](Tessellate_a_Body_Example_VBNET.htm)  
[Tessellate a Body (VBA)](Tessellate_a_Body_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)
