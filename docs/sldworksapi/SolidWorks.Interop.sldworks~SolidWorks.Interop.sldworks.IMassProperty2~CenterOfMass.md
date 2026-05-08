# CenterOfMass Property (IMassProperty2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~CenterOfMass`

Gets the center of mass of selected components/bodies.
Gets the center of mass of selected components/bodies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property CenterOfMass As System.Object
```

```

Dim instance As IMassProperty2
Dim value As System.Object
 
value = instance.CenterOfMass
```

```

System.object CenterOfMass {get;}
```

```

property System.Object^ CenterOfMass {
   System.Object^ get();
}
```

#### Property Value

Array of three doubles of the x, y, and z coordinates of the center of mass

Remarks

If [IMassPropertyOverrideOptions::OverrideCenterOfMass](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideCenterOfMass.md) is true or [IMassProperty2::IncludeHiddenBodiesOrComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~IncludeHiddenBodiesOrComponents.md) is reset, then call [IMassProperty2::Recalculate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~Recalculate.md) before using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.md)  
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.md)  
[IMassPropertyOverrideOptions::SetOverrideCenterOfMassValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverrideCenterOfMassValue.md)  
[IMassProeprtyOverrideOptions::GetOverrideCenterOfMassValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~GetOverrideCenterOfMassValue.md)
