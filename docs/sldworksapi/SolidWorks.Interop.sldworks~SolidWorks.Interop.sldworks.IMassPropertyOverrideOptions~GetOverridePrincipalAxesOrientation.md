# GetOverridePrincipalAxesOrientation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~GetOverridePrincipalAxesOrientation`

Gets the override principal axis of inertia.
Gets the override principal axis of inertia.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetOverridePrincipalAxesOrientation( _
   ByVal Axis As System.Integer _
) As System.Object
```

```

Dim instance As IMassPropertyOverrideOptions
Dim Axis As System.Integer
Dim value As System.Object
 
value = instance.GetOverridePrincipalAxesOrientation(Axis)
```

```

System.object GetOverridePrincipalAxesOrientation( 
   System.int Axis
)
```

```

System.Object^ GetOverridePrincipalAxesOrientation( 
   System.int Axis
) 
```

#### Parameters

*Axis*
:   One of the following principal axes:

    - 0 = X axis
    - 1 = Y axis
    - 2 = Z axis

#### Return Value

An array of three doubles of the x, y, and z coordinates of Axis

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassPropertyOverrideOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions.md)  
[IMassPropertyOverrideOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions_members.md)  
[IMassPropertyOverrideOptions::SetOverridePrincipalAxesOrientation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverridePrincipalAxesOrientation.md)  
[IMassPropertyOverrideOptions::OverrideMomentsOfInertia Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideMomentsOfInertia.md)  
[IMassProperty2::PrincipalAxesOfInertia Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~PrincipalAxesOfInertia.md)
