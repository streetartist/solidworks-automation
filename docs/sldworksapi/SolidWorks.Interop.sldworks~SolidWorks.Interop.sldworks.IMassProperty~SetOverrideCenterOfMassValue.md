# SetOverrideCenterOfMassValue Method (IMassProperty)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetOverrideCenterOfMassValue`

Overrides the center of mass of the model currently being edited in this part or assembly document.
Overrides the center of mass of the model currently being edited in this part or assembly document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetOverrideCenterOfMassValue( _
   ByVal Value As System.Object, _
   ByVal CoordinateSystemName As System.String, _
   ByVal Config_option As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Boolean
```

```

Dim instance As IMassProperty
Dim Value As System.Object
Dim CoordinateSystemName As System.String
Dim Config_option As System.Integer
Dim Config_names As System.Object
Dim value As System.Boolean
 
value = instance.SetOverrideCenterOfMassValue(Value, CoordinateSystemName, Config_option, Config_names)
```

```

System.bool SetOverrideCenterOfMassValue( 
   System.object Value,
   System.string CoordinateSystemName,
   System.int Config_option,
   System.object Config_names
)
```

```

System.bool SetOverrideCenterOfMassValue( 
   System.Object^ Value,
   System.String^ CoordinateSystemName,
   System.int Config_option,
   System.Object^ Config_names
) 
```

#### Parameters

*Value*
:   Array of three doubles of the x, y, and z coordinates of the center of mass

*CoordinateSystemName*
:   Name of the coordinate system in which the center of mass is defined

*Config\_option*
:   Configuration option as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

*Config\_names*
:   Array of configuration names; valid only if Config\_option = swInConfigurationOpts\_e.swSpecifyConfiguration

#### Return Value

True if the center of mass is overridden, false if not

Example

[Get and Override Mass Properties (VBA)](Get_Mass_Properties_using_MassProperty_Object_Example_VB.htm)  
[Get and Override Mass Properties (VB.NET)](Get_Mass_Properties_Using_IMassProperty_Example_VBNET.htm)  
[Get and Override Mass Properties (C#)](Get_Mass_Properties_Using_IMassProperty_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.md)  
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.md)  
[IMassProperty::ISetOverrideCenterOfMassValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetOverrideCenterOfMassValue.md)  
[IMassProperty::OverrideCenterOfMass Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~OverrideCenterOfMass.md)
