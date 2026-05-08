# UseSolidWorksViewAspectRatio Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~UseSolidWorksViewAspectRatio`

Gets or sets whether to use the aspect ratio of the SOLIDWORKS view for ray-trace rendering engine preview and final renders.
Gets or sets whether to use the aspect ratio of the SOLIDWORKS view for ray-trace rendering engine preview and final renders.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseSolidWorksViewAspectRatio As System.Boolean
```

```

Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean
 
instance.UseSolidWorksViewAspectRatio = value
 
value = instance.UseSolidWorksViewAspectRatio
```

```

System.bool UseSolidWorksViewAspectRatio {get; set;}
```

```

property System.bool UseSolidWorksViewAspectRatio {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use the aspect ratio of the SOLIDWORKS view for ray-trace rendering engine preview and final renders, false to not

Example

See the [IRayTraceRendererOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.md)  
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.md)  
[IRayTraceRendererOptions::UseSceneBackgroundImageAspectRatio Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~UseSceneBackgroundImageAspectRatio.md)
