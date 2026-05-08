# FinalRenderQuality Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~FinalRenderQuality`

Gets or sets quality of the final render.
Gets or sets quality of the [final render](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FinalRenderQuality As System.Integer
```

```

Dim instance As IRayTraceRendererOptions
Dim value As System.Integer
 
instance.FinalRenderQuality = value
 
value = instance.FinalRenderQuality
```

```

System.int FinalRenderQuality {get; set;}
```

```

property System.int FinalRenderQuality {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Quality of final render as defined in [swRayTraceRenderQuality\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRayTraceRenderQuality_e.html)

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
[IRayTraceRendererOptions::PreviewRenderQuality Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~PreviewRenderQuality.md)  
[IRayTraceRendererOptions::DirectCaustics Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~DirectCaustics.md)
