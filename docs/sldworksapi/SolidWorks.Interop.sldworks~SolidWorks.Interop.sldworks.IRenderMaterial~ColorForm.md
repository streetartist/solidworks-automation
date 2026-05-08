# ColorForm Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~ColorForm`

Gets or sets the number of colors required to describe the appearance .
Gets or sets the number of colors required to describe the appearance .

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ColorForm As System.Integer
```

```

Dim instance As IRenderMaterial
Dim value As System.Integer
 
instance.ColorForm = value
 
value = instance.ColorForm
```

```

System.int ColorForm {get; set;}
```

```

property System.int ColorForm {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Number of colors as defined by [swRenderMaterialColorForms\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRenderMaterialColorForms_e.html)

Remarks

For example, blue glass is defined by two colors. To see the corresponding user-interface controls, open a model to which the blue glass appearance has been applied. Edit the blue glass appearance to open the Appearances PropertyManager page. Two color controls, Current Color1 and Current Color2, are displayed under Color.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
