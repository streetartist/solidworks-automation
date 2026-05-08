# SetRoutingUserPreferenceStringValue Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~SetRoutingUserPreferenceStringValue`

Sets a string value for the specified routing user preference.
Sets a string value for the specified routing user preference.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetRoutingUserPreferenceStringValue( _
   ByVal UserPreference As System.Integer, _
   ByVal Value As System.String _
) As System.Boolean
```

```

Dim instance As IRoutingSettings
Dim UserPreference As System.Integer
Dim Value As System.String
Dim value As System.Boolean
 
value = instance.SetRoutingUserPreferenceStringValue(UserPreference, Value)
```

```

System.bool SetRoutingUserPreferenceStringValue( 
   System.int UserPreference,
   System.string Value
)
```

```

System.bool SetRoutingUserPreferenceStringValue( 
   System.int UserPreference,
   System.String^ Value
) 
```

#### Parameters

*UserPreference*
:   User preference as defined in [swUserPreferenceRoutingFileLocations\_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swUserPreferenceRoutingFileLocations_e.md)

*Value*
:   String value of the specified user preference

#### Return Value

True if successful, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRoutingSettings Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.md)  
[IRoutingSettings Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings_members.md)  
[IRoutingSettings::GetRoutingUserPreferenceStringValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~GetRoutingUserPreferenceStringValue.md)
