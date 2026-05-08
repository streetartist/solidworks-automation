# Ambient Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Ambient`

Gets or sets the ambient light intensity for illuminating this appearance.
Gets or sets the ambient light intensity for illuminating this appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Ambient As System.Double
```

```

Dim instance As IRenderMaterial
Dim value As System.Double
 
instance.Ambient = value
 
value = instance.Ambient
```

```

System.double Ambient {get; set;}
```

```

property System.double Ambient {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Ambient light intensity

Remarks

The scene should contain an ambient light.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
