# NumberOfRefractions Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NumberOfRefractions`

Gets or sets the number of refractions in the final render.
Gets or sets the number of refractions in the [final render](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property NumberOfRefractions As System.Integer
```

```

Dim instance As IRayTraceRendererOptions
Dim value As System.Integer
 
instance.NumberOfRefractions = value
 
value = instance.NumberOfRefractions
```

```

System.int NumberOfRefractions {get; set;}
```

```

property System.int NumberOfRefractions {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

0 <= Number of refractions <= 32

Remarks

This property is only available when [IRayTraceRendererOptions::CustomRenderSettings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~CustomRenderSettings.md) is true.

The number of refractions impacts rendering performance, so only use a high number of refractions to correctly see objects in the rendering.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.md)  
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.md)  
[IRayTraceRendererOptions::NumberOfReflections Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NumberOfReflections.md)
