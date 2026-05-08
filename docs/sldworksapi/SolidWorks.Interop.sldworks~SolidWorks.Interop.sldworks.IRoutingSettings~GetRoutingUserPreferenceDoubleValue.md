# GetRoutingUserPreferenceDoubleValue Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~GetRoutingUserPreferenceDoubleValue`

Gets the double value of the specified routing user preference.
Gets the double value of the specified routing user preference.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRoutingUserPreferenceDoubleValue( _
   ByVal UserPreferenceValue As System.Integer _
) As System.Double
```

```

Dim instance As IRoutingSettings
Dim UserPreferenceValue As System.Integer
Dim value As System.Double
 
value = instance.GetRoutingUserPreferenceDoubleValue(UserPreferenceValue)
```

```

System.double GetRoutingUserPreferenceDoubleValue( 
   System.int UserPreferenceValue
)
```

```

System.double GetRoutingUserPreferenceDoubleValue( 
   System.int UserPreferenceValue
) 
```

#### Parameters

*UserPreferenceValue*
:   User preference as defined in [swUserPreferenceRoutingDouble\_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swUserPreferenceRoutingDouble_e.md)

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
[IRoutingSettings::SetRoutingUserPreferenceDoubleValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~SetRoutingUserPreferenceDoubleValue.md)
