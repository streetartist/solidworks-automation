# IGetVertexNormal Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetVertexNormal`

Gets the information that describes the normal direction corresponding to vertex.
Gets the information that describes the normal direction corresponding to vertex.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetVertexNormal( _
   ByVal VertexId As System.Integer _
) As System.Double
```

```

Dim instance As ITessellation
Dim VertexId As System.Integer
Dim value As System.Double
 
value = instance.IGetVertexNormal(VertexId)
```

```

System.double IGetVertexNormal( 
   System.int VertexId
)
```

```

System.double IGetVertexNormal( 
   System.int VertexId
) 
```

#### Parameters

*VertexId*
:   ID of the vertex from which you want to return the normal information

#### Return Value

Array of 3 doubles describing the normal vector direction of this vertex corresponding to the face to which it belongs

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)  
[ITessellate::GetVertexNormal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetVertexNormal.md)
