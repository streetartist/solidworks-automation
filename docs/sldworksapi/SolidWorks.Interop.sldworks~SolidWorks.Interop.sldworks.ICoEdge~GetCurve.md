# GetCurve Method (ICoEdge)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurve`

Gets the underlying curve of this coedge if the coedge is a result of imprecisely sewing two surfaces together.
Gets the underlying curve of this coedge if the coedge is a result of imprecisely sewing two surfaces together.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCurve() As System.Object
```

```

Dim instance As ICoEdge
Dim value As System.Object
 
value = instance.GetCurve()
```

```

System.object GetCurve()
```

```

System.Object^ GetCurve(); 
```

#### Return Value

Curve that is attached to this coedge (see **Remarks**)

Remarks

This method may return Nothing if no geometry is attached to the coedge. The edge may still be accurate, and you can obtain the geometry from the edge using:

- [ICoEdge::GetEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetEdge.md)
- [IEdge::GetCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurve.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICoEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.md)  
[ICoEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge_members.md)  
[ICoEdge::IGetCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetCurve.md)
