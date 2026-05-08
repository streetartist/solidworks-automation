# GetParent Method (IConfiguration)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParent`

Gets the parent configuration of this derived configuration.
Gets the parent configuration of this derived configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetParent() As Configuration
```

```

Dim instance As IConfiguration
Dim value As Configuration
 
value = instance.GetParent()
```

```

Configuration GetParent()
```

```

Configuration^ GetParent(); 
```

#### Return Value

Parent configuration of this derived configuration

Remarks

To determine if this configuration is derived, call [IConfiguration::IsDerived](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IsDerived.md).

Example

[Change Configuration Properties (VBA)](Change_Configuration_Properties_Example_VB.htm)  
[Traverse Hierarchy of Configurations (VBA)](Traverse_Hierarchy_of_Configurations_Example_VB.htm)  
[Work with Configurations (VBA)](Work_with_Configurations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetChildren.md)  
[IConfiguration::GetChildrenCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetChildrenCount.md)  
[IConfiguration::IGetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetChildren.md)  
[IConfigurationt::GetRootComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent3.md)
