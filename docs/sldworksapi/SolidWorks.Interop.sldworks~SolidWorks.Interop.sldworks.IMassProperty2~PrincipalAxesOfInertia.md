# PrincipalAxesOfInertia Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~PrincipalAxesOfInertia`

Gets the principal axis of inertia for the specified axis.
Gets the principal axis of inertia for the specified axis.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property PrincipalAxesOfInertia( _
   ByVal Axis As System.Integer _
) As System.Object
```

```

Dim instance As IMassProperty2
Dim Axis As System.Integer
Dim value As System.Object
 
value = instance.PrincipalAxesOfInertia(Axis)
```

```

System.object PrincipalAxesOfInertia( 
   System.int Axis
) {get;}
```

```

property System.Object^ PrincipalAxesOfInertia {
   System.Object^ get(System.int Axis);
}
```

#### Parameters

*Axis*
:   - 0 = x axis
    - 1 = y axis
    - 2 = z axis

#### Property Value

Zero-based array of size 3 (see **Remarks**)

Remarks

This method returns:

- A vector that represents the specified Axis: lx, ly, or lz.
- Metric units unless explicitly specified otherwise.

If [IMassPropertyOverrideOptions::OverrideMomentsOfInertia](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideMomentsOfInertia.md) is true or [IMassProperty2::IncludeHiddenBodiesOrComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~IncludeHiddenBodiesOrComponents.md) is reset, then call [IMassProperty2::Recalculate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~Recalculate.md) before using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.md)  
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.md)  
[IMassPropertyOverrideOptions::SetOverridePrincipalAxesOrientation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverridePrincipalAxesOrientation.md)  
[IMassProperty2::PrincipalMomentsOfInertia Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~PrincipalMomentsOfInertia.md)  
[IMassProperty2::GetMomentOfInertia Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~GetMomentOfInertia.md)  
[IMassPropertyOverrideOptions::GetOverridePrincipalAxesOrientation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~GetOverridePrincipalAxesOrientation.md)
