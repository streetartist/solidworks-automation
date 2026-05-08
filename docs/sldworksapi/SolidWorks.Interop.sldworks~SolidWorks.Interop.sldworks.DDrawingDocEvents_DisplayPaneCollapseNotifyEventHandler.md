# DDrawingDocEvents_DisplayPaneCollapseNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_DisplayPaneCollapseNotifyEventHandler`

Fired when a display pane is collapsed in this drawing.
Fired when a display pane is collapsed in this drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DDrawingDocEvents_DisplayPaneCollapseNotifyEventHandler() As System.Integer
```

```

Dim instance As New DDrawingDocEvents_DisplayPaneCollapseNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DDrawingDocEvents_DisplayPaneCollapseNotifyEventHandler()
```

```

public delegate System.int DDrawingDocEvents_DisplayPaneCollapseNotifyEventHandler();
```

Remarks

If developing a C++ application, use [swDrawingDisplayPaneCollapseNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

Example

[Create Task Pane View Add-in (C#)](Create_TaskPaneView_Add-in_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DDrawingDocEvents\_DisplayPaneCollapseNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_DisplayPaneCollapseNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
