# WeldBeadMass Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~WeldBeadMass`

Gets the weld bead mass.
Gets the weld bead mass.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property WeldBeadMass As System.Double
```

```

Dim instance As IMassProperty2
Dim value As System.Double
 
value = instance.WeldBeadMass
```

```

System.double WeldBeadMass {get;}
```

```

property System.double WeldBeadMass {
   System.double get();
}
```

#### Property Value

Weld bead mass

Remarks

This property is valid only if [IMassProperty2::ShowWeldBeadMass](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~ShowWeldBeadMass.md) is set to true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.md)  
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.md)
