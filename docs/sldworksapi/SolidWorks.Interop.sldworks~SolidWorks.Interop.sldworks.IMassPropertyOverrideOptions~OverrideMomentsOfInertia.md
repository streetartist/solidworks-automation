# OverrideMomentsOfInertia Property (IMassPropertyOverrideOptions)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideMomentsOfInertia`

Gets or sets whether to override the calculated moments of inertia for the model currently being edited.
Gets or sets whether to override the calculated moments of inertia for the model currently being edited.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OverrideMomentsOfInertia As System.Boolean
```

```

Dim instance As IMassPropertyOverrideOptions
Dim value As System.Boolean
 
instance.OverrideMomentsOfInertia = value
 
value = instance.OverrideMomentsOfInertia
```

```

System.bool OverrideMomentsOfInertia {get; set;}
```

```

property System.bool OverrideMomentsOfInertia {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to override the calculated moments of inertia, false to not

Remarks

After setting this property to true, call:

- [IMassPropertyOverrideOptions::SetOverrideMomentsOfInertiaValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverrideMomentsOfInertiaValue.md)

- [IMassPropertyOverrideOptions::SetOverridePrincipalAxesOrientation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverridePrincipalAxesOrientation.md)

- [IMassPropertyOverrideOptions::SetOverridePrincipalMomentsOfInertia](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverridePrincipalMomentsOfInertia.md)

Example

See the [IMassProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassPropertyOverrideOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions.md)  
[IMassPropertyOverrideOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions_members.md)  
[IMassProperty2::GetMomentOfInertia Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~GetMomentOfInertia.md)  
[IMassProperty2::PrincipalAxesOfInertia Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~PrincipalAxesOfInertia.md)  
[IMassProperty2::PrincipalMomentsOfInertia Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~PrincipalMomentsOfInertia.md)  
[IMassPropertyOverrideOptions::GetOverrideMomentsOfInertiaValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~GetOverrideMomentsOfInertiaValue.md)  
[IMassPropertyOverrideOptions::GetOverridePrincipalMomentsOfInertia Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~GetOverridePrincipalMomentsOfInertia.md)  
[IMassPropertyOverrideOptions::GetOverridePrincipalAxesOrientation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~GetOverridePrincipalAxesOrientation.md)
