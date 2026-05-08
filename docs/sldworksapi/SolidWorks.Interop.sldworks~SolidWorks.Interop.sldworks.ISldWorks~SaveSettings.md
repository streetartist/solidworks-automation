# SaveSettings Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SaveSettings`

Saves the specified SOLIDWORKS settings to the specified *.sldreg file.
Saves the specified SOLIDWORKS settings to the specified **\*.sldreg** file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveSettings( _
   ByVal FileName As System.String, _
   ByVal SystemOptions As System.Boolean, _
   ByVal ToolbarLayout As System.Integer, _
   ByVal KeyboardShortcuts As System.Boolean, _
   ByVal MouseGestures As System.Boolean, _
   ByVal MenuCustomization As System.Boolean, _
   ByVal SavedViews As System.Boolean _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim FileName As System.String
Dim SystemOptions As System.Boolean
Dim ToolbarLayout As System.Integer
Dim KeyboardShortcuts As System.Boolean
Dim MouseGestures As System.Boolean
Dim MenuCustomization As System.Boolean
Dim SavedViews As System.Boolean
Dim value As System.Integer
 
value = instance.SaveSettings(FileName, SystemOptions, ToolbarLayout, KeyboardShortcuts, MouseGestures, MenuCustomization, SavedViews)
```

```

System.int SaveSettings( 
   System.string FileName,
   System.bool SystemOptions,
   System.int ToolbarLayout,
   System.bool KeyboardShortcuts,
   System.bool MouseGestures,
   System.bool MenuCustomization,
   System.bool SavedViews
)
```

```

System.int SaveSettings( 
   System.String^ FileName,
   System.bool SystemOptions,
   System.int ToolbarLayout,
   System.bool KeyboardShortcuts,
   System.bool MouseGestures,
   System.bool MenuCustomization,
   System.bool SavedViews
) 
```

#### Parameters

*FileName*
:   Full path and filename to which to save the settings (**\*.sldreg**)

*SystemOptions*
:   True to save system options, false to not

*ToolbarLayout*
:   Toolbar layout as defined in [swToolbarLayoutOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swToolbarLayoutOption_e.html)

*KeyboardShortcuts*
:   True to save keyboard shortcuts, false to not

*MouseGestures*
:   True to save mouse gestures, false to not

*MenuCustomization*
:   True to save menu customizations, false to not

*SavedViews*
:   True to save views, false to not

#### Return Value

Error code as defined in [swSaveRestoreSettingsResults\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSaveRestoreSettingsResults_e.html)

Remarks

For C++ only, specify all System.bool parameters using VARIANT\_TRUE (-1) and VARIANT\_FALSE (0).

Example

' VBA precondition:

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
[ISldWorks::RestoreSettings Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RestoreSettings.md)  
[ISldWorks::LoadAdminSettingsFile Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadAdminSettingsFile.md)
