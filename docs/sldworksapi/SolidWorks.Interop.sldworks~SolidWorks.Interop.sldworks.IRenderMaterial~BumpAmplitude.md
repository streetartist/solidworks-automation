# BumpAmplitude Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpAmplitude`

Obsolete. Superseded by IRenderMaterial::BumpStrength.
Obsolete. Superseded by [IRenderMaterial::BumpStrength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpStrength.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BumpAmplitude As System.Double
```

```

Dim instance As IRenderMaterial
Dim value As System.Double
 
instance.BumpAmplitude = value
 
value = instance.BumpAmplitude
```

```

System.double BumpAmplitude {get; set;}
```

```

property System.double BumpAmplitude {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Amplitude

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
