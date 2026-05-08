# SetOverridePrincipalMomentsOfInertia Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverridePrincipalMomentsOfInertia`

Overrides the calculated principal moments of inertia of the model currently being edited.
Overrides the calculated principal moments of inertia of the model currently being edited.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetOverridePrincipalMomentsOfInertia( _
   ByVal Value As System.Object _
) As System.Boolean
```

```

Dim instance As IMassPropertyOverrideOptions
Dim Value As System.Object
Dim value As System.Boolean
 
value = instance.SetOverridePrincipalMomentsOfInertia(Value)
```

```

System.bool SetOverridePrincipalMomentsOfInertia( 
   System.object Value
)
```

```

System.bool SetOverridePrincipalMomentsOfInertia( 
   System.Object^ Value
) 
```

#### Parameters

*Value*
:   Array of three doubles of the principal moments of inertia: **[** Px, Py, Pz **]**

#### Return Value

True if the prinicpal moments of inertia are successfully overridden, false if not

Remarks

This method is valid only if [IMassPropertyOverrideOptions::OverrideMomentsOfInertia](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideMomentsOfInertia.md) is set to true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassPropertyOverrideOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions.md)  
[IMassPropertyOverrideOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions_members.md)  
[IMassProperty2::PrincipalMomentsOfInertia Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~PrincipalMomentsOfInertia.md)
