# UseDocDisplaySettings Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~UseDocDisplaySettings`

Gets or sets whether to use the document defaults for this center mark's display settings.
Gets or sets whether to use the document defaults for this center mark's display settings.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseDocDisplaySettings As System.Boolean
```

```

Dim instance As ICenterMark
Dim value As System.Boolean
 
instance.UseDocDisplaySettings = value
 
value = instance.UseDocDisplaySettings
```

```

System.bool UseDocDisplaySettings {get; set;}
```

```

property System.bool UseDocDisplaySettings {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True uses the document defaults, false does not

Remarks

You can use the following user-preference methods to get or set these document defaults:

- [IModelDocExtension::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceToggle.md) or [IModelDocExtension::GetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceToggle.md) -  swDetailingCenterMarkShowLines, swDetailingNoOptionSpecified
- [IModelDocExtension::SetUserPreferenceDouble](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceDouble.md) or [IModelDocExtension::GetUserPreferenceDouble](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceDouble.md) - swDetailingCenterMarkSize, swDetailingNoOptionSpecified

Example

[List Center Marks in Drawing (VBA)](List_Center_Marks_in_Drawing_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.md)  
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.md)
