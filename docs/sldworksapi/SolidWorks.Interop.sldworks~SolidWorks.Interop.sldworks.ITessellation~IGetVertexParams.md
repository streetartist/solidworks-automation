# IGetVertexParams Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetVertexParams`

Gets the parameters corresponding to a tessellation vertex.
Gets the parameters corresponding to a tessellation vertex.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetVertexParams( _
   ByVal VertexId As System.Integer _
) As System.Double
```

```

Dim instance As ITessellation
Dim VertexId As System.Integer
Dim value As System.Double
 
value = instance.IGetVertexParams(VertexId)
```

```

System.double IGetVertexParams( 
   System.int VertexId
)
```

```

System.double IGetVertexParams( 
   System.int VertexId
) 
```

#### Parameters

*VertexId*
:   ID of the tessellation vertex for which you want to the parameters

#### Return Value

- in-process, unmanaged C++: Pointer to an array of contains 17 doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The following parameters returned from this method are formatted as an array of 17 doubles:

- u, v - location of the vertex on the face (return value position [0-1])
- du - tangent vector at u (return value [2-4])
- dv - tangent vector at v (return value [5-7])
- d2u, dudv, d2v - curvature vectors for u and v (return value [8-16])

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)  
[ITessellate::GetVertexParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetVertexParams.md)
