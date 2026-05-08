# DAssemblyDocEvents_DeleteItemNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_DeleteItemNotifyEventHandler`

Notifies the user program when an item is deleted from one of the SOLIDWORKS tree structures (for example, the FeatureManager design tree or the ConfigurationManager tree).
Notifies the user program when an item is deleted from one of the SOLIDWORKS tree structures (for example, the FeatureManager design tree or the ConfigurationManager tree).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_DeleteItemNotifyEventHandler( _
   ByVal EntityType As System.Integer, _
   ByVal itemName As System.String _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_DeleteItemNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_DeleteItemNotifyEventHandler( 
   System.int EntityType,
   System.string itemName
)
```

```

public delegate System.int DAssemblyDocEvents_DeleteItemNotifyEventHandler( 
   System.int EntityType,
   System.String^ itemName
)
```

#### Parameters

*EntityType*
:   Type of entity deleted as defined in [swNotifyEntityType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNotifyEntityType_e.html)

*itemName*
:   Name of entity deleted

Remarks

If developing a C++ application, use [swAssemblyDeleteItemNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

No explicit notification is available for a component reorder operation. However, component reordering generates [DeleteItemNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_DeleteItemNotifyEventHandler.md) and [AddItemNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_AddItemNotifyEventHandler.md) events.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_DeleteItemNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_DeleteItemNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
