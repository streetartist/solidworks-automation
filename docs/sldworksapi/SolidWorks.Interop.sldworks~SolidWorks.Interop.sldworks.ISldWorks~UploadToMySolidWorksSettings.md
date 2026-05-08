# UploadToMySolidWorksSettings Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UploadToMySolidWorksSettings`

Uploads the specified SOLIDWORKS Desktop settings to SOLIDWORKS Connected.
Uploads the specified SOLIDWORKS Desktop settings to [SOLIDWORKS Connected](sldworksapiprogguide.chm::/Overview/SOLIDWORKS_Connected.htm).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function UploadToMySolidWorksSettings( _
   ByVal SystemOptions As System.Boolean, _
   ByVal FileLocations As System.Boolean, _
   ByVal Customizations As System.Boolean _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim SystemOptions As System.Boolean
Dim FileLocations As System.Boolean
Dim Customizations As System.Boolean
Dim value As System.Integer
 
value = instance.UploadToMySolidWorksSettings(SystemOptions, FileLocations, Customizations)
```

```

System.int UploadToMySolidWorksSettings( 
   System.bool SystemOptions,
   System.bool FileLocations,
   System.bool Customizations
)
```

```

System.int UploadToMySolidWorksSettings( 
   System.bool SystemOptions,
   System.bool FileLocations,
   System.bool Customizations
) 
```

#### Parameters

*SystemOptions*
:   True to upload, false to not

*FileLocations*
:   True to upload, false to not

*Customizations*
:   True to upload, false to not

#### Return Value

Return code as defined by [swConnectedSyncSettingsErrors\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConnectedSyncSettingsErrors_e.html)

Remarks

In order to use this method, you must be logged into SOLIDWORKS Connected.

To turn on auto synchronization of settings, call:

- [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.md)([swUserPreferenceToggle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.html).swAutomaticSyncSettings, True)

and then call one, two, or all three of:

- ISldWorks::SetUserPreferenceToggle(swUserPreferenceToggle\_e.swAutoSyncSettingsToInclude\_SystemOptions, True)
- ISldWorks::SetUserPreferenceToggle(swUserPreferenceToggle\_e.swAutoSyncSettingsToInclude\_FileLocations, True)
- ISldWorks::SetUserPreferenceToggle(swUserPreferenceToggle\_e.swAutoSyncSettingsToInclude\_Customizations, True)

To get the timestamp of the last synchronization, call [ISldWorks::GetUserPreferenceStringValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceStringValue.md)([swUserPreferenceStringValue\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceStringValue_e.html).swLastSynchronizationTimeStamp).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::DownloadFromMySolidWorksSettings Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DownloadFromMySolidWorksSettings.md)
