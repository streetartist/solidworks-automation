# Reflection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting~Reflection`

Gets or sets the reflectivity of a surface.
Gets or sets the reflectivity of a surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Reflection As System.Double
```

```

Dim instance As IAppearanceSetting
Dim value As System.Double
 
instance.Reflection = value
 
value = instance.Reflection
```

```

System.double Reflection {get; set;}
```

```

property System.double Reflection {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

0 <= *reflectivity* <= 1, where 0 is for no reflection, and 1 is for a mirror reflection

Remarks

See SOLIDWORKS Help for more information about appearances.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAppearanceSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.md)  
[IAppearanceSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting_members.md)
