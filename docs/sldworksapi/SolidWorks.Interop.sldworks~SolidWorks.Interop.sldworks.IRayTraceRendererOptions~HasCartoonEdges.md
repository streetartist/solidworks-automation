# HasCartoonEdges Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~HasCartoonEdges`

Gets or sets whether to render with cartoon edges.
Gets or sets whether to render with cartoon edges.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property HasCartoonEdges As System.Boolean
```

```

Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean
 
instance.HasCartoonEdges = value
 
value = instance.HasCartoonEdges
```

```

System.bool HasCartoonEdges {get; set;}
```

```

property System.bool HasCartoonEdges {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to render with cartoon edges, false to not

Remarks

This property is only available when [IRayTraceRendererOptions::ContourCartoonRenderingEnabled](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourCartoonRenderingEnabled.md) is true and [IRayTraceRendererOptions::RenderType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~RenderType.md) is swRayTraceRenderingType\_e.swRayTraceCartoon.

| To set cartoon... | Set IRayTraceRendererOptions::HasCartoonEdges to... | Set [IRayTraceRendererOptions::HasCartoonShading](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~HasCartoonShading.md) to... |
| --- | --- | --- |
| Edges | True | False |
| Shading | False | True |
| Edges and shading | True | True |

Example

[Update Graphics Area After Changing Render Options (C#)](Update_Graphics_After_Changing_Render_Options_Example_CSharp.htm)  
[Update Graphics Area After Changing Render Options (VB.NET)](Update_Graphics_After_Changing_Render_Options_Example_VBNET.htm)  
[Update Graphics Area After Changing Render Options (VBA)](Update_Graphics_After_Changing_Render_Options_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.md)  
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.md)  
[IRayTraceRendererOptions::ContourLineColor Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourLineColor.md)  
[IRayTraceRendererOptions::ContourLineThickness Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourLineThickness.md)
