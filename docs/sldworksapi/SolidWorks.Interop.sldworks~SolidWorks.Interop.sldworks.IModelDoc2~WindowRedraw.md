# WindowRedraw Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~WindowRedraw`

Redraws the current window.
Redraws the current window.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub WindowRedraw() 
```

```

Dim instance As IModelDoc2
 
instance.WindowRedraw()
```

```

void WindowRedraw()
```

```

void WindowRedraw(); 
```

Remarks

The current window includes the FeatureManager design tree view and the graphics area or graphics areas if you are using the window splitter.

Example

[Insert a Note (VBA)](Insert_a_Note_Example_VB.htm)  
[Running or Attaching to a SOLIDWORKS Session (VBA)](SOLIDWORKS_Visible_or_BackGround_Example_VB.htm)  
[Anchor a Note (C#)](Anchor_a_Note_Example_CSharp.htm)  
[Anchor a Note (VB.NET)](Anchor_a_Note_Example_VBNET.htm)  
[Anchor a Note (VBA)](Anchor_a_Note_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::GraphicsRedraw2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md)  
[IModelView::DrawHighlightedItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DrawHighlightedItems.md)  
[IModelView::DrawTransparentFeatureTree Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DrawTransparentFeatureTree.md)  
[IModelView::SuppressWaitCursorDuringRedraw Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SuppressWaitCursorDuringRedraw.md)
