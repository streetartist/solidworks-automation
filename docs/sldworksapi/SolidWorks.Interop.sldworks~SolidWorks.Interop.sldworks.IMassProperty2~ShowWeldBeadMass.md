# ShowWeldBeadMass Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~ShowWeldBeadMass`

Gets or sets whether to calculate weld bead mass.
Gets or sets whether to calculate weld bead mass.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowWeldBeadMass As System.Boolean
```

```

Dim instance As IMassProperty2
Dim value As System.Boolean
 
instance.ShowWeldBeadMass = value
 
value = instance.ShowWeldBeadMass
```

```

System.bool ShowWeldBeadMass {get; set;}
```

```

property System.bool ShowWeldBeadMass {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to calculate weld bead mass, false to not

Remarks

After setting this property to true, you can use [IMassProperty2::WeldBeadMass](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~WeldBeadMass.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.md)  
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.md)
