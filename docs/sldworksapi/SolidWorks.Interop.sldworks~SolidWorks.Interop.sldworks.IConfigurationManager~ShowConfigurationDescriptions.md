# ShowConfigurationDescriptions Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ShowConfigurationDescriptions`

Gets or sets whether to display configuration descriptions in ConfigurationManager.
Gets or sets whether to display configuration descriptions in ConfigurationManager.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowConfigurationDescriptions As System.Boolean
```

```

Dim instance As IConfigurationManager
Dim value As System.Boolean
 
instance.ShowConfigurationDescriptions = value
 
value = instance.ShowConfigurationDescriptions
```

```

System.bool ShowConfigurationDescriptions {get; set;}
```

```

property System.bool ShowConfigurationDescriptions {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to display configuration descriptions, false to not

Remarks

If you set this property to false, you cannot set [IConfigurationManager::ShowConfigurationNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ShowConfigurationNames.md) to false. Either the name or the description of a configuration must be shown.

Example

[Work With Configurations (VBA)](Work_with_Configurations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.md)  
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.md)
