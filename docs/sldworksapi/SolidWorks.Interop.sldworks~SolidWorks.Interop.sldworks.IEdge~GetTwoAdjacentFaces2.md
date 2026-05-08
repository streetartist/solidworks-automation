# GetTwoAdjacentFaces2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTwoAdjacentFaces2`

Gets the two faces adjacent to an edge.
Gets the two faces adjacent to an edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTwoAdjacentFaces2() As System.Object
```

```

Dim instance As IEdge
Dim value As System.Object
 
value = instance.GetTwoAdjacentFaces2()
```

```

System.object GetTwoAdjacentFaces2()
```

```

System.Object^ GetTwoAdjacentFaces2(); 
```

#### Return Value

Array containing two adjacent [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Remarks

This method is designed to be used with body-related edges, not reference curve or reference sketch edges. This method supports both solid and sheet bodies.

|  |  |
| --- | --- |
| **If...** | **Then the values returned are...** |
| Two valid faces exist | Two faces |
| Only one valid face exists | One face and NULL |

Example

[Get Angle of Hole Not Normal to a Face (VBA)](Get_Angle_of_Hole_Not_Normal_to_a_Face_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)  
[IEdge::IGetTwoAdjacentFaces2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetTwoAdjacentFaces2.md)  
[IVertex::GetAdjacentFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetAdjacentFaces.md)  
[IVertex::IGetAdjacentFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetAdjacentFaces.md)
