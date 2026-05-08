# ISetSystemValue3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetSystemValue3`

Sets the value of this dimension in system units (meters) in the specified configuration.
Sets the value of this dimension in system units (meters) in the specified configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetSystemValue3( _
   ByVal NewValue As System.Double, _
   ByVal WhichConfigurations As System.Integer, _
   ByVal Config_count As System.Integer, _
   ByRef Config_names As System.String _
) As System.Integer
```

```

Dim instance As IDimension
Dim NewValue As System.Double
Dim WhichConfigurations As System.Integer
Dim Config_count As System.Integer
Dim Config_names As System.String
Dim value As System.Integer
 
value = instance.ISetSystemValue3(NewValue, WhichConfigurations, Config_count, Config_names)
```

```

System.int ISetSystemValue3( 
   System.double NewValue,
   System.int WhichConfigurations,
   System.int Config_count,
   ref System.string Config_names
)
```

```

System.int ISetSystemValue3( 
   System.double NewValue,
   System.int WhichConfigurations,
   System.int Config_count,
   System.String^% Config_names
) 
```

#### Parameters

*NewValue*
:   Dimension value in meters

*WhichConfigurations*
:   Configuration in which to set this value as defined in [swSetValueInConfiguration\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSetValueInConfiguration_e.html) (see Remarks)

*Config\_count*
:   Names of the configurations (see Remarks)

*Config\_names*
:   Names of the configurations (see **Remarks**)

#### Return Value

Success indicator value as defined in [swSetValueReturnStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSetValueReturnStatus_e.html)

Remarks

The WhichConfigurations argument is equivalent to the Change Parameter dialog in the SOLIDWORKS user interface, which gives the user the option of having the value set in all configurations or the current configuration. If there is one configuration in the part, SOLIDWORKS ignores this argument.

The Config\_count and Config\_names arguments are only used if WhichConfigurations is set to swSetValue\_InSpecificConfigurations.

Config\_names can contain either a BSTR array or a single BSTR.

This method allows you to change the value of a read-only dimension. You can use [IDimension::ReadOnly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ReadOnly.md) to determine if a dimension is read-only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)  
[IDimension::SetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetSystemValue3.md)  
[IDimension::GetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetSystemValue3.md)  
[IDimension::GetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetValue3.md)  
[IDimension::ISetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetValue3.md)  
[IDimension::SetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetValue3.md)  
[IDimension::GetUserValueIn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetUserValueIn.md)  
[IDimension::IGetUserValueIn2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetUserValueIn2.md)  
[IDimension::ISetUserValueIn2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetUserValueIn2.md)  
[IDimension::SetUserValueIn2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetUserValueIn2.md)  
[IDimension::GetUserValueIn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetUserValueIn.md)
