# DAssemblyDocEvents_PreRenameItemNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_PreRenameItemNotifyEventHandler`

Fired when a component document in an assembly is about to be renamed.
Fired when a component document in an assembly is about to be renamed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_PreRenameItemNotifyEventHandler( _
   ByVal EntityType As System.Integer, _
   ByVal oldName As System.String, _
   ByVal NewName As System.String _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_PreRenameItemNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_PreRenameItemNotifyEventHandler( 
   System.int EntityType,
   System.string oldName,
   System.string NewName
)
```

```

public delegate System.int DAssemblyDocEvents_PreRenameItemNotifyEventHandler( 
   System.int EntityType,
   System.String^ oldName,
   System.String^ NewName
)
```

#### Parameters

*EntityType*
:   Type of item to rename as defined in [swNotifyEntityType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swNotifyEntityType_e.html)

*oldName*
:   Current name of the component document

*NewName*
:   New name of the component document

Remarks

This event is also fired when [IComponent2::MakeVirtual](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~MakeVirtual.md) is called.

If developing a C++ application, use [swAssemblyPreRenameItemNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Example

[Fire Notifications When Renaming Components (C#)](Fire_Notifications_When_Renaming_Components_Example_CSharp.htm)  
[Fire Notifications When Renaming Components (VB.NET)](Fire_Notifications_When_Renaming_Components_Example_VBNET.htm)  
[Fire Notifications When Renaming Components (VBA)](Fire_Notifications_When_Renaming_Components_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_PreRenameItemNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_PreRenameItemNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
