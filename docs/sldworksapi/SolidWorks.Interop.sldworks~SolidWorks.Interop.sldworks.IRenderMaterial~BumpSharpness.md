# BumpSharpness Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpSharpness`

Gets or sets the sharpness, which influences the shape of the surface finish, of this appearance.
Gets or sets the sharpness, which influences the shape of the surface finish, of this appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BumpSharpness As System.Double
```

```

Dim instance As IRenderMaterial
Dim value As System.Double
 
instance.BumpSharpness = value
 
value = instance.BumpSharpness
```

```

System.double BumpSharpness {get; set;}
```

```

property System.double BumpSharpness {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Sharpness

Remarks

A higher sharpness value retains the original shape of the surface finish; a lower sharpness value filters (smoothens) the surface-finish details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
