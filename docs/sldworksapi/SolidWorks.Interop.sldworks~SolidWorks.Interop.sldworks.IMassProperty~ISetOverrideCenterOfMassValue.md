# ISetOverrideCenterOfMassValue Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetOverrideCenterOfMassValue`

Overrides the center of mass of the model currently being edited in this part or assembly document.
Overrides the center of mass of the model currently being edited in this part or assembly document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetOverrideCenterOfMassValue( _
   ByRef Value As System.Double, _
   ByVal CoordinateSystemName As System.String, _
   ByVal Config_option As System.Integer, _
   ByVal Config_numbers As System.Integer, _
   ByRef Config_names As System.String _
) As System.Boolean
```

```

Dim instance As IMassProperty
Dim Value As System.Double
Dim CoordinateSystemName As System.String
Dim Config_option As System.Integer
Dim Config_numbers As System.Integer
Dim Config_names As System.String
Dim value As System.Boolean
 
value = instance.ISetOverrideCenterOfMassValue(Value, CoordinateSystemName, Config_option, Config_numbers, Config_names)
```

```

System.bool ISetOverrideCenterOfMassValue( 
   ref System.double Value,
   System.string CoordinateSystemName,
   System.int Config_option,
   System.int Config_numbers,
   ref System.string Config_names
)
```

```

System.bool ISetOverrideCenterOfMassValue( 
   System.double% Value,
   System.String^ CoordinateSystemName,
   System.int Config_option,
   System.int Config_numbers,
   System.String^% Config_names
) 
```

#### Parameters

*Value*
:   - in-process, unmanaged C++: Pointer to an array of three doubles of the x, y, and z coordinates of the center of mass
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*CoordinateSystemName*
:   Name of the coordinate system in which the center of mass is defined

*Config\_option*
:   Configuration option as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

*Config\_numbers*
:   Number of configurations

*Config\_names*
:   - in-process, unmanaged C++: Pointer to an array of configuration names of size Config\_numbers; valid only if Config\_option = swInConfigurationOpts\_e.swSpecifyConfiguration
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

True if the center of mass is overridden, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.md)  
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.md)  
[IMassProperty::SetOverrideCenterOfMassValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetOverrideCenterOfMassValue.md)  
[IMassProperty::OverrideCenterOfMass Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~OverrideCenterOfMass.md)
