# SetOverrideMassValue Method (IMassProperty)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetOverrideMassValue`

Overrides the mass of the model currently being edited in this part or assembly document.
Overrides the mass of the model currently being edited in this part or assembly document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetOverrideMassValue( _
   ByVal Value As System.Double, _
   ByVal Config_option As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Boolean
```

```

Dim instance As IMassProperty
Dim Value As System.Double
Dim Config_option As System.Integer
Dim Config_names As System.Object
Dim value As System.Boolean
 
value = instance.SetOverrideMassValue(Value, Config_option, Config_names)
```

```

System.bool SetOverrideMassValue( 
   System.double Value,
   System.int Config_option,
   System.object Config_names
)
```

```

System.bool SetOverrideMassValue( 
   System.double Value,
   System.int Config_option,
   System.Object^ Config_names
) 
```

#### Parameters

*Value*
:   Override mass value (see **Remarks**)

*Config\_option*
:   Configuration option as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

*Config\_names*
:   Array of configuration names (see **Remarks**)

#### Return Value

True if the mass value is overridden, false if not

Remarks

|  |  |
| --- | --- |
| If... | Then... |
| You are editing a subcomponent | you are overriding the mass for this subcomponent and not for the top-level model. |
| Value > 0  Value < 0 | mass is overridden.  mass is calculated. |
| Config\_option = [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html).swSpecifyConfiguration | Config\_names is used. |

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
[IMassProperty::ISetOverrideMassValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetOverrideMassValue.md)  
[IMassProperty::OverrideMass Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~OverrideMass.md)
