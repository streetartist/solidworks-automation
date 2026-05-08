# IEdgeInFaceSense2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IEdgeInFaceSense2`

Checks whether the edge and the loop lying on the specified face have the same direction (sense).
Checks whether the edge and the loop lying on the specified face have the same direction (sense).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IEdgeInFaceSense2( _
   ByVal Facedisp As Face2 _
) As System.Boolean
```

```

Dim instance As IEdge
Dim Facedisp As Face2
Dim value As System.Boolean
 
value = instance.IEdgeInFaceSense2(Facedisp)
```

```

System.bool IEdgeInFaceSense2( 
   Face2 Facedisp
)
```

```

System.bool IEdgeInFaceSense2( 
   Face2^ Facedisp
) 
```

#### Parameters

*Facedisp*
:   Pointer to the [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) that the edge is on

#### Return Value

True for same direction as the loop, false for opposite

Remarks

If this edge does not belong to the face that is passed as an argument, unpredictable results can occur.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)  
[IEdge::EdgeInFaceSense Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~EdgeInFaceSense.md)
