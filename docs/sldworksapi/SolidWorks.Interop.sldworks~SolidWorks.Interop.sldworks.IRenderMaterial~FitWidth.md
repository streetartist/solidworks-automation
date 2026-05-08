# FitWidth Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~FitWidth`

Gets or sets whether to stretch the width of the appearance texture to the selected entity when mapping the appearance.
Gets or sets whether to stretch the width of the appearance texture to the selected entity when mapping the appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FitWidth As System.Boolean
```

```

Dim instance As IRenderMaterial
Dim value As System.Boolean
 
instance.FitWidth = value
 
value = instance.FitWidth
```

```

System.bool FitWidth {get; set;}
```

```

property System.bool FitWidth {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to stretch the width of the appearance texture to the selected entity, false to not

Remarks

Call [IRenderMaterial::FitHeight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~FitHeight.md) to get or set whether to stretch the height of the appearance texture to the selected entity.

To stretch width and height of the appearance texture yourself, call [IRenderMaterial::Width](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Width.md) and [IRenderMaterial::Height](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Height.md).

Example

See the "Add Decal" examples in [IRenderMaterial::FileName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~FileName.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
