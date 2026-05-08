# Transparent Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting~Transparent`

Gets or sets the degree to which light can pass through a surface.
Gets or sets the degree to which light can pass through a surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Transparent As System.Double
```

```

Dim instance As IAppearanceSetting
Dim value As System.Double
 
instance.Transparent = value
 
value = instance.Transparent
```

```

System.double Transparent {get; set;}
```

```

property System.double Transparent {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

0 <= *transparency* <= 100, where 0 is for total opaqueness, and 100 is for total transparency

Remarks

See SOLIDWORKS Help for more information about appearances.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAppearanceSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.md)  
[IAppearanceSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting_members.md)
