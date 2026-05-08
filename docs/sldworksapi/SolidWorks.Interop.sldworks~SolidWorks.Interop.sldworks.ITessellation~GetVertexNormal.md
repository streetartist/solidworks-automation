# GetVertexNormal Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetVertexNormal`

Gets the information that describes the normal direction corresponding to vertex.
Gets the information that describes the normal direction corresponding to vertex.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetVertexNormal( _
   ByVal VertexId As System.Integer _
) As System.Object
```

```

Dim instance As ITessellation
Dim VertexId As System.Integer
Dim value As System.Object
 
value = instance.GetVertexNormal(VertexId)
```

```

System.object GetVertexNormal( 
   System.int VertexId
)
```

```

System.Object^ GetVertexNormal( 
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
[ITessellation::IGetVertexNormal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetVertexNormal.md)
