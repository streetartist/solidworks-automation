# IncludeAnnotationsInRendering Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~IncludeAnnotationsInRendering`

Gets or sets whether to include annotations and dimensions visible in the model when rendering to a file.
Gets or sets whether to include annotations and dimensions visible in the model when [rendering to a file](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~RenderToFile.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IncludeAnnotationsInRendering As System.Boolean
```

```

Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean
 
instance.IncludeAnnotationsInRendering = value
 
value = instance.IncludeAnnotationsInRendering
```

```

System.bool IncludeAnnotationsInRendering {get; set;}
```

```

property System.bool IncludeAnnotationsInRendering {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to include annotations and dimensions visible in the model when rendering to a file, false to not

Remarks

This property is only available when rendering to a file; this property is not available when only [invoking the final render window](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.md).

To render the annotations and dimensions visible in the model to a separate image file, call [IRayTraceRendererOptions::RenderAnnotationsToSeparateImage](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~RenderAnnotationsToSeparateImage.md).

Example

[Include Note in Render File (C#)](Include_Note_in_Render_File_Example_CSharp.htm)  
[Include Note in Render File (VB.NET)](Include_Note_in_Render_File_Example_VBNET.htm)  
[Include Note in Render File (VBA)](Include_Note_in_Render_File_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.md)  
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.md)
