# HideNewComponentModels Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~HideNewComponentModels`

Gets or sets whether new components are hidden in this inactive configuration.
Gets or sets whether new components are hidden in this inactive configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property HideNewComponentModels As System.Boolean
```

```

Dim instance As IConfiguration
Dim value As System.Boolean
 
instance.HideNewComponentModels = value
 
value = instance.HideNewComponentModels
```

```

System.bool HideNewComponentModels {get; set;}
```

```

property System.bool HideNewComponentModels {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True hides new components, false create new components as shown in this configuration

Remarks

This setting is only valid when the configuration is not the active configuration.

This property applies only to assembly configurations. SOLIDWORKS always returns false when you get this property on a part configuration. This property has no effect on part configurations.

Example

[Change Configuration Properties (VBA)](Change_Configuration_Properties_Example_VB.htm)  
[Traverse Hierarchy of Configurations (VBA)](Traverse_Hierarchy_of_Configurations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[SuppressNewComponentModels Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SuppressNewComponentModels.md)
