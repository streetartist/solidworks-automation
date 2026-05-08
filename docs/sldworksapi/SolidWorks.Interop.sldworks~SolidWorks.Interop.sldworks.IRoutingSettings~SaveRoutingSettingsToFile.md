# SaveRoutingSettingsToFile Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~SaveRoutingSettingsToFile`

Saves routing settings to the specified file.
Saves routing settings to the specified file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveRoutingSettingsToFile( _
   ByVal RoutingSettingsFilename As System.String _
) As System.Boolean
```

```

Dim instance As IRoutingSettings
Dim RoutingSettingsFilename As System.String
Dim value As System.Boolean
 
value = instance.SaveRoutingSettingsToFile(RoutingSettingsFilename)
```

```

System.bool SaveRoutingSettingsToFile( 
   System.string RoutingSettingsFilename
)
```

```

System.bool SaveRoutingSettingsToFile( 
   System.String^ RoutingSettingsFilename
) 
```

#### Parameters

*RoutingSettingsFilename*
:   Full path name of file to which to save routing settings; file name must have an extension of **.sqy**

#### Return Value

True if successful, false if not

Example

See the [IRoutingSettings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRoutingSettings Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.md)  
[IRoutingSettings Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings_members.md)  
[IRoutingSettings::LoadRoutingSettingsFromFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~LoadRoutingSettingsFromFile.md)
