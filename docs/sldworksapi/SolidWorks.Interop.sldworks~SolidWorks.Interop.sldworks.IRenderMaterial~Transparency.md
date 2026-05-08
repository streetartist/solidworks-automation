# Transparency Property (IRenderMaterial)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Transparency`

Gets or sets the degree to which a material allows light to pass through for illuminating the appearance.
Gets or sets the degree to which a material allows light to pass through for illuminating the appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Transparency As System.Double
```

```

Dim instance As IRenderMaterial
Dim value As System.Double
 
instance.Transparency = value
 
value = instance.Transparency
```

```

System.double Transparency {get; set;}
```

```

property System.double Transparency {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Degree to which a material allows light to pass through

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
