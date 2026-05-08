# DPartDocEvents_PreRenameItemNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_PreRenameItemNotifyEventHandler`

Fired when a part document referenced by other documents is about to be renamed.
Fired when a part document referenced by other documents is about to be renamed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_PreRenameItemNotifyEventHandler( _
   ByVal EntityType As System.Integer, _
   ByVal oldName As System.String, _
   ByVal NewName As System.String _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_PreRenameItemNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_PreRenameItemNotifyEventHandler( 
   System.int EntityType,
   System.string oldName,
   System.string NewName
)
```

```

public delegate System.int DPartDocEvents_PreRenameItemNotifyEventHandler( 
   System.int EntityType,
   System.String^ oldName,
   System.String^ NewName
)
```

#### Parameters

*EntityType*
:   :   Type of item to rename as defined in [swNotifyEntityType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swNotifyEntityType_e.html)

*oldName*
:   :   Current name of the part document

*NewName*
:   New name of the part document

Remarks

If developing a C++ application, use [swPartPreRenameItemNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Example

[Fire Notifications When Renaming Part Document Belonging to Assembly (C#)](Fire_Notifications_When_Renaming_Part_Document_Belonging_to_Assembly_Example_CSharp.htm)  
[Fire Notifications When Renaming Part Document Belonging to Assembly (VB.NET)](Fire_Notifications_When_Renaming_Part_Document_Belonging_to_Assembly_Example_VBNET.htm)  
[Fire Notifications When Renaming Part Document Belonging to Assembly (VBA)](Fire_Notifications_When_Renaming_Part_Document_Belonging_to_Assembly_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_PreRenameItemNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_PreRenameItemNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
