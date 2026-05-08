# SpecularColor Property (IRenderMaterial)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SpecularColor`

Gets or sets the specular color for illuminating this appearance.
Gets or sets the specular color for illuminating this appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SpecularColor As System.Integer
```

```

Dim instance As IRenderMaterial
Dim value As System.Integer
 
instance.SpecularColor = value
 
value = instance.SpecularColor
```

```

System.int SpecularColor {get; set;}
```

```

property System.int SpecularColor {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

RGB value

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
