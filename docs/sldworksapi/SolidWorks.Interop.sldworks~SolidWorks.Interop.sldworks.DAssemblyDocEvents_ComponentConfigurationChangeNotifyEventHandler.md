# DAssemblyDocEvents_ComponentConfigurationChangeNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentConfigurationChangeNotifyEventHandler`

Fired when a reference component's configuration is being changed in an assembly.
Fired when a reference component's configuration is being changed in an assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_ComponentConfigurationChangeNotifyEventHandler( _
   ByVal componentName As System.String, _
   ByVal oldConfigurationName As System.String, _
   ByVal newConfigurationName As System.String _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_ComponentConfigurationChangeNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_ComponentConfigurationChangeNotifyEventHandler( 
   System.string componentName,
   System.string oldConfigurationName,
   System.string newConfigurationName
)
```

```

public delegate System.int DAssemblyDocEvents_ComponentConfigurationChangeNotifyEventHandler( 
   System.String^ componentName,
   System.String^ oldConfigurationName,
   System.String^ newConfigurationName
)
```

#### Parameters

*componentName*
:   Name of reference component whose configuration is changing

*oldConfigurationName*
:   Old name of reference component's configuration

*newConfigurationName*
:   New name of reference component's configuration

Remarks

If developing a C++ application, use [swAssemblyComponentConfigurationChangeNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Example

[Fire Notification When Changing Configuration of Reference Component (C#)](Fire_Notification_When_Changing_Configuration_of_Reference_Component_Example_CSharp.htm)  
[Fire Notification When Changing Configuration of Reference Component (VB.NET)](Fire_Notification_When_Changing_Configuration_of_Reference_Component__Example_VBNET.htm)  
[Fire Notification When Changing Configuration of Reference Component (VBA)](Fire_Notification_When_Changing_Configuration_of_Reference_Component_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_ComponentConfigurationChangeNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentConfigurationChangeNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
