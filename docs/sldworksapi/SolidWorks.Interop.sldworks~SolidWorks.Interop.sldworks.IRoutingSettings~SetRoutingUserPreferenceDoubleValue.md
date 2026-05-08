# SetRoutingUserPreferenceDoubleValue Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~SetRoutingUserPreferenceDoubleValue`

Sets a double value for the specified routing user preference.
Sets a double value for the specified routing user preference.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetRoutingUserPreferenceDoubleValue( _
   ByVal UserPreferenceValue As System.Integer, _
   ByVal Value As System.Double _
) As System.Boolean
```

```

Dim instance As IRoutingSettings
Dim UserPreferenceValue As System.Integer
Dim Value As System.Double
Dim value As System.Boolean
 
value = instance.SetRoutingUserPreferenceDoubleValue(UserPreferenceValue, Value)
```

```

System.bool SetRoutingUserPreferenceDoubleValue( 
   System.int UserPreferenceValue,
   System.double Value
)
```

```

System.bool SetRoutingUserPreferenceDoubleValue( 
   System.int UserPreferenceValue,
   System.double Value
) 
```

#### Parameters

*UserPreferenceValue*
:   User preference as defined in [swUserPreferenceRoutingDouble\_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swUserPreferenceRoutingDouble_e.md)

*Value*
:   Double value of the specified user preference

#### Return Value

True if successful, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRoutingSettings Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.md)  
[IRoutingSettings Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings_members.md)  
[IRoutingSettings::GetRoutingUserPreferenceDoubleValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~GetRoutingUserPreferenceDoubleValue.md)
