# GetAdjacentFaces Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetAdjacentFaces`

Gets the faces adjacent to this vertex.
Gets the faces adjacent to this vertex.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAdjacentFaces() As System.Object
```

```

Dim instance As IVertex
Dim value As System.Object
 
value = instance.GetAdjacentFaces()
```

```

System.object GetAdjacentFaces()
```

```

System.Object^ GetAdjacentFaces(); 
```

#### Return Value

Array of the [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) adjacent to this vertex

Example

[Get Faces Adjacent to Vertex (VBA)](Get_Faces_Adjacent_to_Vertex_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)  
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.md)  
[IVertex::IGetAdjacentFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetAdjacentFaces.md)  
[IVertex::IGetAdjacentFacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetAdjacentFacesCount.md)
