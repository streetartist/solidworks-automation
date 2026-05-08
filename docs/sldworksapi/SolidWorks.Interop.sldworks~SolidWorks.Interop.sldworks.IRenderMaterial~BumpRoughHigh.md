# BumpRoughHigh Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpRoughHigh`

Gets or sets the high threshold of the surface finish for this appearance.
Gets or sets the high threshold of the surface finish for this appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BumpRoughHigh As System.Double
```

```

Dim instance As IRenderMaterial
Dim value As System.Double
 
instance.BumpRoughHigh = value
 
value = instance.BumpRoughHigh
```

```

System.double BumpRoughHigh {get; set;}
```

```

property System.double BumpRoughHigh {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

High threshold

Remarks

The high threshold is an absolute distance from the neutral surface (amplitude = 0). The high threshold extends further away from the neutral surface than the low threshold.

For positive [amplitude](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpAmplitude.md), the high threshold flattens the peaks of the surface finish. For negative amplitude, the high threshold flattens the valleys of the surface finish.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
