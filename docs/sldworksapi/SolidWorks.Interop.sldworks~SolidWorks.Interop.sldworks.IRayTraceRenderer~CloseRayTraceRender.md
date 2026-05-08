# CloseRayTraceRender Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~CloseRayTraceRender`

Closes both the preview and final render windows.
Closes both the [preview](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~DisplayPreviewWindow.md) and [final render windows](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~CloseFinalRenderWindow.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CloseRayTraceRender() As System.Boolean
```

```

Dim instance As IRayTraceRenderer
Dim value As System.Boolean
 
value = instance.CloseRayTraceRender()
```

```

System.bool CloseRayTraceRender()
```

```

System.bool CloseRayTraceRender(); 
```

#### Return Value

True if both the [preview](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~DisplayPreviewWindow.md) and [final render windows](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~CloseFinalRenderWindow.md) are closed, false if not

Remarks

When this method is called after calling [IRayTraceRenderer::Invoke FinalRender](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.md) or [IRayTraceRenderer::RenderToFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~RenderToFile.md), then both the preview and final render windows are closed.

To leave the preview render window open, call [IRayTraceRenderer::CloseFinalRenderWindow](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~CloseFinalRenderWindow.md) instead of calling IRayTraceRender::CloseRayTraceRender.

Example

[Render Model (C#)](Render_Model_Example_CSharp.htm)  
[Render Model (VB.NET)](Render_Model_Example_VBNET.htm)  
[Render Model (VBA)](Render_Model_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRayTraceRenderer Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer.md)  
[IRayTraceRenderer Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer_members.md)
