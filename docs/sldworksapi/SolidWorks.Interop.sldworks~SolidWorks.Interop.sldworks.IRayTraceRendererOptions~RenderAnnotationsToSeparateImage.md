# RenderAnnotationsToSeparateImage Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~RenderAnnotationsToSeparateImage`

Gets or sets whether to render annotations and dimensions visible in the model to a separate image file.
Gets or sets whether to render annotations and dimensions visible in the model to a separate image file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RenderAnnotationsToSeparateImage As System.Boolean
```

```

Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean
 
instance.RenderAnnotationsToSeparateImage = value
 
value = instance.RenderAnnotationsToSeparateImage
```

```

System.bool RenderAnnotationsToSeparateImage {get; set;}
```

```

property System.bool RenderAnnotationsToSeparateImage {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to render annotations and dimensions visible in the model to a separate image file, false to not

Remarks

This property is only available when:

- [rendering to a file](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~RenderToFile.md). This property is not available when only [invoking the final render window](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.md).
- [IRayTraceRendererOptions::IncludeAnnotationsInRendering](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~IncludeAnnotationsInRendering.md) is set to true.

When this property is set to true, then SOLIDWORKS appends **\_1** to the name of the render file. For example, if you named the render file **abc.png**, then this property creates a file named **abc\_1.png** that contains only the annotations and dimensions visible in the model.

Example

[Render Annotations to Separate Image File (C#)](Render_Annotations_to_Separate_Image_File_Example_CSharp.htm)  
[Render Annotations to Separate Image File (VB.NET)](Render_Annotations_to_Separate_Image_File_Example_VBNET.htm)  
[Render Annotations to Separate Image File (VBA)](Render_Annotations_to_Separate_Image_File_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.md)  
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.md)
