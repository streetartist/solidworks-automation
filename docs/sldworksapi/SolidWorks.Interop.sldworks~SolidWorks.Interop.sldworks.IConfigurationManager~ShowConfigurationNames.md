# ShowConfigurationNames Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ShowConfigurationNames`

Gets or sets whether to display configuration names in ConfigurationManager.
Gets or sets whether to display configuration names in ConfigurationManager.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowConfigurationNames As System.Boolean
```

```

Dim instance As IConfigurationManager
Dim value As System.Boolean
 
instance.ShowConfigurationNames = value
 
value = instance.ShowConfigurationNames
```

```

System.bool ShowConfigurationNames {get; set;}
```

```

property System.bool ShowConfigurationNames {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to display configuration names, false to not

Remarks

If you set this property to false, you cannot set [IConfigurationManager::ShowConfigurationDescriptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ShowConfigurationDescriptions.md) to false. Either the name or the description of a configuration must be shown.

Example

[Work With Configurations (VBA)](Work_with_Configurations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.md)  
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.md)
