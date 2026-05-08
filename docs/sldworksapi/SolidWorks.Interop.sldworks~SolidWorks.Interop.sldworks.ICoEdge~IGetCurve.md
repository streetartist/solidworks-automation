# IGetCurve Method (ICoEdge)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetCurve`

Gets the underlying curve of this coedge if the coedge is a result of imprecisely sewing two surfaces together.
Gets the underlying curve of this coedge if the coedge is a result of imprecisely sewing two surfaces together.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetCurve() As Curve
```

```

Dim instance As ICoEdge
Dim value As Curve
 
value = instance.IGetCurve()
```

```

Curve IGetCurve()
```

```

Curve^ IGetCurve(); 
```

#### Return Value

Pointer to the curve that is attached to this coedge (see **Remarks**)

Remarks

This method may return NULL if no geometry is attached to the coedge. The edge may still be accurate, and you can obtain the geometry from the edge using:

- [ICoEdge::IGetEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetEdge.md)
- [IEdge::IGetCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetCurve.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICoEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.md)  
[ICoEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge_members.md)  
[ICoEdge::GetCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurve.md)
