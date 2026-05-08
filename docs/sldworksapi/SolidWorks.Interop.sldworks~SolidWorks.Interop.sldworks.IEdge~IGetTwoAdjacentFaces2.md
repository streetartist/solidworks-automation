# IGetTwoAdjacentFaces2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetTwoAdjacentFaces2`

Gets the two faces adjacent to an edge.
Gets the two faces adjacent to an edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IGetTwoAdjacentFaces2( _
   ByRef Face1 As Face2, _
   ByRef Face2 As Face2 _
) 
```

```

Dim instance As IEdge
Dim Face1 As Face2
Dim Face2 As Face2
 
instance.IGetTwoAdjacentFaces2(Face1, Face2)
```

```

void IGetTwoAdjacentFaces2( 
   out Face2 Face1,
   out Face2 Face2
)
```

```

void IGetTwoAdjacentFaces2( 
   [Out] Face2^ Face1,
   [Out] Face2^ Face2
) 
```

#### Parameters

*Face1*
:   Pointer to the first adjacent [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

*Face2*
:   Pointer to the second adjacent [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Remarks

This method is designed to be used with body-related edges, not reference curve or reference sketch edges. This method supports both solid and sheet bodies.

|  |  |
| --- | --- |
| **If...** | **Then the values returned are...** |
| Two valid faces exist | Two faces |
| Only one valid face exists | One face and NULL |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)  
[IEdge::GetTwoAdjacentFaces2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTwoAdjacentFaces2.md)  
[IVertex::GetAdjacentFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetAdjacentFaces.md)  
[IVertex::IGetAdjacentFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetAdjacentFaces.md)
