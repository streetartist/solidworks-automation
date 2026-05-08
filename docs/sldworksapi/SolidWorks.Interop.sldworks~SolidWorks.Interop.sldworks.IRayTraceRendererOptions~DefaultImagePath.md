# DefaultImagePath Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~DefaultImagePath`

Gets or sets the default path to which to save the image.
Gets or sets the default path to which to save the image.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DefaultImagePath As System.String
```

```

Dim instance As IRayTraceRendererOptions
Dim value As System.String
 
instance.DefaultImagePath = value
 
value = instance.DefaultImagePath
```

```

System.string DefaultImagePath {get; set;}
```

```

property System.String^ DefaultImagePath {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Path to which to save the image

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.md)  
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.md)  
[IRayTraceRendererOptions::ImageFormat Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ImageFormat.md)  
[IRayTraceRendererOptions::ImageHeight Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ImageHeight.md)  
[IRayTraceRendererOptions::ImageWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ImageWidth.md)
