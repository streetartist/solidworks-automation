# DModelViewEvents_BufferSwapNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_BufferSwapNotifyEventHandler`

Fired from the model view immediately before the buffers are swapped when rendering shaded graphics in OpenGL.
Fired from the model view immediately before the buffers are swapped when rendering shaded graphics in OpenGL.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DModelViewEvents_BufferSwapNotifyEventHandler() As System.Integer
```

```

Dim instance As New DModelViewEvents_BufferSwapNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DModelViewEvents_BufferSwapNotifyEventHandler()
```

```

public delegate System.int DModelViewEvents_BufferSwapNotifyEventHandler();
```

Remarks

The OpenGL context contains matrices such that graphics are drawn correctly relative to the part or top-level assembly, but not any components within the assembly. This event is also sent when the model is in HLR or HLV mode and being dynamically rotated.

This event is sent for any other wireframe repainting. (GDI is used for all other wireframe painting). You can determine if a model is shaded by using [IModelView::GetDisplayState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetDisplayState.md).

This event is fired after rendering to Layer0.

**NOTE:** When SOLIDWORKS renders to a frame, it renders two layers:

- Layer0: The model, usually shaded, but may be Fast HLR/LG and inactive sketch data.
- Layer2: Active sketch, annotations, and temporary graphic objects like the reference triad, View Orientation box, and the flyout FeatureManager design tree.

[RenderLayer0Notify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_RenderLayer0NotifyEventHandler.md) is fired when SOLIDWORKS renders to Layer0, depending on optimization. [GraphicsRenderPostNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_GraphicsRenderPostNotifyEventHandler.md) is always fired after rendering to Layer2.

If developing a C++ application, use [swViewBufferSwapNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DModelViewEvents\_BufferSwapNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_BufferSwapNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
