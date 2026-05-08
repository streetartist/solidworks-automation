# GetRoutingUserPreferenceToggle Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~GetRoutingUserPreferenceToggle`

Gets whether the specified routing user preference is turned on.
Gets whether the specified routing user preference is turned on.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRoutingUserPreferenceToggle( _
   ByVal UserPreferenceToggle As System.Integer _
) As System.Boolean
```

```

Dim instance As IRoutingSettings
Dim UserPreferenceToggle As System.Integer
Dim value As System.Boolean
 
value = instance.GetRoutingUserPreferenceToggle(UserPreferenceToggle)
```

```

System.bool GetRoutingUserPreferenceToggle( 
   System.int UserPreferenceToggle
)
```

```

System.bool GetRoutingUserPreferenceToggle( 
   System.int UserPreferenceToggle
) 
```

#### Parameters

*UserPreferenceToggle*
:   User preference as defined in [swUserPreferenceRoutingToggle\_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swUserPreferenceRoutingToggle_e.md)

#### Return Value

True if on, false if off

Example

See the [IRoutingSettings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRoutingSettings Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.md)  
[IRoutingSettings Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings_members.md)  
[IRoutingSettings::SetRoutingUserPreferenceToggle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~SetRoutingUserPreferenceToggle.md)
