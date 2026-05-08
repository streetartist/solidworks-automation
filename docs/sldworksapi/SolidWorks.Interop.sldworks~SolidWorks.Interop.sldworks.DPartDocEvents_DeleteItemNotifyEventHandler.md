# DPartDocEvents_DeleteItemNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_DeleteItemNotifyEventHandler`

Notifies the user program when an item is deleted from one of the SOLIDWORKS tree structures, such as the FeatureManager design tree and the ConfigurationManager.
Notifies the user program when an item is deleted from one of the SOLIDWORKS tree structures, such as the FeatureManager design tree and the ConfigurationManager.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_DeleteItemNotifyEventHandler( _
   ByVal EntityType As System.Integer, _
   ByVal itemName As System.String _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_DeleteItemNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_DeleteItemNotifyEventHandler( 
   System.int EntityType,
   System.string itemName
)
```

```

public delegate System.int DPartDocEvents_DeleteItemNotifyEventHandler( 
   System.int EntityType,
   System.String^ itemName
)
```

#### Parameters

*EntityType*
:   Type of item deleted as defined in [swNotifyEntityType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNotifyEntityType_e.html)

*itemName*
:   Name of the deleted item

Remarks

If developing a C++ application, use [swPartDeleteItemNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_DeleteItemNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_DeleteItemNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
