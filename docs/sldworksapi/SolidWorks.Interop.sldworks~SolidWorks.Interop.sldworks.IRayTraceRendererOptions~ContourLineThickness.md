# ContourLineThickness Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourLineThickness`

Gets or sets the thickness of contour lines.
Gets or sets the thickness of contour lines.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ContourLineThickness As System.Integer
```

```

Dim instance As IRayTraceRendererOptions
Dim value As System.Integer
 
instance.ContourLineThickness = value
 
value = instance.ContourLineThickness
```

```

System.int ContourLineThickness {get; set;}
```

```

property System.int ContourLineThickness {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Thickness, in pixels, of contour lines

Remarks

This property is only available when [IRayTraceRendererOptions::ContourCartoonRenderingEnabled](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourCartoonRenderingEnabled.md) is true.

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
[IRayTraceRendererOptions::ContourLineColor Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourLineColor.md)
