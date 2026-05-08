# Gamma Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~Gamma`

Gets or sets the value for midtones of the rendered image while preserving the extreme whites and blacks.
Gets or sets the value for midtones of the rendered image while preserving the extreme whites and blacks.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Gamma As System.Double
```

```

Dim instance As IRayTraceRendererOptions
Dim value As System.Double
 
instance.Gamma = value
 
value = instance.Gamma
```

```

System.double Gamma {get; set;}
```

```

property System.double Gamma {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Value for midtones of the rendered image

Remarks

Increasing the value for midtones lightens them; decreasing the value darkens them.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.md)  
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.md)
