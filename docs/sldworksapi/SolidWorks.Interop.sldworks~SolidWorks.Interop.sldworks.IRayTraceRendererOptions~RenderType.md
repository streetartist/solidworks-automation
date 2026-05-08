# RenderType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~RenderType`

Gets or sets whether to render with contour or cartoon lines.
Gets or sets whether to render with contour or cartoon lines.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RenderType As System.Integer
```

```

Dim instance As IRayTraceRendererOptions
Dim value As System.Integer
 
instance.RenderType = value
 
value = instance.RenderType
```

```

System.int RenderType {get; set;}
```

```

property System.int RenderType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Render type as defined by [swRayTraceRenderingType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRayTraceRenderingType_e.html)

Remarks

This property is only available when [IRayTraceRendererOptions::ContourCartoonRenderingEnabled](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourCartoonRenderingEnabled.md) is true.

Example

[Render Model (C#)](Render_Model_Example_CSharp.htm)  
[Render Model (VB.NET)](Render_Model_Example_VBNET.htm)  
[Render Model (VBA)](Render_Model_Example_VB.htm)  
[Update Graphics Area After Changing Render Options (C#)](Update_Graphics_After_Changing_Render_Options_Example_CSharp.htm)  
[Update Graphics Area After Changing Render Options (VB.NET)](Update_Graphics_After_Changing_Render_Options_Example_VBNET.htm)  
[Update Graphics Area After Changing Render Options (VBA)](Update_Graphics_After_Changing_Render_Options_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.md)  
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.md)  
[IRayTraceRendererOptions::HasCartoonEdges Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~HasCartoonEdges.md)  
[IRayTraceRendererOptions::HasCartoonShading Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~HasCartoonShading.md)  
[IRayTraceRendererOptions::ShadedContour Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ShadedContour.md)
