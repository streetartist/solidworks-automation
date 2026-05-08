# DirectCaustics Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~DirectCaustics`

Gets or sets whether to enable direct caustics in the final render.
Gets or sets whether to enable direct caustics in the [final render](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DirectCaustics As System.Boolean
```

```

Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean
 
instance.DirectCaustics = value
 
value = instance.DirectCaustics
```

```

System.bool DirectCaustics {get; set;}
```

```

property System.bool DirectCaustics {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to enable direct caustics in the final render, false to not

Remarks

Direct caustics are only visible in the final render and only when reflected off a floor appearance or physical geometry using a spot or point light. The light bounces off or filters through the model creating a bright pattern on the floor.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.md)  
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.md)  
[IRayTraceRendererOptions::CausticAmount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~CausticAmount.md)  
[IRayTraceRendererOptions::CausticQuality Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~CausticQuality.md)  
[IRayTraceRendererOptions::FinalRenderQuality Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~FinalRenderQuality.md)  
[IRayTraceRendererOptions::PreviewRenderQuality Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~PreviewRenderQuality.md)
