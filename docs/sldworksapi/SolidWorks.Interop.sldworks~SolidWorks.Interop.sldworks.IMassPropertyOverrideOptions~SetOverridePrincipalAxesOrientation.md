# SetOverridePrincipalAxesOrientation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverridePrincipalAxesOrientation`

Overrides the orientation of the specified principal axis of inertia of the model currently being edited.
Overrides the orientation of the specified principal axis of inertia of the model currently being edited.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetOverridePrincipalAxesOrientation( _
   ByVal Axis As System.Integer, _
   ByVal Value As System.Object, _
   ByVal AutoCorrect As System.Boolean _
) As System.Boolean
```

```

Dim instance As IMassPropertyOverrideOptions
Dim Axis As System.Integer
Dim Value As System.Object
Dim AutoCorrect As System.Boolean
Dim value As System.Boolean
 
value = instance.SetOverridePrincipalAxesOrientation(Axis, Value, AutoCorrect)
```

```

System.bool SetOverridePrincipalAxesOrientation( 
   System.int Axis,
   System.object Value,
   System.bool AutoCorrect
)
```

```

System.bool SetOverridePrincipalAxesOrientation( 
   System.int Axis,
   System.Object^ Value,
   System.bool AutoCorrect
) 
```

#### Parameters

*Axis*
:   One of the following principal axes:

    - 0 = X axis
    - 1 = Y axis
    - 2 = Z axis

*Value*
:   An array of three doubles of the x, y, and z coordinates of Axis

*AutoCorrect*
:   True to generate orthogonal axes, false to not

#### Return Value

True if the principal axis orientation successfully overridden, false if not

Remarks

This method is valid only if [IMassPropertyOverrideOptions::OverrideMomentsOfInertia](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideMomentsOfInertia.md) is set to true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassPropertyOverrideOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions.md)  
[IMassPropertyOverrideOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions_members.md)  
[IMassProperty2::PrincipalAxesOfInertia Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~PrincipalAxesOfInertia.md)
