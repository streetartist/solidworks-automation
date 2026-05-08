# RenderToFile Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~RenderToFile`

Saves the current view of the rendered model as an image to the specified file.
Saves the current view of the rendered model as an image to the specified file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RenderToFile( _
   ByVal ImageFileName As System.String, _
   ByVal Width As System.Integer, _
   ByVal Height As System.Integer _
) As System.Boolean
```

```

Dim instance As IRayTraceRenderer
Dim ImageFileName As System.String
Dim Width As System.Integer
Dim Height As System.Integer
Dim value As System.Boolean
 
value = instance.RenderToFile(ImageFileName, Width, Height)
```

```

System.bool RenderToFile( 
   System.string ImageFileName,
   System.int Width,
   System.int Height
)
```

```

System.bool RenderToFile( 
   System.String^ ImageFileName,
   System.int Width,
   System.int Height
) 
```

#### Parameters

*ImageFileName*
:   File path and name (see **Remarks**)

*Width*
:   Width of image in pixels (see **Remarks**)

*Height*
:   Height of image in pixels (see **Remarks**)

#### Return Value

True if the current view of the rendered model is saved, false if not

Remarks

Before calling this method:

- you can call [IRayTraceRendererOptions::ImageFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ImageFormat.md) to specify the image format in which to save the model and omit the file format extension when specifying ImageFileName.
- set [IRayTraceRendererOptions::IncludeAnnotationsInRendering](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~IncludeAnnotationsInRendering.md) to true to include annotations and dimensions visible in the model in the render file. You can also set [IRayTraceRendererOptions::RenderAnnotationsToSeparateImage](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~RenderAnnotationsToSeparateImage.md) to true to render the annotations and dimensions visible in the model to a separate image file.

You can override the values set in [IRayTraceRendererOptions::ImageWidth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ImageWidth.md) and [IRayTraceRendererOptions::ImageHeight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ImageHeight.md) by calling this method with specific values for Width and Height. Set Width and Height to 0 to use values specified by IRayTraceRendererOptions::ImageWidth and IRayTraceRendererOptions::ImageHeight.

After calling this method, call [IRayTraceRenderer::CloseRayTraceRender](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~CloseRayTraceRender.md).

Example

[Render Model (C#)](Render_Model_Example_CSharp.htm)  
[Render Model (VB.NET)](Render_Model_Example_VBNET.htm)  
[Render Model (VBA)](Render_Model_Example_VB.htm)  
[Include Note in Render File (C#)](Include_Note_in_Render_File_Example_CSharp.htm)  
[Include Note in Render File (VB.NET)](Include_Note_in_Render_File_Example_VBNET.htm)  
[Include Note in Render File (VBA)](Include_Note_in_Render_File_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRayTraceRenderer Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer.md)  
[IRayTraceRenderer Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer_members.md)  
[IRayTraceRenderer::InvokeFinalRender Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.md)  
[IRayTraceRendererOptions::UpdateGraphics Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~UpdateGraphics.md)
