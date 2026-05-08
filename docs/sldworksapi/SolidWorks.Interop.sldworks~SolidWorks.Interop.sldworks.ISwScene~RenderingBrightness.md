# RenderingBrightness Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~RenderingBrightness`

Gets or sets the brightness contributed by the high dynamic range imaging (HDRI) environment.
Gets or sets the brightness contributed by the high dynamic range imaging (HDRI) environment.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RenderingBrightness As System.Double
```

```

Dim instance As ISwScene
Dim value As System.Double
 
instance.RenderingBrightness = value
 
value = instance.RenderingBrightness
```

```

System.double RenderingBrightness {get; set;}
```

```

property System.double RenderingBrightness {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Brightness

Remarks

This property is valid only when a ray-trace rendering engine is activated.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md)  
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.md)
