# DDrawingDocEvents_RenameItemNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_RenameItemNotifyEventHandler`

Notifies the user program when an item is renamed in one of the SOLIDWORKS tree structures (for example, such as the FeatureManager design tree or the ConfigurationManager tree).
Notifies the user program when an item is renamed in one of the SOLIDWORKS tree structures (for example, such as the FeatureManager design tree or the ConfigurationManager tree).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DDrawingDocEvents_RenameItemNotifyEventHandler( _
   ByVal EntityType As System.Integer, _
   ByVal oldName As System.String, _
   ByVal NewName As System.String _
) As System.Integer
```

```

Dim instance As New DDrawingDocEvents_RenameItemNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DDrawingDocEvents_RenameItemNotifyEventHandler( 
   System.int EntityType,
   System.string oldName,
   System.string NewName
)
```

```

public delegate System.int DDrawingDocEvents_RenameItemNotifyEventHandler( 
   System.int EntityType,
   System.String^ oldName,
   System.String^ NewName
)
```

#### Parameters

*EntityType*
:   Type of item renamed as defined in [swNotifyEntityType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNotifyEntityType_e.html)

*oldName*
:   Previous item name

*NewName*
:   New item name

Remarks

This supports the renaming of configurations.

If developing a C++ application, use [swDrawingRenameItemNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DDrawingDocEvents\_RenameItemNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_RenameItemNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
