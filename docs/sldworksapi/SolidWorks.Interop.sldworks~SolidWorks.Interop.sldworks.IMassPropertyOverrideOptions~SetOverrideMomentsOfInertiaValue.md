# SetOverrideMomentsOfInertiaValue Method (IMassPropertyOverrideOptions)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverrideMomentsOfInertiaValue`

Overrides the calculated moments of inertia of the model currently being edited.
Overrides the calculated moments of inertia of the model currently being edited.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetOverrideMomentsOfInertiaValue( _
   ByVal ReferenceFrame As System.Integer, _
   ByVal Value As System.Object, _
   ByVal CoordinateSystemName As System.String _
) As System.Boolean
```

```

Dim instance As IMassPropertyOverrideOptions
Dim ReferenceFrame As System.Integer
Dim Value As System.Object
Dim CoordinateSystemName As System.String
Dim value As System.Boolean
 
value = instance.SetOverrideMomentsOfInertiaValue(ReferenceFrame, Value, CoordinateSystemName)
```

```

System.bool SetOverrideMomentsOfInertiaValue( 
   System.int ReferenceFrame,
   System.object Value,
   System.string CoordinateSystemName
)
```

```

System.bool SetOverrideMomentsOfInertiaValue( 
   System.int ReferenceFrame,
   System.Object^ Value,
   System.String^ CoordinateSystemName
) 
```

#### Parameters

*ReferenceFrame*
:   Frame of reference as defined in [swMomentsOfInertiaReferenceFrame\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMomentsOfInertiaReferenceFrame_e.html)

*Value*
:   Array of nine doubles: [ Lxx, Lxy, Lxz, Lyx, Lyy, Lyz, Lzx, Lzy, Lzz ]

*CoordinateSystemName*
:   Name of coordinate system; valid only if ReferenceFrame = swMomentsOfInertiaReferenceFrame\_e.swMomentsOfInertiaReferenceFrame\_UserCoordinateSystem

#### Return Value

True if the moments of inertia are successfully overridden, false if not

Remarks

This method is valid only if [IMassPropertyOverrideOptions::OverrideMomentsOfInertia](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideMomentsOfInertia.md) is set to true.

Example

See the [IMassProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassPropertyOverrideOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions.md)  
[IMassPropertyOverrideOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions_members.md)  
[IMassProperty2::GetMomentOfInertia Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~GetMomentOfInertia.md)
