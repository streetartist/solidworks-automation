# OverrideCenterOfMass Property (IMassPropertyOverrideOptions)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideCenterOfMass`

Gets or sets whether to override the calculated center of mass for the model currently being edited.
Gets or sets whether to override the calculated center of mass for the model currently being edited.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OverrideCenterOfMass As System.Boolean
```

```

Dim instance As IMassPropertyOverrideOptions
Dim value As System.Boolean
 
instance.OverrideCenterOfMass = value
 
value = instance.OverrideCenterOfMass
```

```

System.bool OverrideCenterOfMass {get; set;}
```

```

property System.bool OverrideCenterOfMass {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to override the calculated center of mass, false to not

Remarks

After setting this property to true, call [IMassPropertyOverrideOptions::SetOverrideCenterOfMassValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverrideCenterOfMassValue.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassPropertyOverrideOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions.md)  
[IMassPropertyOverrideOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions_members.md)  
[IMassProperty2::CenterOfMass Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~CenterOfMass.md)  
[IMassPropertyOverrideOptions::GetOverrideCenterOfMassValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~GetOverrideCenterOfMassValue.md)
