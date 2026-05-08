# GetDisplayEdgesInShadedMode Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayEdgesInShadedMode`

Gets whether to display the edges in this when the drawing view is in shaded mode.
Gets whether to display the edges in this when the drawing view is in shaded mode.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDisplayEdgesInShadedMode() As System.Boolean
```

```

Dim instance As IView
Dim value As System.Boolean
 
value = instance.GetDisplayEdgesInShadedMode()
```

```

System.bool GetDisplayEdgesInShadedMode()
```

```

System.bool GetDisplayEdgesInShadedMode(); 
```

#### Return Value

True if the edges are displayed when the view is in shaded mode, false if not

Remarks

|  |  |
| --- | --- |
| **To...** | **Then use...** |
| Determine whether this view is displayed with faceted or precise geometry | [IView::GetFacettedHlrDisplay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFacettedHlrDisplay.md) |
| Determine the display mode of a drawing view | [IView::GetDisplayMode2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayMode2.md) |
| Set the display mode of a drawing view | [IView::SetDisplayMode3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayMode3.md) |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetDisplayTangentEdges2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayTangentEdges2.md)  
[IView::GetUseParentDisplayMode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetUseParentDisplayMode.md)  
[IView::SetDisplayTangentEdges2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayTangentEdges2.md)  
[IView::UpdateViewDisplayGeometry Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UpdateViewDisplayGeometry.md)
