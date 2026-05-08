# IGetChildren Method (IConfiguration)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetChildren`

Gets all of the children configurations of this derived configuration.
Gets all of the children configurations of this derived configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetChildren( _
   ByVal NumChildren As System.Integer _
) As Configuration
```

```

Dim instance As IConfiguration
Dim NumChildren As System.Integer
Dim value As Configuration
 
value = instance.IGetChildren(NumChildren)
```

```

Configuration IGetChildren( 
   System.int NumChildren
)
```

```

Configuration^ IGetChildren( 
   System.int NumChildren
) 
```

#### Parameters

*NumChildren*
:   Number of children configurations of this configuration

#### Return Value

- in-process, unmanaged C++: Pointer to an array containing the children [configurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md) of this configuration

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

To determine if this configuration is derived, call [IConfiguration::IsDerived](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IsDerived.md).

Before calling this method, call [IConfiguration::GetChildrenCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetChildrenCount.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetChildren.md)  
[IConfiguration::GetParent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParent.md)  
[IConfiguration::GetRootComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent3.md)
