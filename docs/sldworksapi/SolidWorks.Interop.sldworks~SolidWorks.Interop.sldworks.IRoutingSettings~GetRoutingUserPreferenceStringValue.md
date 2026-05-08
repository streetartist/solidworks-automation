# GetRoutingUserPreferenceStringValue Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~GetRoutingUserPreferenceStringValue`

Gets the string value of the specified routing user preference.
Gets the string value of the specified routing user preference.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRoutingUserPreferenceStringValue( _
   ByVal UserPreference As System.Integer, _
   ByVal UseDefaultVal As System.Boolean _
) As System.String
```

```

Dim instance As IRoutingSettings
Dim UserPreference As System.Integer
Dim UseDefaultVal As System.Boolean
Dim value As System.String
 
value = instance.GetRoutingUserPreferenceStringValue(UserPreference, UseDefaultVal)
```

```

System.string GetRoutingUserPreferenceStringValue( 
   System.int UserPreference,
   System.bool UseDefaultVal
)
```

```

System.String^ GetRoutingUserPreferenceStringValue( 
   System.int UserPreference,
   System.bool UseDefaultVal
) 
```

#### Parameters

*UserPreference*
:   User preference as defined in [swUserPreferenceRoutingFileLocations\_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swUserPreferenceRoutingFileLocations_e.md)

*UseDefaultVal*
:   True to use the default, false to not

#### Return Value

User preference

Example

See the [IRoutingSettings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRoutingSettings Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.md)  
[IRoutingSettings Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings_members.md)  
[IRoutingSettings::SetRoutingUserPreferenceStringValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~SetRoutingUserPreferenceStringValue.md)
