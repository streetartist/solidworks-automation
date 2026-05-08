# DPartDocEvents_DeleteItemPreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_DeleteItemPreNotifyEventHandler`

Notifies the user program when an item is about to be deleted from one of the SOLIDWORKS tree structures, such as the FeatureManager design tree and the ConfigurationManager.
Notifies the user program when an item is about to be deleted from one of the SOLIDWORKS tree structures, such as the FeatureManager design tree and the ConfigurationManager.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_DeleteItemPreNotifyEventHandler( _
   ByVal EntityType As System.Integer, _
   ByVal itemName As System.String _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_DeleteItemPreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_DeleteItemPreNotifyEventHandler( 
   System.int EntityType,
   System.string itemName
)
```

```

public delegate System.int DPartDocEvents_DeleteItemPreNotifyEventHandler( 
   System.int EntityType,
   System.String^ itemName
)
```

#### Parameters

*EntityType*
:   Type of item deleted as defined in [swNotifyEntityType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNotifyEntityType_e.html)

*itemName*
:   Name of the item to be deleted

Remarks

Use [IPartDoc::FeatureByName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FeatureByName.md) or [IPartDoc::IFeatureByName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IFeatureByName.md) to get the object to be deleted.

If developing a C++ application, use [swPartDeleteItemPreNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_DeleteItemPreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_DeleteItemPreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
