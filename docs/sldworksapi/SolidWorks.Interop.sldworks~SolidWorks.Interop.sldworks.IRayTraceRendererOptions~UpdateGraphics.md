# UpdateGraphics Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~UpdateGraphics`

Updates the graphics area.
Updates the graphics area.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub UpdateGraphics() 
```

```

Dim instance As IRayTraceRendererOptions
 
instance.UpdateGraphics()
```

```

void UpdateGraphics()
```

```

void UpdateGraphics(); 
```

Remarks

To visually verify your changes after changing a model's ray-trace rendering engine's options and before rendering the model, call this method.

Example

[Update Graphics Area After Changing Render Options (C#)](Update_Graphics_After_Changing_Render_Options_Example_CSharp.htm)  
[Update Graphics Area After Changing Render Options (VB.NET)](Update_Graphics_After_Changing_Render_Options_Example_VBNET.htm)  
[Update Graphics Area After Changing Render Options (VBA)](Update_Graphics_After_Changing_Render_Options_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.md)  
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.md)  
[IRayTraceRenderer::InvokeFinalRender Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.md)  
[IRayTraceRenderer::RenderToFile Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~RenderToFile.md)
