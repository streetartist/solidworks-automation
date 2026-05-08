# IGetCurve Method (IEdge)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetCurve`

Gets the underlying curve for this edge.
Gets the underlying curve for this edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetCurve() As Curve
```

```

Dim instance As IEdge
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

Pointer to the underlying [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) for this edge

Example

[Get Circular Holes in Face (C++)](Get_Circular_Holes_In_Face_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)  
[IEdge::GetCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurve.md)  
[ICoEdge::GetCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurve.md)  
[ICoEdge::IGetCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetCurve.md)  
[ICoEdge::GetEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetEdge.md)  
[ICoEdge::IGetEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetEdge.md)  
[ICoEdge::GetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurveParams.md)  
[ICoEdge::IGetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetCurveParams.md)  
[IEdge::GetCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams2.md)  
[IEdge::IGetCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetCurveParams2.md)
