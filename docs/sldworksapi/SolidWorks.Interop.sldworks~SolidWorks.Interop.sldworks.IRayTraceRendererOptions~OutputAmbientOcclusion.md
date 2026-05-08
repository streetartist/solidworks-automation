# OutputAmbientOcclusion Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~OutputAmbientOcclusion`

Gets or sets whether to render with ambient occlusion.
Gets or sets whether to render with ambient occlusion.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OutputAmbientOcclusion As System.Boolean
```

```

Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean
 
instance.OutputAmbientOcclusion = value
 
value = instance.OutputAmbientOcclusion
```

```

System.bool OutputAmbientOcclusion {get; set;}
```

```

property System.bool OutputAmbientOcclusion {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to render with ambient occlusion, false to not

Remarks

Ambient occlusion is a global lighting method that adds realism to models by controlling the attenuation of ambient light due to occluded areas. Objects appear as they would on an overcast day.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.md)  
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.md)
