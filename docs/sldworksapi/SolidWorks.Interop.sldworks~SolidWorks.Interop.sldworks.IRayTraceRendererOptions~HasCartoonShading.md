# HasCartoonShading Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~HasCartoonShading`

Gets or sets whether to render with cartoon shading.
Gets or sets whether to render with cartoon shading.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property HasCartoonShading As System.Boolean
```

```

Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean
 
instance.HasCartoonShading = value
 
value = instance.HasCartoonShading
```

```

System.bool HasCartoonShading {get; set;}
```

```

property System.bool HasCartoonShading {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to render with cartoon shading, false to not

Remarks

This property is only available when [IRayTraceRendererOptions::ContourCartoonRenderingEnabled](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourCartoonRenderingEnabled.md) is true and [IRayTraceRendererOptions::RenderType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~RenderType.md) is swRayTraceRenderingType\_e.swRayTraceCartoon.

| To set cartoon... | Set [IRayTraceRendererOptions::HasCartoonEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~HasCartoonEdges.md) to... | Set IRayTraceRendererOptions::HasCartoonShading to... |
| --- | --- | --- |
| Edges | True | False |
| Shading | False | True |
| Edges and shading | True | True |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.md)  
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.md)  
[IRayTraceRendererOptions::ContourLineColor Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourLineColor.md)  
[IRayTraceRendererOptions::ContourLineThickness Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourLineThickness.md)
