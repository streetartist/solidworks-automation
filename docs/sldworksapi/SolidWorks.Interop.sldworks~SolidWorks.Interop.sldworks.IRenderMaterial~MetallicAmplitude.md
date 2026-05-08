# MetallicAmplitude Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~MetallicAmplitude`

Gets or sets the amplitude of the metallic flakes for illuminating the appearance.
Gets or sets the amplitude of the metallic flakes for illuminating the appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MetallicAmplitude As System.Double
```

```

Dim instance As IRenderMaterial
Dim value As System.Double
 
instance.MetallicAmplitude = value
 
value = instance.MetallicAmplitude
```

```

System.double MetallicAmplitude {get; set;}
```

```

property System.double MetallicAmplitude {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Amplitude of the metallic flakes

Remarks

When the metallic amplitude is set to smaller values, the metallic flakes are flat. When set to larger values, the metallic flakes are irregular and high.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
