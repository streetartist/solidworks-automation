# PatternScale Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~PatternScale`

Gets or sets the pattern scale of procedural textures for mapping the appearance.
Gets or sets the pattern scale of procedural textures for mapping the appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PatternScale As System.Double
```

```

Dim instance As IRenderMaterial
Dim value As System.Double
 
instance.PatternScale = value
 
value = instance.PatternScale
```

```

System.double PatternScale {get; set;}
```

```

property System.double PatternScale {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Pattern scale

Remarks

A procedural texture is one where you only have control over the colors in the material and the size of the material (for example, colored marble or cherry wood).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
