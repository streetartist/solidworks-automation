# ShowPreview Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ShowPreview`

Gets or sets whether to display the preview of a selected configuration.
Gets or sets whether to display the preview of a selected configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowPreview As System.Boolean
```

```

Dim instance As IConfigurationManager
Dim value As System.Boolean
 
instance.ShowPreview = value
 
value = instance.ShowPreview
```

```

System.bool ShowPreview {get; set;}
```

```

property System.bool ShowPreview {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to display the preview, false to restore the original ConfigurationManager

Remarks

Before using this property, you must activate and select the configuration to preview. If multiple configurations are selected, the last one's preview is displayed. The preview displays in the configuration pane below or above the pane of the selected configuration.

Example

[Work With Configurations (VBA)](Work_with_Configurations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.md)  
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.md)
