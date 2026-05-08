# DModelViewEvents_GraphicsRenderPostNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_GraphicsRenderPostNotifyEventHandler`

Fired after all SOLIDWORKS graphics are drawn, including SOLIDWORKS model, sketch, dimension, and annotation graphics.
Fired after all SOLIDWORKS graphics are drawn, including SOLIDWORKS model, sketch, dimension, and annotation graphics.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DModelViewEvents_GraphicsRenderPostNotifyEventHandler() As System.Integer
```

```

Dim instance As New DModelViewEvents_GraphicsRenderPostNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DModelViewEvents_GraphicsRenderPostNotifyEventHandler()
```

```

public delegate System.int DModelViewEvents_GraphicsRenderPostNotifyEventHandler();
```

Remarks

This event:

- is always fired after rendering to Layer2. Depending on optimization:
  - [RenderLayer0Notify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_RenderLayer0NotifyEventHandler.md) is fired when SOLIDWORKS renders to Layer0.
  - [BufferSwapNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_BufferSwapNotifyEventHandler.md) is fired after rendering to Layer0**.**
- allows third-party applications to draw graphics in the SOLIDWORKS model window without worrying about SOLIDWORKS graphics being drawn over them.
- does not support depth buffering.

If developing a C++ application, use [swViewGraphicsRenderPostNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DModelViewEvents\_GraphicsRenderPostNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_GraphicsRenderPostNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
