# SecondaryColor Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SecondaryColor`

Gets or sets the secondary color of the appearance.
Gets or sets the secondary color of the appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SecondaryColor As System.Integer
```

```

Dim instance As IRenderMaterial
Dim value As System.Integer
 
instance.SecondaryColor = value
 
value = instance.SecondaryColor
```

```

System.int SecondaryColor {get; set;}
```

```

property System.int SecondaryColor {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

RGB value

Remarks

This property corresponds to the Current Color 2 control on the Color/Image tab of the Appearances PropertyManager page.

To get or set:

- Current Color 1, call [IRenderMaterial::PrimaryColor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~PrimaryColor.md).
- Current Color 3, call [IRenderMaterial::TertiaryColor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~TertiaryColor.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
