# Diffuse Property (IAppearanceSetting)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting~Diffuse`

Gets or sets the intensity of light on a surface.
Gets or sets the intensity of light on a surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Diffuse As System.Double
```

```

Dim instance As IAppearanceSetting
Dim value As System.Double
 
instance.Diffuse = value
 
value = instance.Diffuse
```

```

System.double Diffuse {get; set;}
```

```

property System.double Diffuse {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

0 <= *diffuseness* <= 1

Remarks

See SOLIDWORKS Help for more information about appearances.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAppearanceSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.md)  
[IAppearanceSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting_members.md)
