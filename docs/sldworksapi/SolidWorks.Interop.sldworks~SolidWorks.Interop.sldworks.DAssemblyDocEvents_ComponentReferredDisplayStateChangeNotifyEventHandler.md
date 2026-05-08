# DAssemblyDocEvents_ComponentReferredDisplayStateChangeNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentReferredDisplayStateChangeNotifyEventHandler`

Fired when a component's referenced display state changes.
Fired when a component's referenced display state changes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_ComponentReferredDisplayStateChangeNotifyEventHandler( _
   ByVal componentModel As System.Object, _
   ByVal CompName As System.String, _
   ByVal oldDSId As System.Integer, _
   ByVal oldDSName As System.String, _
   ByVal newDSId As System.Integer, _
   ByVal newDSName As System.String _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_ComponentReferredDisplayStateChangeNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_ComponentReferredDisplayStateChangeNotifyEventHandler( 
   System.object componentModel,
   System.string CompName,
   System.int oldDSId,
   System.string oldDSName,
   System.int newDSId,
   System.string newDSName
)
```

```

public delegate System.int DAssemblyDocEvents_ComponentReferredDisplayStateChangeNotifyEventHandler( 
   System.Object^ componentModel,
   System.String^ CompName,
   System.int oldDSId,
   System.String^ oldDSName,
   System.int newDSId,
   System.String^ newDSName
)
```

#### Parameters

*componentModel*
:   [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) whose referenced display state is changing

*CompName*
:   Name of component

*oldDSId*
:   Original referenced display state ID of the component

*oldDSName*
:   Original referenced display state name for the component

*newDSId*
:   New referenced display state ID of the component

*newDSName*
:   New referenced display state name for the component

Remarks

If developing a C++ application, use [ComponentReferredDisplayStateChangeNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Example

[Fire Notification When Component Referenced Display State Changes (C#)](Fire_Notification_When_Component_Referenced_Display_State_Changes_Example_CSharp.htm)  
[Fire Notification When Component Referenced Display State Changes (VB.NET)](Fire_Notification_When_Component_Referenced_Display_State_Changes_Example_VBNET.htm)  
[Fire Notification When Component Referenced Display State Changes (VBA)](Fire_Notification_When_Component_Referenced_Display_State_Changed_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_ComponentReferredDisplayStateChangeNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentReferredDisplayStateChangeNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
