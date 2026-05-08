# GetRoutingUserPreferenceIntegerValue Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~GetRoutingUserPreferenceIntegerValue`

Gets the integer value of the specified routing user preference.
Gets the integer value of the specified routing user preference.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRoutingUserPreferenceIntegerValue( _
   ByVal UserPreferenceValue As System.Integer _
) As System.Integer
```

```

Dim instance As IRoutingSettings
Dim UserPreferenceValue As System.Integer
Dim value As System.Integer
 
value = instance.GetRoutingUserPreferenceIntegerValue(UserPreferenceValue)
```

```

System.int GetRoutingUserPreferenceIntegerValue( 
   System.int UserPreferenceValue
)
```

```

System.int GetRoutingUserPreferenceIntegerValue( 
   System.int UserPreferenceValue
) 
```

#### Parameters

*UserPreferenceValue*
:   User preference as defined in [swUserPreferenceRoutingInteger\_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swUserPreferenceRoutingInteger_e.md)

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
[IRoutingSettings::GetRoutingUserPreferenceIntegerValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~GetRoutingUserPreferenceIntegerValue.md)
