# GetOverridePrincipalMomentsOfInertia Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~GetOverridePrincipalMomentsOfInertia`

Gets the override principal moments of inertia.
Gets the override principal moments of inertia.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetOverridePrincipalMomentsOfInertia() As System.Object
```

```

Dim instance As IMassPropertyOverrideOptions
Dim value As System.Object
 
value = instance.GetOverridePrincipalMomentsOfInertia()
```

```

System.object GetOverridePrincipalMomentsOfInertia()
```

```

System.Object^ GetOverridePrincipalMomentsOfInertia(); 
```

#### Return Value

Array of three doubles of the principal moments of inertia: **[** Px, Py, Pz **]**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassPropertyOverrideOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions.md)  
[IMassPropertyOverrideOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions_members.md)  
[IMassPropertyOverrideOptions::SetOverridePrincipalMomentsOfInertia Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverridePrincipalMomentsOfInertia.md)  
[IMassPropertyOverrideOptions::OverrideMomentsOfInertia Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideMomentsOfInertia.md)  
[IMassProperty2::PrincipalMomentsOfInertia Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~PrincipalMomentsOfInertia.md)
