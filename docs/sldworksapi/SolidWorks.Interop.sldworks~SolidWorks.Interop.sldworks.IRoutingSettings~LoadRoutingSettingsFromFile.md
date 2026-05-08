# LoadRoutingSettingsFromFile Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~LoadRoutingSettingsFromFile`

Loads routing settings from the specified file.
Loads routing settings from the specified file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function LoadRoutingSettingsFromFile( _
   ByVal RoutingSettingsFilename As System.String _
) As System.Boolean
```

```

Dim instance As IRoutingSettings
Dim RoutingSettingsFilename As System.String
Dim value As System.Boolean
 
value = instance.LoadRoutingSettingsFromFile(RoutingSettingsFilename)
```

```

System.bool LoadRoutingSettingsFromFile( 
   System.string RoutingSettingsFilename
)
```

```

System.bool LoadRoutingSettingsFromFile( 
   System.String^ RoutingSettingsFilename
) 
```

#### Parameters

*RoutingSettingsFilename*
:   :   Full path name of the **.sqy** file from which to load the routing settings

#### Return Value

True if successful, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRoutingSettings Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.md)  
[IRoutingSettings Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings_members.md)  
[IRoutingSettings::LoadDefaultRoutingSettings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~LoadDefaultRoutingSettings.md)  
[IRoutingSettings::SaveRoutingSettingsToFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~SaveRoutingSettingsToFile.md)
