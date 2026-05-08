# GetMomentOfInertia Method (IMassProperty2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~GetMomentOfInertia`

Gets the moment of inertia at the specified coordinate system for the selected bodies/components.
Gets the moment of inertia at the specified coordinate system for the selected bodies/components.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMomentOfInertia( _
   ByVal WhereTaken As System.Integer _
) As System.Object
```

```

Dim instance As IMassProperty2
Dim WhereTaken As System.Integer
Dim value As System.Object
 
value = instance.GetMomentOfInertia(WhereTaken)
```

```

System.object GetMomentOfInertia( 
   System.int WhereTaken
)
```

```

System.Object^ GetMomentOfInertia( 
   System.int WhereTaken
) 
```

#### Parameters

*WhereTaken*
:   Coordinate system as defined in [swMassPropertyMoment\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMassPropertyMoment_e.html)

#### Return Value

Array containing the moment of inertia calculations (see **Remarks**)

Remarks

The return value is a 0-based array of nine doubles:

[ Lxx, Lxy, Lxz, Lyx, Lyy, Lyz, Lzx, Lzy, Lzz ]

Example

See the [IMassProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.md)  
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.md)  
[IMassProperty2::PrincipalAxesOfInertia Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~PrincipalAxesOfInertia.md)  
[IMassProperty2::PrincipalMomentsOfInertia Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~PrincipalMomentsOfInertia.md)  
[IMassPropertyOverrideOptions::SetOverrideMomentsOfInertiaValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverrideMomentsOfInertiaValue.md)  
[IMassPropertyOverrideOptions::GetOverrideMomentsOfInertiaValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~GetOverrideMomentsOfInertiaValue.md)
