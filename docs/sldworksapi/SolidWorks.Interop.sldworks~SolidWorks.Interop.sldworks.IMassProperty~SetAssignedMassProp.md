# SetAssignedMassProp Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetAssignedMassProp`

Sets the mass and center of gravity for the specified configurations for this model being edited in this part or assembly document.
Sets the mass and center of gravity for the specified configurations for this model being edited in this part or assembly document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetAssignedMassProp( _
   ByVal Mass As System.Double, _
   ByVal Center_x As System.Double, _
   ByVal Center_y As System.Double, _
   ByVal Center_z As System.Double, _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Boolean
```

```

Dim instance As IMassProperty
Dim Mass As System.Double
Dim Center_x As System.Double
Dim Center_y As System.Double
Dim Center_z As System.Double
Dim Config_opt As System.Integer
Dim Config_names As System.Object
Dim value As System.Boolean
 
value = instance.SetAssignedMassProp(Mass, Center_x, Center_y, Center_z, Config_opt, Config_names)
```

```

System.bool SetAssignedMassProp( 
   System.double Mass,
   System.double Center_x,
   System.double Center_y,
   System.double Center_z,
   System.int Config_opt,
   System.object Config_names
)
```

```

System.bool SetAssignedMassProp( 
   System.double Mass,
   System.double Center_x,
   System.double Center_y,
   System.double Center_z,
   System.int Config_opt,
   System.Object^ Config_names
) 
```

#### Parameters

*Mass*
:   Value for mass

*Center\_x*
:   x coordinate for center of gravity

*Center\_y*
:   y coordinate for center of gravity

*Center\_z*
:   z coordinate for center of gravity

*Config\_opt*
:   Configuration options as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

*Config\_names*
:   Array of the configuration names

#### Return Value

True if the mass and center of gravity are set, false if not

Remarks

|  |  |
| --- | --- |
| If... | Then... |
| You are editing a subcomponent | you are setting the mass for this subcomponent and not for the top-level model. |
| You specify a value < 0 for Mass | mass is calculated; it is not user-defined. |
| Config\_opt is set to swSpecifyConfiguration | Config\_names is used. |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.md)  
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.md)  
[IMassProperty::ISetAssignedMassProp Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetAssignedMassProp.md)  
[IMassProperty::Mass Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~Mass.md)  
[IMassProperty::UserAssigned Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~UserAssigned.md)  
[IMassProperty::IGetCenterOfMass Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetCenterOfMass.md)  
[IMassProperty::CenterOfMass Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~CenterOfMass.md)
