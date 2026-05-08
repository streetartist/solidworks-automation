# DModelViewEvents_RenderLayer0NotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_RenderLayer0NotifyEventHandler`

Fired whenever SOLIDWORKS renders to Layer0.
Fired whenever SOLIDWORKS renders to Layer0.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DModelViewEvents_RenderLayer0NotifyEventHandler() As System.Integer
```

```

Dim instance As New DModelViewEvents_RenderLayer0NotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DModelViewEvents_RenderLayer0NotifyEventHandler()
```

```

public delegate System.int DModelViewEvents_RenderLayer0NotifyEventHandler();
```

Remarks

This event allows you to render the model instead of SOLIDWORKS rendering the model. If the return value from the event is S\_FALSE, then SOLIDWORKS will not render to Layer0, but will render to Layer1.

**NOTE:** When SOLIDWORKS renders to a frame, it renders two layers:

- Layer0: The model, usually shaded, but may be Fast HLR/LG and inactive sketch data.
- Layer2: Active sketch, annotations, and temporary graphic objects like the reference triad, View Orientation box, and the flyout FeatureManager design tree.

This event is not sent if [swViewRepaintNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) returns S\_FALSE. Also, if [swViewRenderLayer0Notify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) returns S\_FALSE, then [swViewBufferSwapNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) is not sent.

[BufferSwapNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_BufferSwapNotifyEventHandler.md) is fired after rendering to Layer0, depending on optimization**.** [GraphicsRenderPostNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_GraphicsRenderPostNotifyEventHandler.md) is always fired after rendering to Layer2.

Prior to the event, the graphics area is cleared and the model view's xform is set.

If developing a C++ application, use [swViewRenderLayer0Notify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DModelViewEvents\_RenderLayer0NotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_RenderLayer0NotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
