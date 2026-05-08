# BumpRoughLow Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpRoughLow`

Gets or sets the low threshold of the surface finish for this appearance.
Gets or sets the low threshold of the surface finish for this appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BumpRoughLow As System.Double
```

```

Dim instance As IRenderMaterial
Dim value As System.Double
 
instance.BumpRoughLow = value
 
value = instance.BumpRoughLow
```

```

System.double BumpRoughLow {get; set;}
```

```

property System.double BumpRoughLow {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Low threshold of the surface finish

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
