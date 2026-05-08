# IGetVertices Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetVertices`

Gets the vertices in this body.
Gets the vertices in this body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetVertices( _
   ByVal Count As System.Integer _
) As Vertex
```

```

Dim instance As IBody2
Dim Count As System.Integer
Dim value As Vertex
 
value = instance.IGetVertices(Count)
```

```

Vertex IGetVertices( 
   System.int Count
)
```

```

Vertex^ IGetVertices( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of vertices in this body

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [vertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) in this body

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IBody2::GetVertexCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetVertexCount.md) to determine the size of the array.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[GetVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetVertices.md)
