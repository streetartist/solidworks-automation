# UpdateViewDisplayGeometry Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UpdateViewDisplayGeometry`

Updates the displayed geometry for a drawing view.
Updates the displayed geometry for a drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub UpdateViewDisplayGeometry() 
```

```

Dim instance As IView
 
instance.UpdateViewDisplayGeometry()
```

```

void UpdateViewDisplayGeometry()
```

```

void UpdateViewDisplayGeometry(); 
```

Remarks

This method accesses new view geometry before Microsoft has repainted the window. For example, this can occur if you were changing the display mode of the drawing view from HLR to HLV and wanted immediate access to the polylines in that drawing view.

Because Microsoft controls repainting the window, you do not have access to your drawing view changes until control is returned. However, using this method immediately updates the view geometry for your purposes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetDisplayMode2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayMode2.md)  
[IView::SetDisplayMode3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayMode3.md)
