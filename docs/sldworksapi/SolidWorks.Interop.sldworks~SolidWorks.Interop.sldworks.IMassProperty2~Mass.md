# Mass Property (IMassProperty2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~Mass`

Gets the mass of selected components/bodies.
Gets the mass of selected components/bodies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Mass As System.Double
```

```

Dim instance As IMassProperty2
Dim value As System.Double
 
value = instance.Mass
```

```

System.double Mass {get;}
```

```

property System.double Mass {
   System.double get();
}
```

#### Property Value

Mass

Remarks

If [IMassPropertyOverrideOptions::OverrideMass](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideMass.md) is true or [IMassProperty2::IncludeHiddenBodiesOrComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~IncludeHiddenBodiesOrComponents.md) is reset, then call [IMassProperty2::Recalculate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~Recalculate.md) before using this property.

Example

See the [IMassProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.md)  
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.md)  
[IMassPropertyOverrideOptions::SetOverrideMassValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverrideMassValue.md)  
[IMassPropertyOverrideOptions::GetOverrideMassValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~GetOverrideMassValue.md)
