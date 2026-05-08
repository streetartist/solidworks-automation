# DDrawingDocEvents_AddItemNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_AddItemNotifyEventHandler`

Notifies the user program when an item is added to one of the SOLIDWORKS tree structures (for example, FeatureManager design tree, ConfigurationManager tree, and so on).
Notifies the user program when an item is added to one of the SOLIDWORKS tree structures (for example, FeatureManager design tree, ConfigurationManager tree, and so on).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DDrawingDocEvents_AddItemNotifyEventHandler( _
   ByVal EntityType As System.Integer, _
   ByVal itemName As System.String _
) As System.Integer
```

```

Dim instance As New DDrawingDocEvents_AddItemNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DDrawingDocEvents_AddItemNotifyEventHandler( 
   System.int EntityType,
   System.string itemName
)
```

```

public delegate System.int DDrawingDocEvents_AddItemNotifyEventHandler( 
   System.int EntityType,
   System.String^ itemName
)
```

#### Parameters

*EntityType*
:   Type of the new item as defined in [swNotifyEntityType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNotifyEntityType_e.html)

*itemName*
:   Name of the new item

Remarks

This method supports the addition of configurations.

If developing a C++ application, use [swDrawingAddItemNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DDrawingDocEvents\_AddItemNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_AddItemNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
