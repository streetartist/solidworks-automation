# SetRoutingUserPreferenceIntegerValue Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~SetRoutingUserPreferenceIntegerValue`

Sets an integer value for the specified routing user preference.
Sets an integer value for the specified routing user preference.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetRoutingUserPreferenceIntegerValue( _
   ByVal UserPreferenceValue As System.Integer, _
   ByVal Value As System.Integer _
) As System.Boolean
```

```

Dim instance As IRoutingSettings
Dim UserPreferenceValue As System.Integer
Dim Value As System.Integer
Dim value As System.Boolean
 
value = instance.SetRoutingUserPreferenceIntegerValue(UserPreferenceValue, Value)
```

```

System.bool SetRoutingUserPreferenceIntegerValue( 
   System.int UserPreferenceValue,
   System.int Value
)
```

```

System.bool SetRoutingUserPreferenceIntegerValue( 
   System.int UserPreferenceValue,
   System.int Value
) 
```

#### Parameters

*UserPreferenceValue*
:   User preference as defined in [swUserPreferenceRoutingInteger\_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swUserPreferenceRoutingInteger_e.md)

*Value*
:   Integer value of the specified user preference

#### Return Value

True if successful, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRoutingSettings Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.md)  
[IRoutingSettings Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings_members.md)  
[IRoutingSettings::GetRoutingUserPreferenceIntegerValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~GetRoutingUserPreferenceIntegerValue.md)
