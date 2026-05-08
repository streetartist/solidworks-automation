# IEdgeInFaceSense Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IEdgeInFaceSense`

Obsolete. Superseded by IEdge::IEdgeInFaceSense2.
Obsolete. Superseded by [IEdge::IEdgeInFaceSense2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IEdgeInFaceSense2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IEdgeInFaceSense( _
   ByVal Facedisp As Face _
) As System.Boolean
```

```

Dim instance As IEdge
Dim Facedisp As Face
Dim value As System.Boolean
 
value = instance.IEdgeInFaceSense(Facedisp)
```

```

System.bool IEdgeInFaceSense( 
   Face Facedisp
)
```

```

System.bool IEdgeInFaceSense( 
   Face^ Facedisp
) 
```

#### Parameters

*Facedisp*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)
