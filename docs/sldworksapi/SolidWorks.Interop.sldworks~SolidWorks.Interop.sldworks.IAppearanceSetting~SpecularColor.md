# SpecularColor Property (IAppearanceSetting)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting~SpecularColor`

Gets or sets the color of reflected highlights for a specular component.
Gets or sets the color of reflected highlights for a specular component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SpecularColor As System.Integer
```

```

Dim instance As IAppearanceSetting
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

Color of reflected highlights; valid only when [IAppearanceSetting::SpecularSpread](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting~SpecularSpread.md) > 0 and [IAppearanceSetting::Specular](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting~Specular.md) > 0 (see **Remarks**)

Remarks

*specular\_color* = MAX(MIN(*red\_rgb\_value*,255),0) + MAX(MIN(*green\_rgb\_value*,255),0)\*16\*16 + MAX(MIN(*blue\_rgb\_value*,255),0)\*16\*16\*16\*16

See SOLIDWORKS Help for more information about appearances.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAppearanceSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.md)  
[IAppearanceSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting_members.md)
