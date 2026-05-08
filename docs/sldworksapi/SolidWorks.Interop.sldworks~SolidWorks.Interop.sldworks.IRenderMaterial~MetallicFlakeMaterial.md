# MetallicFlakeMaterial Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~MetallicFlakeMaterial`

Gets or sets the metallic flake material for illuminating the appearance.
Gets or sets the metallic flake material for illuminating the appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MetallicFlakeMaterial As System.Integer
```

```

Dim instance As IRenderMaterial
Dim value As System.Integer
 
instance.MetallicFlakeMaterial = value
 
value = instance.MetallicFlakeMaterial
```

```

System.int MetallicFlakeMaterial {get; set;}
```

```

property System.int MetallicFlakeMaterial {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

- 0 = Aluminum

1 = Copper

2 = Gold

3 = Silver

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
