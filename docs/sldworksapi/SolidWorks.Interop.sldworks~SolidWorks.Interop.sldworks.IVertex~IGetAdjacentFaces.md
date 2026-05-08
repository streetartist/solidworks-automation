# IGetAdjacentFaces Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetAdjacentFaces`

Gets the faces adjacent to this vertex.
Gets the faces adjacent to this vertex.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetAdjacentFaces( _
   ByVal NFaceCount As System.Integer _
) As Face2
```

```

Dim instance As IVertex
Dim NFaceCount As System.Integer
Dim value As Face2
 
value = instance.IGetAdjacentFaces(NFaceCount)
```

```

Face2 IGetAdjacentFaces( 
   System.int NFaceCount
)
```

```

Face2^ IGetAdjacentFaces( 
   System.int NFaceCount
) 
```

#### Parameters

*NFaceCount*
:   Number of adjacent faces

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) adjacent to this vertex

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IVertex::IGetAdjacentFacesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetAdjacentFacesCount.md) to get the number of faces adjacent to this vertex.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)  
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.md)  
[IVertex::GetAdjacentFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetAdjacentFaces.md)
