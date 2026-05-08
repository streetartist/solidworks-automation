# CausticQuality Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~CausticQuality`

Gets or sets the number of photons sampled at each pixel, which controls the quality of the caustics.
Gets or sets the number of photons sampled at each pixel, which controls the quality of the caustics.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CausticQuality As System.Integer
```

```

Dim instance As IRayTraceRendererOptions
Dim value As System.Integer
 
instance.CausticQuality = value
 
value = instance.CausticQuality
```

```

System.int CausticQuality {get; set;}
```

```

property System.int CausticQuality {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Number of photons sampled at each pixel

Remarks

Increasing the number of photons sampled at each pixel creates a smoother caustic effect at the expense of detail. Decreasing the number of photons results in a sharper caustic effect with increasing graininess.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.md)  
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.md)  
[IRayTraceRendererOptions::CausticAmount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~CausticAmount.md)  
[IRayTraceRendererOptions::DirectCaustics Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~DirectCaustics.md)
