# SetDisplayTangentEdges2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayTangentEdges2`

Sets the tangent edge display mode of the drawing view.
Sets the tangent edge display mode of the drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetDisplayTangentEdges2( _
   ByVal DisplayIn As System.Integer _
) 
```

```

Dim instance As IView
Dim DisplayIn As System.Integer
 
instance.SetDisplayTangentEdges2(DisplayIn)
```

```

void SetDisplayTangentEdges2( 
   System.int DisplayIn
)
```

```

void SetDisplayTangentEdges2( 
   System.int DisplayIn
) 
```

#### Parameters

*DisplayIn*
:   Tangent edge display mode as defined in [swDisplayTangentEdges\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDisplayTangentEdges_e.html)

Remarks

Tangent edges are the transition lines between, for example, a blend and a face.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetDisplayTangentEdges2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayTangentEdges2.md)  
[IView::GetDisplayEdgesInShadedMode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayEdgesInShadedMode.md)  
[IView::GetDisplayMode2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayMode2.md)  
[IView::GetUseParentDisplayMode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetUseParentDisplayMode.md)  
[IView::UpdateViewDisplayGeometry Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UpdateViewDisplayGeometry.md)
