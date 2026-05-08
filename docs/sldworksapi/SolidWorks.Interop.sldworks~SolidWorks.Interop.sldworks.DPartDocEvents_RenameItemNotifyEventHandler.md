# DPartDocEvents_RenameItemNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_RenameItemNotifyEventHandler`

Fired when an item is renamed in one of the SOLIDWORKS tree structures, such as the FeatureManager design tree or the ConfigurationManager.
Fired when an item is renamed in one of the SOLIDWORKS tree structures, such as the FeatureManager design tree or the ConfigurationManager.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_RenameItemNotifyEventHandler( _
   ByVal EntityType As System.Integer, _
   ByVal oldName As System.String, _
   ByVal NewName As System.String _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_RenameItemNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_RenameItemNotifyEventHandler( 
   System.int EntityType,
   System.string oldName,
   System.string NewName
)
```

```

public delegate System.int DPartDocEvents_RenameItemNotifyEventHandler( 
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

If developing a C++ application, use [swPartRenameItemNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Example

[Fire Notifications When Renaming Part Document Belonging to Assembly (C#)](Fire_Notifications_When_Renaming_Part_Document_Belonging_to_Assembly_Example_CSharp.htm)  
[Fire Notifications When Renaming Part Document Belonging to Assembly (VB.NET)](Fire_Notifications_When_Renaming_Part_Document_Belonging_to_Assembly_Example_VBNET.htm)  
[Fire Notifications When Renaming Part Document Belonging to Assembly (VBA)](Fire_Notifications_When_Renaming_Part_Document_Belonging_to_Assembly_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_RenameItemNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_RenameItemNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
