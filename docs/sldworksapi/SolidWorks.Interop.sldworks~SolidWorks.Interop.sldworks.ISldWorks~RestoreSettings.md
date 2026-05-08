# RestoreSettings Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RestoreSettings`

Restores the specified SOLIDWORKS settings from the specified *.sldreg file.
Restores the specified SOLIDWORKS settings from the specified **\*.sldreg** file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RestoreSettings( _
   ByVal FileName As System.String, _
   ByVal SystemOptions As System.Boolean, _
   ByVal ToolbarLayout As System.Boolean, _
   ByVal KeyboardShortcuts As System.Boolean, _
   ByVal MouseGestures As System.Boolean, _
   ByVal MenuCustomization As System.Boolean, _
   ByVal SavedViews As System.Boolean, _
   ByVal CreateBackup As System.Boolean _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim FileName As System.String
Dim SystemOptions As System.Boolean
Dim ToolbarLayout As System.Boolean
Dim KeyboardShortcuts As System.Boolean
Dim MouseGestures As System.Boolean
Dim MenuCustomization As System.Boolean
Dim SavedViews As System.Boolean
Dim CreateBackup As System.Boolean
Dim value As System.Integer
 
value = instance.RestoreSettings(FileName, SystemOptions, ToolbarLayout, KeyboardShortcuts, MouseGestures, MenuCustomization, SavedViews, CreateBackup)
```

```

System.int RestoreSettings( 
   System.string FileName,
   System.bool SystemOptions,
   System.bool ToolbarLayout,
   System.bool KeyboardShortcuts,
   System.bool MouseGestures,
   System.bool MenuCustomization,
   System.bool SavedViews,
   System.bool CreateBackup
)
```

```

System.int RestoreSettings( 
   System.String^ FileName,
   System.bool SystemOptions,
   System.bool ToolbarLayout,
   System.bool KeyboardShortcuts,
   System.bool MouseGestures,
   System.bool MenuCustomization,
   System.bool SavedViews,
   System.bool CreateBackup
) 
```

#### Parameters

*FileName*
:   Full path and filename of the settings to restore (**\*.sldreg**) (see **Remarks**)

*SystemOptions*
:   True to restore system options, false to not

*ToolbarLayout*
:   True to restore the toolbar layout, false to not

*KeyboardShortcuts*
:   True to restore keyboard shortcuts, false to not (see **Remarks**)

*MouseGestures*
:   True to restore mouse gestures, false to not

*MenuCustomization*
:   True to restore menu customizations, false to not

*SavedViews*
:   True to restore saved views, false to not (see **Remarks**)

*CreateBackup*
:   True to create a backup of the current settings, false to not (see **Remarks**)

#### Return Value

Error code as defined in [swSaveRestoreSettingsResults\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSaveRestoreSettingsResults_e.html)

Remarks

This method is valid only if [ISldWorks::SaveSettings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SaveSettings.md) was called previously.

KeyboardShortcuts and SavedViews are valid only if these settings were previously saved using ISldWorks::SaveSettings.

If CreateBackup is true, this method backs up the current settings to **backup\_***userid*\_*yyyymmdd***\_***hhmms*s**.sldreg** in the same location as specified in FileName.

For C++ only, specify all System.bool parameters using VARIANT\_TRUE (-1) and VARIANT\_FALSE (0).

Example

' VBA precondition:

' c:\temp exists

```

Dim swApp As SldWorks.SldWorks  
Option Explicit  
Sub main()
```

```

    Set swApp = Application.SldWorks  
      
    Dim boolStatus As Long  
    Dim path As String  
      
    path = "C:\temp\swSettings2.sldreg"  
    boolStatus = swApp.SaveSettings(path, True, swToolbarLayoutOption_e.swToolbarLayoutOption_AllToolbars, True, True, True, True)  
      
    path = "C:\temp\swSettings2.sldreg"  
    boolStatus = swApp.RestoreSettings(path, True, True, True, True, True, True, True)
```

```

End Sub
```

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::LoadAdminSettingsFile Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadAdminSettingsFile.md)
