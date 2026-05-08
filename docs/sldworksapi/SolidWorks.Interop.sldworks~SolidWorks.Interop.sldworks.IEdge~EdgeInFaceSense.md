# EdgeInFaceSense Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~EdgeInFaceSense`

Checks whether the edge and the loop lying on the specified face have the same direction (sense).
Checks whether the edge and the loop lying on the specified face have the same direction (sense).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EdgeInFaceSense( _
   ByVal Facedisp As System.Object _
) As System.Boolean
```

```

Dim instance As IEdge
Dim Facedisp As System.Object
Dim value As System.Boolean
 
value = instance.EdgeInFaceSense(Facedisp)
```

```

System.bool EdgeInFaceSense( 
   System.object Facedisp
)
```

```

System.bool EdgeInFaceSense( 
   System.Object^ Facedisp
) 
```

#### Parameters

*Facedisp*
:   Face that the edge is on

#### Return Value

True for the same direction, false for the opposite direction

Remarks

If this edge does not belong to the specified face, then this method can cause unpredictable  
results.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)  
[IEdge::IEdgeInFaceSense2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IEdgeInFaceSense2.md)
