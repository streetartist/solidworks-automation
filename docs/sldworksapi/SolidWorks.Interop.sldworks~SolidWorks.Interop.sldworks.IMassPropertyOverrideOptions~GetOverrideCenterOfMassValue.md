# GetOverrideCenterOfMassValue Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~GetOverrideCenterOfMassValue`

Gets the override center of mass.
Gets the override center of mass.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetOverrideCenterOfMassValue( _
   ByRef CoordinateSystemName As System.String _
) As System.Object
```

```

Dim instance As IMassPropertyOverrideOptions
Dim CoordinateSystemName As System.String
Dim value As System.Object
 
value = instance.GetOverrideCenterOfMassValue(CoordinateSystemName)
```

```

System.object GetOverrideCenterOfMassValue( 
   out System.string CoordinateSystemName
)
```

```

System.Object^ GetOverrideCenterOfMassValue( 
   [Out] System.String^ CoordinateSystemName
) 
```

#### Parameters

*CoordinateSystemName*
:   Name of the coordinate system in which the center of mass is defined

#### Return Value

Array of three doubles of the x, y, and z coordinates of the center of mass

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassPropertyOverrideOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions.md)  
[IMassPropertyOverrideOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions_members.md)  
[IMassPropertyOverrideOptions::SetOverrideCenterOfMassValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverrideCenterOfMassValue.md)  
[IMassProperty2::CenterOfMass Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~CenterOfMass.md)  
[IMassPropertyOverrideOptions::OverrideCenterOfMass Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideCenterOfMass.md)
