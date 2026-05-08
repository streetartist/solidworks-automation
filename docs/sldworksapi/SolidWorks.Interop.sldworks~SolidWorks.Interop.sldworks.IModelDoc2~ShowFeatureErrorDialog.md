# ShowFeatureErrorDialog Property (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowFeatureErrorDialog`

Gets or sets whether to display the feature error dialog.
Gets or sets whether to display the feature error dialog.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowFeatureErrorDialog As System.Boolean
```

```

Dim instance As IModelDoc2
Dim value As System.Boolean
 
instance.ShowFeatureErrorDialog = value
 
value = instance.ShowFeatureErrorDialog
```

```

System.bool ShowFeatureErrorDialog {get; set;}
```

```

property System.bool ShowFeatureErrorDialog {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True displays an error dialog, false does not

Remarks

This property controls the display of error dialogs generated when an error occurs during a rebuild of a specific feature in the current SOLIDWORKS session. Use [ISldWorks::GetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceToggle.md) or [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.md) to get or set swShowErrorsEveryRebuild, which controls the display of error dialogs generated when a rebuild warning error message is generated.

You can wrap the rebuild API call with the following code to suppress rebuild warning dialogs:

bValue = swApp.GetUserPreferenceToggle(swShowErrorsEveryRebuild)

swApp.SetUserPreferenceToggle swShowErrorsEveryRebuild, false

swModel.ForceRebuild3

swApp.SetUserPreferenceToggle swShowErrorsEveryRebuild, bValue

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::ForceRebuild3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.md)
