# SpecularSpread Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting~SpecularSpread`

Gets or sets the blurriness of reflections on a surface.
Gets or sets the blurriness of reflections on a surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SpecularSpread As System.Double
```

```

Dim instance As IAppearanceSetting
Dim value As System.Double
 
instance.SpecularSpread = value
 
value = instance.SpecularSpread
```

```

System.double SpecularSpread {get; set;}
```

```

property System.double SpecularSpread {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

0 <= specular\_spread <= 1; valid only when [IAppearanceSetting::Specular](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting~Specular.md) > 0 and [IAppearanceSetting::SpecularColor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting~SpecularColor.md) > 0 (not black)

Remarks

See SOLIDWORKS Help for more information about appearances.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAppearanceSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.md)  
[IAppearanceSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting_members.md)
