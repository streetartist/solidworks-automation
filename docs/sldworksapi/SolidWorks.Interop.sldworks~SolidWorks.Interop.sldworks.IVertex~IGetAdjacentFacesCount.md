# IGetAdjacentFacesCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetAdjacentFacesCount`

Gets the number of faces adjacent to this vertex.
Gets the number of faces adjacent to this vertex.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetAdjacentFacesCount() As System.Integer
```

```

Dim instance As IVertex
Dim value As System.Integer
 
value = instance.IGetAdjacentFacesCount()
```

```

System.int IGetAdjacentFacesCount()
```

```

System.int IGetAdjacentFacesCount(); 
```

#### Return Value

Number of faces adjacent to this vertex

Remarks

Call this method before calling [IVertex::IGetAdjacentFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetAdjacentFaces.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)  
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.md)  
[IVertex::GetAdjacentFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetAdjacentFaces.md)
