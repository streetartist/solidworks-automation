# NSamples Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~NSamples`

Gets or sets the number of samples used to calculate the contribution of the glossy component for illuminating the appearance.
Gets or sets the number of samples used to calculate the contribution of the glossy component for illuminating the appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property NSamples As System.Double
```

```

Dim instance As IRenderMaterial
Dim value As System.Double
 
instance.NSamples = value
 
value = instance.NSamples
```

```

System.double NSamples {get; set;}
```

```

property System.double NSamples {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Number of samples used to calculate the contribution of the glossy component

Remarks

Increasing the sampling rate reduces artifacts but reduces performance. This property is available when the type of material is Satin Finish, Accurate reflections is selected, and Glossy is non-zero.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
