# IGetTwoAdjacentFaces Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetTwoAdjacentFaces`

Obsolete. Superseded by IEdge::IGetTwoAdjacentFaces2.
Obsolete. Superseded by [IEdge::IGetTwoAdjacentFaces2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetTwoAdjacentFaces2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IGetTwoAdjacentFaces( _
   ByRef Face1 As Face, _
   ByRef Face2 As Face _
) 
```

```

Dim instance As IEdge
Dim Face1 As Face
Dim Face2 As Face
 
instance.IGetTwoAdjacentFaces(Face1, Face2)
```

```

void IGetTwoAdjacentFaces( 
   out Face Face1,
   out Face Face2
)
```

```

void IGetTwoAdjacentFaces( 
   [Out] Face^ Face1,
   [Out] Face^ Face2
) 
```

#### Parameters

*Face1*

*Face2*
:   v

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)
