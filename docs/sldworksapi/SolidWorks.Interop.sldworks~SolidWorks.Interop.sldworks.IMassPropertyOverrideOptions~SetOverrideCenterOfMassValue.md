# SetOverrideCenterOfMassValue Method (IMassPropertyOverrideOptions)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverrideCenterOfMassValue`

Overrides the calculated center of mass of the model currently being edited.
Overrides the calculated center of mass of the model currently being edited.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetOverrideCenterOfMassValue( _
   ByVal Value As System.Object, _
   ByVal CoordinateSystemName As System.String _
) As System.Boolean
```

```

Dim instance As IMassPropertyOverrideOptions
Dim Value As System.Object
Dim CoordinateSystemName As System.String
Dim value As System.Boolean
 
value = instance.SetOverrideCenterOfMassValue(Value, CoordinateSystemName)
```

```

System.bool SetOverrideCenterOfMassValue( 
   System.object Value,
   System.string CoordinateSystemName
)
```

```

System.bool SetOverrideCenterOfMassValue( 
   System.Object^ Value,
   System.String^ CoordinateSystemName
) 
```

#### Parameters

*Value*
:   Array of three doubles of the x, y, and z coordinates of the center of mass

*CoordinateSystemName*
:   Name of the coordinate system in which the center of mass is defined

#### Return Value

True if the center of mass is successfully overridden, false if not

Remarks

This method is valid only if [IMassPropertyOverrideOptions::OverrideCenterOfMass](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideCenterOfMass.md) is set to true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassPropertyOverrideOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions.md)  
[IMassPropertyOverrideOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions_members.md)  
[IMassProperty2::CenterOfMass Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~CenterOfMass.md)
