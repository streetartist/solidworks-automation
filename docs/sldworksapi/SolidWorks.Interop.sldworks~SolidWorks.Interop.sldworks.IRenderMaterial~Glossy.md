# Glossy Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Glossy`

Gets or sets the specular factor of the lights reflected by the appearance.
Gets or sets the specular factor of the lights reflected by the appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Glossy As System.Double
```

```

Dim instance As IRenderMaterial
Dim value As System.Double
 
instance.Glossy = value
 
value = instance.Glossy
```

```

System.double Glossy {get; set;}
```

```

property System.double Glossy {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Specular factor of the lights reflected by the appearance

Remarks

Increasing Glossy makes reflections more visible.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
