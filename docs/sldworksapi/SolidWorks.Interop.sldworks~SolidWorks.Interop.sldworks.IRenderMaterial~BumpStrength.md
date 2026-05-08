# BumpStrength Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpStrength`

Gets or sets the amplitude of the surface layer for this appearance.
Gets or sets the amplitude of the surface layer for this appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BumpStrength As System.Double
```

```

Dim instance As IRenderMaterial
Dim value As System.Double
 
instance.BumpStrength = value
 
value = instance.BumpStrength
```

```

System.double BumpStrength {get; set;}
```

```

property System.double BumpStrength {
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
