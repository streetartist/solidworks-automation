# GetChildren Method (IConfiguration)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetChildren`

Gets all of the children configurations of this derived configuration.
Gets all of the children configurations of this derived configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetChildren() As System.Object
```

```

Dim instance As IConfiguration
Dim value As System.Object
 
value = instance.GetChildren()
```

```

System.object GetChildren()
```

```

System.Object^ GetChildren(); 
```

#### Return Value

Array containing the children [configurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md) of this configuration

Remarks

To determine if this configuration is derived, call [IConfiguration::IsDerived](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IsDerived.md).

Example

[Traverse Hierarchy of Configurations (VBA)](Traverse_Hierarchy_of_Configurations_Example_VB.htm)  
[Work with Configurations (VBA)](Work_with_Configurations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::IGetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetChildren.md)  
[IConfiguration::GetParent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParent.md)  
[IConfiguration::GetChildrenCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetChildrenCount.md)  
[IConfiguration::GetRootComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent3.md)
