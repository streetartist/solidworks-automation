# GraphicsRedraw Method (IModelView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw`

Redraws the specified region of or the entire SOLIDWORKS graphics window.
Redraws the specified region of or the entire SOLIDWORKS graphics window.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GraphicsRedraw( _
   ByVal Rect As System.Object _
) 
```

```

Dim instance As IModelView
Dim Rect As System.Object
 
instance.GraphicsRedraw(Rect)
```

```

void GraphicsRedraw( 
   System.object Rect
)
```

```

void GraphicsRedraw( 
   System.Object^ Rect
) 
```

#### Parameters

*Rect*
:   Array of four integers or longs indicating the boundary of the region in the SOLIDWORKS graphics window to redraw; if the array is empty, then the entire graphics window is redrawn

Remarks

This method forces the specified region or the entire SOLIDWORKS graphics window to be updated immediately when called.

Example

[Exclude Faces Before Flattening (C#)](Exclude_Faces_Before_Flattening_Example_CSharp.htm)  
[Exclude Faces Before Flattening (VB.NET)](Exclude_Faces_Before_Flattening_Example_VBNET.htm)  
[Exclude Faces Before Flattening (VBA)](Exclude_Faces_Before_Flattening_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)  
[IModelDoc2::WindowRedraw Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~WindowRedraw.md)  
[IModelView::DrawHighlightedItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DrawHighlightedItems.md)  
[IModelView::DrawTransparentFeatureTree Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DrawTransparentFeatureTree.md)  
[IModelView::SuppressWaitCursorDuringRedraw Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SuppressWaitCursorDuringRedraw.md)  
[IModelView::IGraphicsRedraw Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGraphicsRedraw.md)
