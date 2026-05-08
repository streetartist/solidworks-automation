# ImageHeight Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ImageHeight`

Gets or sets the height of the image.
Gets or sets the height of the image.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ImageHeight As System.Integer
```

```

Dim instance As IRayTraceRendererOptions
Dim value As System.Integer
 
instance.ImageHeight = value
 
value = instance.ImageHeight
```

```

System.int ImageHeight {get; set;}
```

```

property System.int ImageHeight {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Height, in pixels, of the image

Remarks

You can override the values set in this property and [IRayTraceRendererOptions::ImageWidth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ImageWidth.md) by specifying Width and Height in [IRayTraceRenderer::RenderToFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~RenderToFile.md).

Example

[Render Model (C#)](Render_Model_Example_CSharp.htm)  
[Render Model (VB.NET)](Render_Model_Example_VBNET.htm)  
[Render Model (VBA)](Render_Model_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.md)  
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.md)  
[IRayTraceRendererOptions::ImageFormat Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ImageFormat.md)  
[IRayTraceRendererOptions::DefaultImagePath Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~DefaultImagePath.md)
