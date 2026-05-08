# GetOverrideMomentsOfInertiaValue Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~GetOverrideMomentsOfInertiaValue`

Gets the override moments of inertia.
Gets the override moments of inertia.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetOverrideMomentsOfInertiaValue( _
   ByRef IsReferenceFrameSet As System.Boolean, _
   ByRef CoordinateSystemName As System.String _
) As System.Object
```

```

Dim instance As IMassPropertyOverrideOptions
Dim IsReferenceFrameSet As System.Boolean
Dim CoordinateSystemName As System.String
Dim value As System.Object
 
value = instance.GetOverrideMomentsOfInertiaValue(IsReferenceFrameSet, CoordinateSystemName)
```

```

System.object GetOverrideMomentsOfInertiaValue( 
   out System.bool IsReferenceFrameSet,
   out System.string CoordinateSystemName
)
```

```

System.Object^ GetOverrideMomentsOfInertiaValue( 
   [Out] System.bool IsReferenceFrameSet,
   [Out] System.String^ CoordinateSystemName
) 
```

#### Parameters

*IsReferenceFrameSet*
:   True if reference frame is set, false if not

*CoordinateSystemName*
:   Name of coordinate system

#### Return Value

Array of nine doubles: [ Lxx, Lxy, Lxz, Lyx, Lyy, Lyz, Lzx, Lzy, Lzz ]

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassPropertyOverrideOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions.md)  
[IMassPropertyOverrideOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions_members.md)  
[IMassPropertyOverrideOptions::SetOverrideMomentsOfInertiaValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverrideMomentsOfInertiaValue.md)  
[IMassPropertyOverrideOptions::OverrideMomentsOfInertia Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideMomentsOfInertia.md)  
[IMassProperty2::GetMomentOfInertia Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~GetMomentOfInertia.md)
