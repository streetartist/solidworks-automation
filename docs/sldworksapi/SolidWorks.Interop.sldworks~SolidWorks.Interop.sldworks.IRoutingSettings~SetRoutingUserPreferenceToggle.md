# SetRoutingUserPreferenceToggle Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~SetRoutingUserPreferenceToggle`

Sets whether the specified routing user preference is turned on or off.
Sets whether the specified routing user preference is turned on or off.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetRoutingUserPreferenceToggle( _
   ByVal UserPreferenceValue As System.Integer, _
   ByVal OnFlag As System.Boolean _
) 
```

```

Dim instance As IRoutingSettings
Dim UserPreferenceValue As System.Integer
Dim OnFlag As System.Boolean
 
instance.SetRoutingUserPreferenceToggle(UserPreferenceValue, OnFlag)
```

```

void SetRoutingUserPreferenceToggle( 
   System.int UserPreferenceValue,
   System.bool OnFlag
)
```

```

void SetRoutingUserPreferenceToggle( 
   System.int UserPreferenceValue,
   System.bool OnFlag
) 
```

#### Parameters

*UserPreferenceValue*
:   User preference as defined in [swUserPreferenceRoutingToggle\_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swUserPreferenceRoutingToggle_e.md)

*OnFlag*
:   True to turn on, false to turn off

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRoutingSettings Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.md)  
[IRoutingSettings Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings_members.md)  
[IRoutingSettings::GetRoutingUserPreferenceToggle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~GetRoutingUserPreferenceToggle.md)
