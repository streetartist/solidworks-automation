# IGetVertexPoint Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetVertexPoint`

Gets the X, Y and Z values that describe a tessellation vertex.
Gets the X, Y and Z values that describe a tessellation vertex.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetVertexPoint( _
   ByVal VertexId As System.Integer _
) As System.Double
```

```

Dim instance As ITessellation
Dim VertexId As System.Integer
Dim value As System.Double
 
value = instance.IGetVertexPoint(VertexId)
```

```

System.double IGetVertexPoint( 
   System.int VertexId
)
```

```

System.double IGetVertexPoint( 
   System.int VertexId
) 
```

#### Parameters

*VertexId*
:   Tessellation vertex ID of the vertex for which you want to get the X Y Z position values

#### Return Value

Array of 3 doubles that describe the tessellation vertex's X, Y, and Z position

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)  
[ITessellate::GetVertexParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetVertexParams.md)
