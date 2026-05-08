# GetCurve Method (ISilhouetteEdge)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge~GetCurve`

Gets the curve for this silhouette edge.
Gets the curve for this silhouette edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCurve() As Curve
```

```

Dim instance As ISilhouetteEdge
Dim value As Curve
 
value = instance.GetCurve()
```

```

Curve GetCurve()
```

```

Curve^ GetCurve(); 
```

#### Return Value

[Curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

Remarks

After getting the curve, then you can create annotations on that curve.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISilhouetteEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge.md)  
[ISilhouetteEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge_members.md)  
[ISilhouetteEdge::GetEndPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge~GetEndPoint.md)  
[ISilhouetteEdge::GetStartPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge~GetStartPoint.md)
