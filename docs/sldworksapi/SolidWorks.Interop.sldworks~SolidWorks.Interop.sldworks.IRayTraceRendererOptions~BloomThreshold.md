# BloomThreshold Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~BloomThreshold`

Gets or sets the level of brightness or emissiveness to which bloom effect is applied.
Gets or sets the level of brightness or emissiveness to which bloom effect is applied.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BloomThreshold As System.Integer
```

```

Dim instance As IRayTraceRendererOptions
Dim value As System.Integer
 
instance.BloomThreshold = value
 
value = instance.BloomThreshold
```

```

System.int BloomThreshold {get; set;}
```

```

property System.int BloomThreshold {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Brightness or emissiveness to which bloom effect is applied

Remarks

Bloom effect is visible in the [final rendering](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.md) only, not in the [preview](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~DisplayPreviewWindow.md). See the SOLIDWORKS Help for details about bloom effect.

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
[IRayTraceRendererOptions::BloomEnabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~BloomEnabled.md)  
[IRayTraceRendererOptions::BloomRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~BloomRadius.md)
