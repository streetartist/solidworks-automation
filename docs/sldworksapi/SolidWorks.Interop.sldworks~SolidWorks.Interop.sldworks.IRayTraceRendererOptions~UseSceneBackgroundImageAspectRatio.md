# UseSceneBackgroundImageAspectRatio Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~UseSceneBackgroundImageAspectRatio`

Gets or sets whether to use the aspect ratio of the scene's background image for ray-trace rendering engine preview and final renders.
Gets or sets whether to use the aspect ratio of the scene's background image for ray-trace rendering engine preview and final renders.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseSceneBackgroundImageAspectRatio As System.Boolean
```

```

Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean
 
instance.UseSceneBackgroundImageAspectRatio = value
 
value = instance.UseSceneBackgroundImageAspectRatio
```

```

System.bool UseSceneBackgroundImageAspectRatio {get; set;}
```

```

property System.bool UseSceneBackgroundImageAspectRatio {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use the aspect ratio of the scene's background image for ray-trace rendering engine preview and final renders, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.md)  
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.md)  
[IRayTraceRendererOptions::UseSolidWorksViewAspectRatio Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~UseSolidWorksViewAspectRatio.md)
