# CloseFinalRenderWindow Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~CloseFinalRenderWindow`

Closes the final render window, but leaves the preview window open.
Closes the final render window, but leaves the [preview window](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~DisplayPreviewWindow.md) open.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CloseFinalRenderWindow() As System.Boolean
```

```

Dim instance As IRayTraceRenderer
Dim value As System.Boolean
 
value = instance.CloseFinalRenderWindow()
```

```

System.bool CloseFinalRenderWindow()
```

```

System.bool CloseFinalRenderWindow(); 
```

#### Return Value

True if the final render window closed, false if it did not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRayTraceRenderer Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer.md)  
[IRayTraceRenderer Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer_members.md)  
[IRayTraceRenderer::CloseRayTraceRender Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~CloseRayTraceRender.md)
