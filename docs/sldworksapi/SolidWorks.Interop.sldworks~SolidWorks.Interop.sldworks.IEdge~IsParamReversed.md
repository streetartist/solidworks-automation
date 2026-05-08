# IsParamReversed Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IsParamReversed`

Gets whether the edge and its underlying curve have the same parameterization or if the direction is reversed.
Gets whether the edge and its underlying curve have the same parameterization or if the direction is reversed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsParamReversed() As System.Boolean
```

```

Dim instance As IEdge
Dim value As System.Boolean
 
value = instance.IsParamReversed()
```

```

System.bool IsParamReversed()
```

```

System.bool IsParamReversed(); 
```

#### Return Value

True if the curve direction and edge direction are different, false if not

Remarks

If this method returns True, then the curve direction and edge direction are different. As the parameter increases, the corresponding point on the edge moves from the end of the edge to the start.

If this method returns false, then the curve direction and edge direction are the same.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)  
[IEdge::GetCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams2.md)  
[IEdge::IGetCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetCurveParams2.md)
